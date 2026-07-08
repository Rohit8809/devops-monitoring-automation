import json
import os
from datetime import datetime

INCIDENT_STORE = "incident_store.json"


def current_time_utc():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")


def load_store():
    if not os.path.exists(INCIDENT_STORE):
        return {}

    with open(INCIDENT_STORE, "r") as file:
        return json.load(file)


def save_store(store):
    with open(INCIDENT_STORE, "w") as file:
        json.dump(store, file, indent=4)


def build_incident_key(alert_name, server):
    return f"{alert_name}|{server}"


def is_duplicate(alert_name, server):
    store = load_store()
    key = build_incident_key(alert_name, server)

    return key in store and store[key].get("status") == "open"


def get_existing_incident(alert_name, server):
    store = load_store()
    key = build_incident_key(alert_name, server)

    return store.get(key)


def register_incident(alert_name, server, ticket_number, severity, priority):
    store = load_store()
    key = build_incident_key(alert_name, server)

    now = current_time_utc()

    store[key] = {
        "ticket_number": ticket_number,
        "alert_name": alert_name,
        "server": server,
        "severity": severity,
        "priority": priority,
        "status": "open",
        "occurrence_count": 1,
        "created_at": now,
        "last_seen": now,
        "last_notification": now
    }

    save_store(store)
    return store[key]


def update_duplicate(alert_name, server):
    store = load_store()
    key = build_incident_key(alert_name, server)

    if key not in store:
        return None

    store[key]["occurrence_count"] = store[key].get("occurrence_count", 1) + 1
    store[key]["last_seen"] = current_time_utc()

    save_store(store)
    return store[key]


def close_incident(alert_name, server):
    store = load_store()
    key = build_incident_key(alert_name, server)

    if key in store:
        now = current_time_utc()

        store[key]["status"] = "closed"
        store[key]["closed_at"] = now
        store[key]["last_seen"] = now

        save_store(store)
        return store[key]

    return None