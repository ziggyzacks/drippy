import csv
import pathlib
import time

from constants import SENSOR_HEIGHT
from garden_state import State
from sensors import moisture, ultrasonic, environment
from vessel import Vessel

if __name__ == "__main__":
    moisture_obj = moisture.Moisture()
    six_quart = Vessel(17.78, 21.59, 21.59)  # 7"x8.5"x8.5"
    distance_obj = ultrasonic.Distance(six_quart, SENSOR_HEIGHT)
    environ_obj = environment.Environment()

    state = State(moisture_obj, distance_obj, environ_obj)


    def read_batch(sleep_time=5, elapsed_batch=1800):
        readings = []
        elapsed = 0
        while elapsed < elapsed_batch:
            state_reading = state.read()
            state_reading['volume-remaining'] = six_quart.cross_section_area * (
                        distance_obj.sensor_height - state_reading['distance-to-water-surface'])
            print(state_reading)
            readings.append(state_reading)
            time.sleep(sleep_time)
            elapsed += sleep_time
        return readings


    def write_batch(readings):
        path = pathlib.Path(__file__).resolve().parent
        path = path / 'logs' / f"{time.time()}.csv"
        if not path.exists():
            path.touch()

        with open(path, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            for record in readings:
                spamwriter.writerow(list(record.values()))


    while True:
        readings = read_batch()
        write_batch(readings)
