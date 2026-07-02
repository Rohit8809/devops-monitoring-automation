# Migration Procedure

## Objective

Provide steps to migrate the monitoring platform to a new server.

---

## Source Environment

Platform

- CentOS Virtual Machine

Components

- Prometheus
- Alertmanager
- Flask Middleware
- Grafana
- osTicket

---

## Target Environment

Supported Platforms

- AWS EC2
- Oracle Cloud Infrastructure
- VMware Virtual Machines
- New Laptop
- CentOS
- Rocky Linux
- Ubuntu

---

## Migration Steps

### Step 1

Provision a new server.

Recommended Configuration

- 2 vCPU
- 4 GB RAM
- 50 GB SSD

---

### Step 2

Install required packages.

- Python 3
- Git
- Prometheus
- Alertmanager
- Grafana

---

### Step 3

Clone GitHub repository.

Example

git clone git@github.com:Rohit8809/devops-monitoring-automation.git

---

### Step 4

Restore backup archive.

Example

./restore_project.sh

---

### Step 5

Configure environment variables.

File

flask/.env

Contains

- OSTICKET_URL
- API_KEY
- SENDER_EMAIL
- SOURCE_IP

---

### Step 6

Configure systemd service.

File

systemd/flask.service

Commands

systemctl daemon-reload

systemctl enable flask

systemctl start flask

---

### Step 7

Validate components.

Prometheus

http://server_ip:9090

Alertmanager

http://server_ip:9093

Grafana

http://server_ip:3000

Flask Middleware

http://server_ip:5000

osTicket

http://server_ip

---

## Post Migration Verification

Verify:

- Prometheus targets are UP.
- Alert rules are firing correctly.
- Alertmanager receives alerts.
- Flask middleware receives webhook requests.
- osTicket creates incidents.
- Email notifications are delivered.

---

## Rollback Plan

If migration fails:

1. Restore backup archive.
2. Restart services.
3. Validate connectivity.
4. Revert to previous server.

---

## Future Migration Targets

- Docker Containers
- Kubernetes
- AWS EC2
- Oracle Cloud Infrastructure
