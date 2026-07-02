# Cloud Architecture

## Current Environment

Platform: CentOS Virtual Machine

Components:

- Prometheus
- Alertmanager
- Flask Middleware
- Grafana
- osTicket
- Gmail SMTP

---

## Current Architecture

Node Exporter
     |
Prometheus
     |
Alertmanager
     |
Flask Middleware
     |
osTicket
     |
Email Notifications

Grafana Dashboard

---

## Target Environment

Future migration targets:

- AWS EC2
- Oracle Cloud Infrastructure (OCI)

---

## Proposed Architecture

Internet
    |
Public IP / Domain
    |
Cloud VM
    |
---------------------------------
| Prometheus                    |
| Alertmanager                  |
| Flask Middleware              |
| Grafana                       |
| osTicket                      |
---------------------------------
            |
         Gmail SMTP

---

## Benefits of Cloud Deployment

- Access from anywhere
- Easy backup and recovery
- Scalability
- High availability
- Centralized monitoring

---

## Future Enhancements

- Docker
- GitHub Actions CI/CD
- Kubernetes
- SSL certificates
- Domain names
- Slack integration
