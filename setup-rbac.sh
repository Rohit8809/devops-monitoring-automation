#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
env_file="$project_root/flask/.env"

if [[ ! -f "$env_file" ]]; then
    echo "Missing $env_file"
    exit 1
fi

if ! docker inspect flask-container >/dev/null 2>&1; then
    echo "flask-container must be running before password hashes are generated."
    exit 1
fi

read -r -s -p "Choose Rohit Kumar password (minimum 8 characters): " rohit_password
echo
read -r -s -p "Choose Kriti Thakur password (minimum 8 characters): " kriti_password
echo

if (( ${#rohit_password} < 8 || ${#kriti_password} < 8 )); then
    echo "Both passwords must contain at least 8 characters."
    exit 1
fi

rohit_hash="$(
    docker exec \
        -e RAW_PASSWORD="$rohit_password" \
        flask-container \
        python -c 'import os; from werkzeug.security import generate_password_hash; print(generate_password_hash(os.environ["RAW_PASSWORD"]))'
)"

kriti_hash="$(
    docker exec \
        -e RAW_PASSWORD="$kriti_password" \
        flask-container \
        python -c 'import os; from werkzeug.security import generate_password_hash; print(generate_password_hash(os.environ["RAW_PASSWORD"]))'
)"

secret_key="$(python3 -c 'import secrets; print(secrets.token_hex(32))')"

unset rohit_password kriti_password

cp "$env_file" "$env_file.before-rbac"

sed -i \
    -e '/^FLASK_SECRET_KEY=/d' \
    -e '/^ROHIT_PASSWORD_HASH=/d' \
    -e '/^KRITI_PASSWORD_HASH=/d' \
    "$env_file"

{
    printf '\nFLASK_SECRET_KEY=%s\n' "$secret_key"
    # Single quotes keep the "$" characters in Werkzeug hashes literal.
    # Without them, Docker Compose treats hash segments as variable names.
    printf "ROHIT_PASSWORD_HASH='%s'\n" "$rohit_hash"
    printf "KRITI_PASSWORD_HASH='%s'\n" "$kriti_hash"
} >> "$env_file"

docker compose \
    -f "$project_root/docker/docker-compose.yml" \
    up -d --force-recreate flask

echo
echo "RBAC configuration completed."
echo "Rohit username: rohit"
echo "Kriti username: kriti"
echo "Login page: http://localhost:5001/login"
