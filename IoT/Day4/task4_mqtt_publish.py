import paho.mqtt.client as mqtt

hostname = "test.mosquitto.org"  # Sandbox broker
port = 1883  # Default port for unencrypted MQTT

topic_traffic_light = "PCxxx/traffic_light/state"
topic_emergency = "PCxxx/traffic_light/emergency"

def publish_traffic_light_state(state):
    client = mqtt.Client()
    client.connect(hostname, port=port)
    client.publish(topic_traffic_light, str(state))
    client.disconnect()

def publish_emergency_status(status):
    client = mqtt.Client()
    client.connect(hostname, port=port)
    client.publish(topic_emergency, str(status))
    client.disconnect()