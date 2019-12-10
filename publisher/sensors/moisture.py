import adafruit_ads1x15.ads1015 as ADS
import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn


class Moisture:
    def __init__(self, _i2c=None):
        self.i2c = busio.I2C(board.SCL, board.SDA) or _i2c
        # Create the ADC object using the I2C bus
        self.ads = ADS.ADS1015(self.i2c)
        # Create single-ended input on channel 0
        self.chan = AnalogIn(self.ads, ADS.P0)

    def read(self):
        return self.chan.value
