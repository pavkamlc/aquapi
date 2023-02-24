#!/usr/bin/python3

import plugins.plugin
import time
import paho.mqtt.client as paho

mqtthost = 'badhost'
mqttport = 0

mqttclient = paho.Client()  # create client object

class PluginMQTT(plugins.plugin.Plugin):
    def __init__(self):
        mqttclient.on_publish = on_publish  # assign function to callback
        mqttclient.on_disconnect = on_disconnect
        mqttclient.on_connect = on_connect
        mqttclient.on_message = on_message
        mqttclient.on_connect_fail = on_connect_fail
    
    def load(self):
        try:
            print("mqtt connection")
            mqttclient.connect(mqtthost, mqttport)  # establish connection

        except ConnectionRefusedError:
            print("Connection Refused")
        except ConnectionError:
            print("Connection Error")
        except Exception as err:
            print("Generic Exception: ", err)
    
    def event(self, eventname, eventparameter):
        print('Publish topic')
        #return mqttclient.publish("house/bulb1", "on")  # publish
        return mqttclient.publish("house/bulb1", "eventparameter")  # publish
    
    def readconfig(self):
        mqtthost = ''
        mqttport = 1

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
                