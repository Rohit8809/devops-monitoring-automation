# Installation Guide

## Environment

Operating System:

- CentOS Linux

---

## Components

- Node Exporter
- Prometheus
- Alertmanager
- Grafana
- Python Flask Middleware
- osTicket
- SMTP Email Integration

---

## Node Exporter Installation

Purpose:

- CPU Monitoring
- Load Monitoring
- Memory Monitoring
- Disk Monitoring

---

## Prometheus Installation

Responsibilities:

- Metric collection
- Alert rule evaluation
- Monitoring targets

Configuration Files:

- prometheus.yml
- alert.rules.yml

---

## Alertmanager Installation

Responsibilities:

- Alert grouping
- Alert routing
- Webhook delivery

Configuration File:

- alertmanager.yml

---

## Flask Middleware Setup

Responsibilities:

- Receive webhook alerts
- Parse JSON payload
- Create incidents in osTicket
- Send email notifications

Main Files:

- app.py
- requirements.txt

---

## Systemd Service

Purpose:

- Automatic startup after reboot

Service File:

- flask.service

Commands:

systemctl daemon-reload

systemctl enable flask

systemctl start flask

---

## osTicket Configuration

Responsibilities:

- Incident creation
- Ticket lifecycle management
- Priority handling

Integration:

- API Key
- Endpoint URL

---

## SMTP Email Configuration

Provider:

- Gmail SMTP

Purpose:

- Alert notifications
- Ticket notifications

---

## Grafana Configuration

Responsibilities:

- Dashboard visualization
- Alert creation
- Monitoring panels

---

## Verification

Verify services:

Prometheus

http://server_ip:9090

Alertmanager

http://server_ip:9093

Grafana

http://server_ip:3000

Flask Middleware

http://server_ip:5000

osTicket

http://server_ip/osticket
