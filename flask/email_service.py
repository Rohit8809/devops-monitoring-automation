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
    subject = "Test Email - Enterprise Incident Management Platform"

    body = """
Hello Team,

This is a test email from the Enterprise Incident Management Platform.

SMTP integration is working successfully.

Regards,
Enterprise Incident Management Platform
"""

    send_email(SUPPORT_EMAILS, subject, body)