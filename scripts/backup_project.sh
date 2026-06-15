#!/bin/bash

DATE=$(date +%F_%H-%M-%S)

tar -czvf /opt/alert_middleware/backups/devops_project_$DATE.tar.gz \
        /opt/alert_middleware/flask \
        /opt/alert_middleware/prometheus \
        /opt/alert_middleware/alertmanager \
        /opt/alert_middleware/systemd \
        /opt/alert_middleware/docs \
        /opt/alert_middleware/grafana \
        /opt/alert_middleware/osticket \
        /opt/alert_middleware/README.md

