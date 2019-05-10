#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function

import matplotlib.pyplot as plt
import can
import numpy as np
import random
import time

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
    msg = can.Message(arbitration_id=0x18FEF10B,
                      data=[0x33, 0x6C, 0x14, 0x7B, 0x82, 0x7F, 0xFF, 0xFF],
                      is_extended_id=True)
    speed = msg.data[1]*256+msg.data[2]

    while True:

        
        print(float(speed)/256)

        value = random.random()
        rnd_num = -1*100 + (value * (100 - (-1*100)))

        speed = int(speed + rnd_num)
        hex_num = hex(speed)
        hex_num = hex_num[2:6]
        byte_2 = hex_num[0:2]
        byte_3 = hex_num[2:4]

        msg.data[1] = int(byte_2,16)
        msg.data[2] = int(byte_3,16)
        try:
            bus.send(msg)
            #print("Message sent on {}".format(bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
            
        time.sleep(0.01)
        

if __name__ == '__main__':
    send_one()