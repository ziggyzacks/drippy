import board
import busio
import adafruit_tsl2561


class Light:
    def __init__(self, _i2c=None):
        self.i2c = busio.I2C(board.SCL, board.SDA) or _i2c
        # Create the ADC object using the I2C bus
        self.light = adafruit_tsl2561.TSL2561(self.i2c)
        self.light.enabled = True
        # Set gain 0=1x, 1=16x
        self.light.gain = 0

    def read(self):
        return {
            'broadband': self.light.broadband,
            'infrared': self.light.infrared,
            'lux': self.light.lux
        }