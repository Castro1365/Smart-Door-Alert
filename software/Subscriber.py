import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPIC  = "smartdoor/castro_rupesh/status"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Door Status Update -> {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to broker...")
client.connect(BROKER, 1883, 60)

print(f"Listening on topic: {TOPIC}")
client.loop_forever()
