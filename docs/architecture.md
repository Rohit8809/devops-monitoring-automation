# System Architecture

## Overview

The Monitoring and Incident Management Automation project provides end-to-end infrastructure monitoring, alerting, ticket creation, and email notifications.

---

## Components

### Node Exporter

Collects system metrics such as:

- CPU utilization
- Load average
- Memory usage
- Disk usage

---

### Prometheus

Responsible for:

- Scraping metrics
- Evaluating alert rules
- Generating alerts

---

### Alertmanager

Responsible for:

- Receiving alerts from Prometheus
- Grouping alerts
- Routing alerts to Flask middleware

---

### Flask Middleware

Responsible for:

- Receiving webhook requests
- Parsing JSON payloads
- Creating incidents in osTicket
- Sending email notifications

---

### osTicket

Responsible for:

- Incident management
- Ticket lifecycle
- Priority handling

---

### SMTP

Responsible for:

- Email notifications
- Alert escalation

---

## Workflow

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
