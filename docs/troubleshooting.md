# Troubleshooting Guide

## GitHub Issues

### Invalid username or token

Cause:

- PAT token authentication issue.

Solution:

- Configure SSH authentication.
- Generate SSH key pair.
- Add public key to GitHub.

---

### Permission denied (publickey)

Cause:

- SSH key not added to GitHub.

Solution:

- Add id_ed25519.pub contents to GitHub SSH settings.

---

### HTTP 403 Error

Cause:

- Insufficient repository permissions.

Solution:

- Verify repository ownership.
- Use SSH authentication.

---

## SMTP Issues

### Host doesn't allow connection

Cause:

- Incorrect Gmail configuration.

Solution:

- Use smtp.gmail.com
- Port 465
- SSL enabled
- Gmail App Password

---

### Protocol Required

Cause:

- Incorrect port and encryption settings.

Solution:

- Enable SSL with port 465.

---

## Alertmanager Issues

### No alerts field found

Cause:

- Grafana payload format mismatch.

Solution:

- Modify Flask middleware parsing logic.

---

### DataSourceError Alerts

Cause:

- Prometheus datasource unavailable.

Solution:

- Verify datasource connectivity.
- Restart Prometheus if required.

---

## osTicket Issues

### Maximum Open Tickets Reached

Cause:

- Ticket limit exceeded.

Solution:

- Close old tickets.
- Increase open ticket limit.

---

### HTML Email Not Rendering

Cause:

- Email template sent as plain text.

Solution:

- Configure HTML email templates.

---

## Git Issues

### Working tree clean

Cause:

- No modified files.

Solution:

- Verify files using git status.

---

### Untracked Files

Cause:

- New files not added.

Solution:

git add .

---

## Flask Middleware Issues

### Webhook Parsing Failure

Cause:

- Unexpected JSON payload structure.

Solution:

- Add payload validation and error handling.

---

## Service Startup Issues

### Flask Service Not Starting

Cause:

- Incorrect systemd configuration.

Solution:

systemctl daemon-reload

systemctl restart flask

systemctl status flask

---

## Monitoring Issues

### CPU Alerts Trigger During Reboot

Cause:

- Services start before metrics stabilize.

Solution:

- Increase alert duration.
- Configure startup delay.
