#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function

import matplotlib.pyplot as plt
import can
import numpy as np

def send_one():

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

    data_points = 0
    max_data_points = 1000

    while data_points <= max_data_points:
        recv_msg=recorder.get_message()
        if recv_msg != None:
            speed = recv_msg.data[1]*256+recv_msg.data[2]
            speed = float(speed)/256
            print(speed)
            data = np.append(data,speed)
            data_points = data_points +1
    
    np.savetxt('test_data_attack.dat', data)
            

if __name__ == '__main__':
    send_one()