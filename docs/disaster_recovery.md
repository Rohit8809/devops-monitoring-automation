# Disaster Recovery Guide

## Purpose

This document describes how to recover the monitoring platform in case of:

- Laptop failure
- VM corruption
- Accidental deletion
- Migration to a new laptop
- Migration to AWS or Oracle Cloud

---

## Backup Procedure

Run:

scripts/backup_project.sh

A backup archive will be generated under:

/opt/alert_middleware/backups

Example:

devops_project_2026-06-15_22-36-08.tar.gz

---

## Restore Procedure

Run:

scripts/restore_project.sh <backup_file>

Example:

./restore_project.sh \
/opt/alert_middleware/backups/devops_project_2026-06-15_22-36-08.tar.gz

---

## Components Covered

### Flask Middleware

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

### Grafana

- dashboard documentation

### osTicket

- integration documentation

---

## Cloud Migration

The backup archive can be restored on:

- AWS EC2
- Oracle Cloud
- New Laptop
- Virtual Machine

---

## Future Improvements

- Scheduled backups
- Cron jobs
- GitHub backup
- Database backup
- Docker volume backup
