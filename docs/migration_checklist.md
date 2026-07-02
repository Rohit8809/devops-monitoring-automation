gration Checklist

## Source Environment

Platform: CentOS VM

Components:

- Prometheus
- Alertmanager
- Flask Middleware
- Grafana
- osTicket
- Gmail SMTP

---

## Target Platforms

- AWS EC2
- Oracle Cloud Infrastructure
- New Laptop
- Virtual Machine

---

## Files to Migrate

### Flask

- app.py
- requirements.txt
- .env

### Prometheus

- prometheus.yml
- alert.rules.yml

### Alertmanager

- alertmanager.yml

### Systemd

- flask.service

### Documentation

- README.md
- installation.md
- architecture.md
- troubleshooting.md

### Backup Scripts

- backup_project.sh
- restore_project.sh

---

## Migration Steps

1. Provision new server.
2. Install required packages.
3. Clone GitHub repository.
4. Restore backup archive.
5. Configure systemd services.
6. Start services.
7. Validate monitoring and alerts.

---

## Post Migration Validation

- Prometheus accessible
- Grafana dashboards working
- Alertmanager operational
- Flask middleware running
- osTicket integration functioning
- Email notifications delivered
