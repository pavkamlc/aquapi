#!/usr/bin/python3

import time
import paho.mqtt.client as paho

print("start")

broker = "192.168.1.184"
port = 1883
client1 = paho.Client("control1")  # create client object

ret = 0


def on_disconnect(client, userdata, rc):
    print("client disconnected ok")


def on_publish(client, userdata, result):  # create function for callback
    print("data published \n")
    pass


client1.on_publish = on_publish  # assign function to callback
client1.on_disconnect = on_disconnect

client1.connect(broker, port)  # establish connection

try:
    while True:
        ret = client1.publish("house/bulb1", "on")  # publish
        time.sleep(1)

except Exception:
    print("stop")
    client1.disconnect()

client1.disconnect()
