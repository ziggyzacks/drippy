import json
import time

import paho.mqtt.client as mqtt
from constants import SENSOR_HEIGHT
from garden_state import State
from sensors import moisture, environment, ultrasonic, light
from vessel import Vessel

if __name__ == "__main__":
    client = mqtt.Client("home")
    client.connect(host="localhost")
    moisture_obj = moisture.Moisture()
    six_quart = Vessel(17.78, 21.59, 21.59)  # 7"x8.5"x8.5"
    distance_obj = ultrasonic.Distance(six_quart, SENSOR_HEIGHT)
    environ_obj = environment.Environment()
    light_obj = light.Light()

    state = State(moisture_obj, distance_obj, environ_obj, light_obj)
    while True:
        data = state.read()
        print(data)
        client.publish("garden/sensors", json.dumps(data))
        time.sleep(1)
