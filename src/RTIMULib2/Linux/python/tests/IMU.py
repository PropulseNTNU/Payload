#!/usr/bin/env python
import sys, getopt
sys.path.append('.')
import RTIMU
import os.path
import time
from datetime import datetime
import math
#import matplotlib.pyplot as plt

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
print("Recommended Poll Interval: %dmS\n" % poll_interval)

file = open("cockballs.txt","a")

file.write("roll\tpitch\tyaw\tacceleration x\t acceleration y\t acceleration z\n")
while True:
    if imu.IMURead():
        x, y, z = imu.getFusionData()
        ts = imu.getIMUData()['timestamp']
        ts /= 1000
        file.write(str(x) + "\t"+ str(y) + "\t" + str(z)+ "\t")
        #resetfusion
        imu.getGyro
        #datetime.utcfromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ')
        accelx, accely, accelz = imu.getAccel()
        file.write(str(accelx) + "\t" + str(accely) + "\t" + str(accelz) + "\n")
        #imu.getCompass
        x = math.degrees(x)
        y = math.degrees(y)
        z  = math.degrees(z)
        #print("%f %f %f" % (x,y,z))
        print("%f %f %f" %(accelx , accely, accelz))
        time.sleep(poll_interval*1.0/1000.0)



