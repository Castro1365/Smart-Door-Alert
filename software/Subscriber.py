"""
Smart Door Alert – MQTT Subscriber
----------------------------------

This Python script listens for door status updates ("open" / "closed")
published by the ESP8266 firmware. It connects to the public Mosquitto
broker and prints live door events to the console.

This script demonstrates the UI/console portion of the walking skeleton:
Device → MQTT Broker → Subscriber Output.

Run this file using:
    python subscriber.py
Ensure the ESP8266 is powered and publishing before running.
"""

import paho.mqtt.client as mqtt

# -----------------------------
# MQTT SETTINGS
# -----------------------------
BROKER = "test.mosquitto.org"              # Public MQTT broker
PORT = 1883                                # Default MQTT port
TOPIC = "smartdoor/castro_rupesh/status"   # Topic where ESP8266 publishes door status


# -----------------------------
# CALLBACKS
# -----------------------------

def on_connect(client, userdata, flags, rc):
    """Called when the client successfully connects to the broker."""
    print("Connected to MQTT Broker (RC={})".format(rc))
    client.subscribe(TOPIC)
    print(f"Subscribed to topic: {TOPIC}")


def on_message(client, userdata, msg):
    """Called whenever a message is received on a subscribed topic."""
    door_status = msg.payload.decode()
    print(f"Door Status Update → {door_status}")


# -----------------------------
# CLIENT SETUP
# -----------------------------

client = mqtt.Client()

# Attach callback functions
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to MQTT broker...")
client.connect(BROKER, PORT, keepalive=60)

print(f"Listening for messages on: {TOPIC}\n")

# -----------------------------
# START LOOP (BLOCKING)
# -----------------------------
client.loop_forever()
