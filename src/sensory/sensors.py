#!/usr/bin/env python3
import sys, getopt
sys.path.append('.')
import RTIMU
import os.path
import time
from datetime import datetime
import math
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
import board
import busio
import adafruit_bme280
import adafruit_bmp280
import adafruit_bme680

import sys
sys.path.append('../rasspberryPI/bluetooth/NRF24L01/')
import blePITeensy as blePITeensy

###################
###### IMU ########
###################



def IMU_init():    
    global imu,s,SETTINGS_FILE
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



file = open("/home/pi/Payload/src/sensory/Data.txt","a")
#file.write("timestamp\troll\tpitch\tyaw\tacceleration x\tacceleration y\tacceleration z\tcompass x\tcompass y\tcompass z\ttemperature\thumidity\taltitude\tpressure\tgas\temprature_accurate_sensor\n")
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
    file.write(str(accelx) + "\t" + str(accely) + "\t" + str(accelz) + "\t" + str(0) + '\t')

    # Compass data
    compx, compy, compz = imu.getIMUData()['compass']
    compx = round(compx,2)
    compy = round(compy,2)
    compz = round(compz,2)
    file.write(str(compx) + "\t" + str(compy) + "\t" + str(compz) + "\t")
    return True
    #time.sleep(poll_interval*1.0/1000.0)



####################
####### BMP280 #####
####################

def BMP280_init(sea_level_pressure): # change this to match the location's pressure (hPa) at sea level
    i2c = busio.I2C(board.SCL, board.SDA)
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    bme280.sea_level_pressure = 1013.25









####################
####### BME680 #####
####################




sea_level_pressure = 1013.25

def BME680_init(sea_level_pressure):
    i2c = busio.I2C(board.SCL, board.SDA)
    bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
    bme680.sea_level_pressure = sea_level_pressure




def Read_BME680():
    temp = bme680.temperature
    humidity = bme680.humidity
    altitude = bme680.altitude
    pressure = bme680.pressure
    gas = bme680.gas 
    file.write(str(temp) + "\t" + str(humidity) + "\t" + str(altitude) + "\t" + str(pressure) + '\t' + str(gas))
















def Read_BMP():
    temp = bme280.temperature
    humidity = bme280.humidity
    altitude = bme280.altitude
    file.write(str(temp) + '\t' + str(humidity) + '\t' + str(altitude) + '\t' + 0 + '\t')


if  __name__ == "__main__":
    IMU_init()
    conn = blePITeensy.bleSetup()
    #bmp280_init()
    #bme680_init()
    while True:
        if imu.IMURead():
            Read_IMU()
            #Read_BME680()
            file.write("\n")
            blePITeensy.sendSensorData(conn)
        
        time.sleep(4/1000)
