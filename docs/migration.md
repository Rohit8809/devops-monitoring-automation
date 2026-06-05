# Migration Guide

## Purpose

This document describes how to migrate the complete monitoring and incident management stack to another machine or cloud platform.

---

## Components to Migrate

- Prometheus
- Alertmanager
- Flask Middleware
- Grafana
- osTicket
- Systemd Services

---

## Prometheus

Files:

- prometheus.yml
- alert.rules.yml

Location:

/home/vagrant/prometheus-2.49.0.linux-amd64/

---

## Alertmanager

File:

- alertmanager.yml

Location:

/home/vagrant/alertmanager-0.27.0.linux-amd64/

---

## Flask Middleware

Files:

- app.py
- requirements.txt

Location:

/opt/alert_middleware/flask/

Install dependencies:

pip3 install -r requirements.txt

---

## Systemd Service

File:

- flask.service

Location:

/etc/systemd/system/

Commands:

systemctl daemon-reload

systemctl enable flask

systemctl start flask

systemctl status flask

---

## Grafana

Export:

- Dashboards
- Alert rules

Default Port:

3000

---

## osTicket

Backup Website:

tar -czvf osticket_backup.tar.gz /var/www/html/osticket

Backup Database:

mysqldump -u root -p osticket > osticket.sql

Restore Database:

mysql -u root -p osticket < osticket.sql

---

## Email Configuration

Provider:

- Gmail SMTP

Parameters:

- smtp.gmail.com
- Port 465
- SSL Enabled
- App Password

---

## GitHub Repository

Clone Project:

git clone git@github.com:Rohit8809/devops-monitoring-automation.git

---

## Verification

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

---

## Supported Platforms

- VMware
- VirtualBox
- AWS EC2
- Oracle Cloud
- Google Cloud Platform

