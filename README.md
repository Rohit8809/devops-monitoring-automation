 Monitoring & Incident Management Automation

## Overview

This project provides automated infrastructure monitoring and incident management using Prometheus, Alertmanager, Flask Middleware, osTicket, Grafana, and Email notifications.

The solution detects infrastructure issues, creates incidents automatically, and sends notifications to administrators without manual intervention.

---

## Technologies Used

- Linux (CentOS)
- Python Flask
- Prometheus
- Alertmanager
- Node Exporter
- Grafana
- osTicket
- Gmail SMTP
- Git & GitHub
- Systemd Services

---

## Features

### Monitoring

- CPU utilization monitoring
- Load average monitoring
- Service availability monitoring

### Alert Management

- Alert rules using Prometheus
- Alert routing using Alertmanager
- Alert severity classification
- Alert grouping

### Incident Automation

- Automatic ticket creation
- osTicket API integration
- Priority-based incident handling

### Email Notifications

- SMTP integration
- HTML email notifications
- Alert escalation emails

### Version Control

- Git repository
- GitHub integration
- SSH authentication

---

## Project Structure


alertmanager/
docs/
flask/
grafana/
osticket/
prometheus/
scripts/
systemd/


---

## Future Enhancements

- Cloud deployment (AWS / Oracle Cloud)
- GitHub Actions CI/CD
- Docker containers
- Kubernetes deployment
- Slack and Microsoft Teams integration
- Auto-remediation

