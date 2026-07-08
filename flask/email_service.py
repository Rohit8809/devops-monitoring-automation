from datetime import datetime
from zoneinfo import ZoneInfo
import os
import smtplib
from email.mime.text import MIMEText


SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

SUPPORT_EMAILS = os.getenv("SUPPORT_EMAILS", "").split(",")
CLIENT_EMAILS = os.getenv("CLIENT_EMAILS", "").split(",")

SUPPORT_PHONE = os.getenv("SUPPORT_PHONE")
SERVICE_NAME = os.getenv("SERVICE_NAME", "Infrastructure Monitoring")
ENVIRONMENT = os.getenv("ENVIRONMENT", "Production")

def get_ist_time():
    return datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%d-%b-%Y %I:%M:%S %p IST")

def send_email(to_emails, subject, body):
    recipients = [email.strip() for email in to_emails if email.strip()]

    if not recipients:
        print("No email recipients configured")
        return

    msg = MIMEText(body, "plain")
    msg["Subject"] = subject
    msg["From"] = SMTP_USERNAME
    msg["To"] = ", ".join(recipients)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)

    print(f"Email sent to: {recipients}")


def send_test_email():
    pass


def build_support_email(ticket_number, alert_name, server, severity, priority, status, summary, description, start_time):
    generated_time = get_ist_time()

    subject = f"[{priority}][{severity.upper()}][{ticket_number}] {alert_name} | {server} | Immediate Action Required"

    body = f"""
Dear Support Team,

A new incident has been automatically created.

Incident Number : {ticket_number}
Priority        : {priority}
Severity        : {severity.upper()}
Alert Name      : {alert_name}
Server          : {server}
Service         : {SERVICE_NAME}
Environment     : {ENVIRONMENT}
Status          : {status.upper()}
Triggered At    : {start_time}
Generated At    : {generated_time}

Summary:
{summary}

Description:
{description}

Recommended Actions:
1. Verify the affected service/container status.
2. Check Docker and server health.
3. Review Prometheus target health.
4. Review application or service logs.
5. Restart the affected service if required.

Support Contact:
Email : {SUPPORT_EMAILS[0]}
Phone : {SUPPORT_PHONE}

Generated Automatically,
Enterprise Incident Management Platform
"""
    return subject, body


def build_client_email(ticket_number, severity, status, start_time):
    generated_time = get_ist_time()

    subject = f"[{ticket_number}][{severity.upper()}] Incident Created - {SERVICE_NAME}"

    body = f"""
Dear Customer,

An infrastructure incident has been detected.

Our monitoring platform has automatically created an incident and our engineering team has started investigating.

Incident Number : {ticket_number}
Severity        : {severity.upper()}
Affected Service: {SERVICE_NAME}
Environment     : {ENVIRONMENT}
Detected At     : {start_time}
Generated At    : {generated_time}
Current Status  : Investigation In Progress

There is no action required from your side at this time.

For urgent assistance:
Email : {SUPPORT_EMAILS[0]}
Phone : {SUPPORT_PHONE}

Regards,
Operations Team
"""
    return subject, body
