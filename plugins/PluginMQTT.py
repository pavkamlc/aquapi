#!/usr/bin/python3

from Plugin import Plugin
import time
import paho.mqtt.client as paho

class PluginMQTT(Plugin):
    def __init__(self):
        raise AttributeError("undefined init method") 

mqttclient = paho.Client()  # create client object

def mqttconnect(host, port):

    def on_disconnect(client, userdata, rc):
        print("client disconnected ok")

    def on_publish(client, userdata, result):  # create function for callback
        print("data published \n")
        pass

    def on_connect(mosq, userdata, flags, rc):
        print(rc)
        print('connect event')

    def on_connect_fail(client, userdata, flags, rc):
        print("failed to connect")

    def on_message(client, userdata, msg):
        try:
            print(msg)
        except:
            print('message event')

    mqttclient.on_publish = on_publish  # assign function to callback
    mqttclient.on_disconnect = on_disconnect
    mqttclient.on_connect = on_connect
    mqttclient.on_message = on_message
    mqttclient.on_connect_fail = on_connect_fail

    try:
        print("mqtt connection")
        mqttclient.connect(host, port)  # establish connection

    except ConnectionRefusedError:
        print("Connection Refused")
    except ConnectionError:
        print("Connection Error")
    except Exception as err:
        print("Generic Exception: ", err)

def mqttsend(topic):
    print('Publish topic')
    return mqttclient.publish("house/bulb1", "on")  # publish

mqttconnect('badhost',1)
mqttsend('send')