#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

plt.title('Velocity Sensor Value Trend Under Attack')
data = np.loadtxt('test_data.dat')
print(data.size)
x = np.arange(data.size)
print(x)
plt.plot(x,data)

plt.xlabel('Sample')
plt.ylabel('Speed [km/hr]')
plt.grid(True)
#plt.title('Velocity Sensor Value Trend Under Attack')

#data = np.loadtxt('test_data_attack.dat')
#print(data.size)
#x = np.arange(data.size)
#print(x)
#plt.plot(x,data)

plt.show()