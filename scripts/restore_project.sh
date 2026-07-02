#!/bin/bash

BACKUP_FILE=$1

if [ -z "$BACKUP_FILE" ]
then
        echo "Usage: ./restore_project.sh <backup_file>"
        exit 1
fi

tar -xzvf $BACKUP_FILE -C /

echo "Restore completed successfully."
