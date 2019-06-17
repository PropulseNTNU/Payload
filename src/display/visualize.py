#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime
plt.style.use('ggplot')
#ts, roll,pitch,yaw,accel_x,accel_y,accel_z, comp_x, comp_y, comp_z,temp,humid,alti,pressure,gas,acc_temp = np.loadtxt('../sensory/Data.txt', delimiter='\t', unpack=True)#,usecols=(0,13))

#new_x = time.strftime("%Y-%m-%d %H:%M:%S", x)
arr = np.genfromtxt('../sensory/Data.txt', delimiter='\t', missing_values='',usemask=True )[:,:]
fig,axes = plt.subplots(nrows=3,ncols=5,sharex=True)
fig.suptitle("Propulse NTNU Payload 2019", fontsize=26)
axes[0,0].set_title('roll')
axes[1,0].set_title('pitch')
axes[2,0].set_title('yaw')

#accel
axes[0,1].set_title('Vibration X')
axes[1,1].set_title('Vibration Y')
axes[2,1].set_title('Gravity')

#compass
#axes[:,2].set_title("Compass")
axes[0,2].set_title('Compass X')
axes[1,2].set_title('Compass Y')
axes[2,2].set_title('Compass Z')

axes[0,3].set_title('temperature ')
axes[1,3].set_title('temperature ')
axes[2,3].set_title('humidity ')
axes[2,4].set_title('altitude ')

axes[0,4].set_title('pressure')
axes[1,4].set_title('gas ')

axes[0,0].plot (arr[1:,0],arr[1:,1])
axes[1,0].plot (arr[1:,0],arr[1:,2])
axes[2,0].plot (arr[1:,0],arr[1:,3])

axes[0,1].plot (arr[1:,0],arr[1:,4])
axes[1,1].plot (arr[1:,0],arr[1:,5])
axes[2,1].plot (arr[1:,0],arr[1:,6])

axes[0,2].plot (arr[1:,0],arr[1:,7])
axes[1,2].plot (arr[1:,0],arr[1:,8])
axes[2,2].plot (arr[1:,0],arr[1:,9])

axes[0,3].plot (arr[1:,0],arr[1:,10],label='bme680')
axes[1,3].plot (arr[1:,0],arr[1:,15],label='MCP9808')
axes[2,3].plot (arr[1:,0],arr[1:,11])
axes[2,4].plot (arr[1:,0],arr[1:,12])
axes[0,4].plot (arr[1:,0],arr[1:,13])
axes[1,4].plot (arr[1:,0],arr[1:,14])

axes[0,3].legend(loc='upper right', frameon=False)
axes[1,3].legend(loc='upper right', frameon=False)
#fig.axes.set_ylim(0,50)

figManager = plt.get_current_fig_manager()
#figManager.full_screen_toggle()

plt.show()

