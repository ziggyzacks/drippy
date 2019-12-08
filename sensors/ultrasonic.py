import time

import RPi.GPIO as GPIO


class Distance:

    def __init__(self, vessel, sensor_height):
        GPIO.setmode(GPIO.BCM)

        self.trigger = 23
        self.echo = 24
        self.vessel = vessel
        self.sensor_height = sensor_height

        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def read(self):
        GPIO.output(self.trigger, True)

        time.sleep(0.00001)
        GPIO.output(self.trigger, False)

        t0 = time.time()
        t1 = time.time()

        while GPIO.input(self.echo) == 0:
            t0 = time.time()

        while GPIO.input(self.echo) == 1:
            t1 = time.time()

        t_delta = t1 - t0
        distance = (t_delta * 34300) / 2

        return distance
