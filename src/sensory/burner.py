#!/usr/bin/env python3
import time
import board
from busio import I2C
import adafruit_bme680

# Create library object using our Bus I2C port
i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1006.0
file = open("/home/pi/payload/src/sensory/burning_data.txt","a")

while True:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    file.write("\ntimestamp: %d " % str(st))
    print("\ntimestamp: %d " % str(stt))
    print("Temperature: %0.1f C" % bme680.temperature)
    file.write("Temperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    file.write("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.humidity)
    file.write("Humidity: %0.1f %%" % bme680.humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    file.write("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)
    file.write("Altitude = %0.2f meters" % bme680.altitude)
    time.sleep(1)


#>>> st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
#import datetime
