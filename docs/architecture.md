ystem Architecture

Node Exporter
        ↓
Prometheus
        ↓
Alertmanager
        ↓
Flask Middleware
        ↓
osTicket API
        ↓
Ticket Creation
        ↓
SMTP Email Notification
        ↓
Administrator Team

---

## Workflow

1. Node Exporter collects metrics.
2. Prometheus evaluates alert rules.
3. Alertmanager routes alerts.
4. Flask middleware receives webhook requests.
5. Alert information is parsed.
6. Ticket is created in osTicket.
7. Email notifications are sent.
