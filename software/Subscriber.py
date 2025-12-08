"""
Python MQTT Subscriber + Data Logger for Smart Door Alert

- Connects to public MQTT broker (test.mosquitto.org)
- Subscribes to door status topic: smartdoor/castro_rupesh/status
- Prints live updates to the console
- Logs each event (timestamp + status) into ../data/events.csv
  -> This file is later used by the REST API for history queries.
"""

import os
import csv
from datetime import datetime

import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPIC = "smartdoor/castro_rupesh/status"

# Path to ../data/events.csv (relative to this file)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
EVENTS_FILE = os.path.join(DATA_DIR, "events.csv")


def ensure_data_file():
    """Create the /data folder and CSV file with header if they do not exist."""
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(EVENTS_FILE):
        with open(EVENTS_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "status"])  # CSV header row


def log_event(status: str):
    """
    Append a new door event to events.csv with current timestamp.
    This provides structured storage for later REST queries.
    """
    ensure_data_file()

    now = datetime.now().isoformat(timespec="seconds")
    with open(EVENTS_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([now, status])


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code:", rc)
    client.subscribe(TOPIC)
    print(f"Subscribed to topic: {TOPIC}")
    ensure_data_file()


def on_message(client, userdata, msg):
    status = msg.payload.decode().strip()
    print(f"Door Status Update -> {status}")

    # Log to CSV for history
    log_event(status)


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    print("Connecting to broker...")
    client.connect(BROKER, 1883, 60)

    print(f"Listening on topic: {TOPIC}")
    print(f"Logging events to: {EVENTS_FILE}")
    client.loop_forever()


if __name__ == "__main__":
    main()
