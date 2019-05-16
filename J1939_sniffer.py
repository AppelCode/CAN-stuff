#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import can
import numpy as np


# this uses the default configuration (for example from the config file)
# see http://python-can.readthedocs.io/en/latest/configuration.html
#bus = can.interface.Bus()

# Using specific buses works similar:
bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
# bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)
# bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
# bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, bitrate=250000)
# ...
bus.set_filters([{"can_id": 0x1FFEF1FF, "can_mask": 0x00FFFF00, "extended": True}])

recorder = can.BufferedReader()
notifier = can.Notifier(bus,[recorder])

data = np.array([])

data_point = 0
max_data_points = 1000

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

plt.xlabel('Sample')
plt.ylabel('Speed [km/hr]')
plt.grid(True)

x = []
y = []


def animate(i,x,y):
    recv_msg=recorder.get_message()

    if recv_msg != None:
        speed = recv_msg.data[1]*256+recv_msg.data[2]
        speed = float(speed)/256

        if len(x) > 1000:
            x.pop(0)
            y.pop(0)

        global data_point
        current_point = data_point

        x.append(current_point)
        y.append(speed)

        data_point = data_point +1
    
    print(y)
    ax1.clear()
    ax1.plot(x,y)
    
    plt.xlabel('Sample')
    plt.ylabel('Speed [km/hr]')
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')

ani = animation.FuncAnimation(fig, animate, fargs=(x, y), interval=1)
plt.show()
            
