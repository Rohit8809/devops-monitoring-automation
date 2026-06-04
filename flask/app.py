from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

OSTICKET_URL = "http://192.168.56.10/api/tickets.json"
API_KEY = "AFDDB0C29E2FF5F924E7BDDE5EB8DC2E"

@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.json

    print("========== ALERT RECEIVED ==========")
    print(json.dumps(data, indent=4))

    try:

        # ==================================
        # PROMETHEUS ALERT FORMAT
        # ==================================
        if 'alerts' in data:

            alert = data['alerts'][0]

            alert_name = alert.get('labels', {}).get('alertname', 'Unknown Alert')
            server = alert.get('labels', {}).get('instance', 'Unknown Server')
            severity = alert.get('labels', {}).get('severity', 'warning')
            status = alert.get('status', 'firing')

        # ==================================
        # GRAFANA DATASOURCE ALERT FORMAT
        # ==================================
        else:

            alert_name = data.get('title', 'Datasource Alert')
            server = "Grafana"
            severity = "critical"
            status = data.get('status', 'firing')

        print(f"Alert Name: {alert_name}")
        print(f"Server: {server}")
        print(f"Severity: {severity}")
        print(f"Status: {status}")

        if status == "resolved":
            print("Resolved alert ignored")

            return jsonify({
                "status": "resolved ignored"
            }), 200

        subject = f"[{severity.upper()}] {alert_name}"

        message = f"""
<html>
<head>
<style>
body {{
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    padding: 20px;
}}

.container {{
    background-color: white;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
}}

.header {{
    background-color: #d32f2f;
    color: white;
    padding: 15px;
    border-radius: 8px;
    font-size: 22px;
    font-weight: bold;
}}

.info-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}}

.info-table td {{
    border: 1px solid #ddd;
    padding: 12px;
}}

.label {{
    font-weight: bold;
    background-color: #f2f2f2;
    width: 30%;
}}

.footer {{
    margin-top: 20px;
    color: #555;
    font-size: 14px;
}}
</style>
</head>

<body>

<div class="container">

<div class="header">
Grafana Monitoring Alert
</div>

<p>Hello Team,</p>

<p>An infrastructure alert has been triggered from the monitoring platform.</p>

<table class="info-table">

<tr>
    <td class="label">Alert Name</td>
    <td>{alert_name}</td>
</tr>

<tr>
    <td class="label">Server</td>
    <td>{server}</td>
</tr>

<tr>
    <td class="label">Severity</td>
    <td>{severity.upper()}</td>
</tr>

<tr>
    <td class="label">Status</td>
    <td>{status.upper()}</td>
</tr>

</table>

<p>Please investigate the issue at the earliest.</p>

<div class="footer">
Regards,<br>
Monitoring Automation System<br>
Grafana | Prometheus | osTicket
</div>

</div>

</body>
</html>
"""

        payload = {
            "name": "Grafana Monitoring",
            "email": "devopstestalert@gmail.com",
            "subject": subject,
            "message": message,
            "ip": "192.168.56.10"
        }

        headers = {
            "X-API-Key": API_KEY,
            "Content-Type": "application/json"
        }

        response = requests.post(
            OSTICKET_URL,
            headers=headers,
            data=json.dumps(payload)
        )

        print("Ticket Response:", response.text)

    except Exception as e:
        print("Error:", e)

    return jsonify({
        "status": "success"
    }), 200


@app.route('/')
def home():
    return "Flask Alert Middleware Running"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
