import bme680


class Environment:
    def __init__(self):
        self.sensor = self._boostrap_sensor()

    def _boostrap_sensor(self):
        try:
            sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
        except IOError:
            sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

        # These oversampling settings can be tweaked to
        # change the balance between accuracy and noise in
        # the data.

        sensor.set_humidity_oversample(bme680.OS_2X)
        sensor.set_pressure_oversample(bme680.OS_4X)
        sensor.set_temperature_oversample(bme680.OS_8X)
        sensor.set_filter(bme680.FILTER_SIZE_3)
        sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

        sensor.set_gas_heater_temperature(320)
        sensor.set_gas_heater_duration(150)
        sensor.select_gas_heater_profile(0)
        return sensor

    def read(self):
        if self.sensor.get_sensor_data():
            data = self.sensor.data
            return {
                'temperature': data.temperature,
                'pressure': data.pressure,
                'humidity': data.humidity,
                'gas': data.gas_resistance
            }
        else:
            return {
                'temperature': "",
                'pressure': "",
                'humidity': "",
                'gas': ""
            }
