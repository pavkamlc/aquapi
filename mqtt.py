#!/usr/bin/python3

import time
import paho.mqtt.client as paho

import dbaccess

print("start")

config = dbaccess.dbgetconfig()
#topic = config.topic

client1 = paho.Client()  # create client object

ret = 0

def on_disconnect(client, userdata, rc):
    print("client disconnected ok")


def on_publish(client, userdata, result):  # create function for callback
    print("data published \n")
    pass

client1.on_publish = on_publish  # assign function to callback
client1.on_disconnect = on_disconnect

try:
    client1.connect(config['mqtt_host'], config['mqtt_port'])  # establish connection
    while True:
        print('Publish topic')
        ret = client1.publish("house/bulb1", "on")  # publish
        time.sleep(1)

except (Exception, ConnectionError, ConnectionRefusedError):
    print("stop")
    client1.disconnect()

client1.disconnect()
