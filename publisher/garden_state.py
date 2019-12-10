import time


class State:

    def __init__(self, moisture_sensor, distance_sensor, environment_sensor, light_sensor):
        self.moisture_sensor = moisture_sensor
        self.distance_sensor = distance_sensor
        self.environment_sensor = environment_sensor
        self.light_sensor = light_sensor

    def read(self):
        return {
            'moisture-level': self.moisture_sensor.read(),
            'distance-to-water-surface': self.distance_sensor.read(),
            **self.environment_sensor.read(),
            **self.light_sensor.read(),
            'time': time.time()
        }
