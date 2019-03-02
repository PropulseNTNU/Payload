#!/usr/bin/env python3
import sys, getopt
sys.path.append('.')
import RTIMU
import os.path
import time
from datetime import datetime
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import board
import busio
import adafruit_bme280
import adafruit_bmp280

###################
###### IMU ########
###################

SETTINGS_FILE = "RTIMULib"

print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
      print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

print("IMU Name: " + imu.IMUName())

if (not imu.IMUInit()):
    print("IMU Init Failed")
    sys.exit(1)
else:
    print("IMU Init Succeeded")

# this is a good time to set any fusion parameters

imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()
print("Poll Intervall: %dmS\n" % poll_interval)

file = open("cockballs.txt","a")
file.write("timestamp\troll\tpitch\tyaw\tacceleration x\tacceleration y\tacceleration z\tcompass x\tcompass y\tcompass z\tt\n")
# Vibration = acceleration z

def Read_IMU():
    #Timestamp 
    ts = imu.getIMUData()['timestamp']
    ts /= 1000
    file.write(str(ts) + "\t")

    # Fusion / Gyroscope data
    x, y, z = imu.getFusionData()
    x = round(math.degrees(x),2)
    y = round(math.degrees(y),2)
    z  = round(math.degrees(z),2)
    file.write(str(x) + "\t"+ str(y) + "\t" + str(z)+ "\t")

    #resetfusion
    imu.getGyro
    #datetime.utcfromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Acceleration data, accely is spin, accelz is acceleration,
    accelx, accely, accelz = imu.getAccel()
    accelx = round(accelx,2)
    accely = round(accely,2)
    accelz = round(accelz,2)
    file.write(str(accelx) + "\t" + str(accely) + "\t" + str(accelz) + "\t")

    # Compass data
    compx, compy, compz = imu.getIMUData()['compass']
    compx = round(compx,2)
    compy = round(compy,2)
    compz = round(compz,2)
    file.write(str(compx) + "\t" + str(compy) + "\t" + str(compz) + "\t")
    return True
    #time.sleep(poll_interval*1.0/1000.0)

'''
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []'''
def animate(xs,ys):
    accelx, accely, accelz = imu.getAccel()
    accelz = accelz / (2*3.14)*1000
    print(accelz)
    xs.append(datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(accelz)
    xs = xs[-20:]
    ys = ys[-20:]
    ax.clear()
    ax.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('MPU-9255 vibration Z over time')
    plt.ylabel('Hertz')


####################
####### BMP280 #####
####################


#i2c = busio.I2C(board.SCL, board.SDA)

#bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# OR create library object using our Bus SPI port
#spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
#bme_cs = digitalio.DigitalInOut(board.D10)
#bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

# change this to match the location's pressure (hPa) at sea level
#bme280.sea_level_pressure = 1013.25


def Read_BMP():
    temp = bme280.temperature
    humidity = bme280.humidity
    altitude = bme280.altitude
    file.write(str(temp) + '\t' + str(humidity) + '\t' + str(altitude) + '\t')


if  __name__ == "__main__":
    while True:
        if imu.IMURead():
            Read_IMU()
            file.write("\n")
        time.sleep(4/1000)
        '''fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        xs = []
        ys = []
        animate(xs,ys)
        #ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys), interval = 5)
        plt.show()'''
