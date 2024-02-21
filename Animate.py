import time
import smbus
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from DHT20Script import read_data


temp_list = []
hum_list = []
time_list = []

fig, (ax_temp, ax_hum) = plt.subplots(2,1, figsize =(10,6))

def animate(i):
    temp, hum = read_data()
    if (temp != None) and (hum != None):
        temp_list.append(temp)
        hum_list.append(hum)
        time_list.append(i)

    ax_temp.clear()
    ax_temp.plot(time_list, temp_list)
    ax_temp.set_ylabel('Temperature (C)')
    ax_temp.set_ylim(22,28)
    ax_temp.set_yticks(range(22,28,1))

    ax_hum.clear()
    ax_hum.plot(time_list, hum_list)
    ax_hum.set_ylabel('Humidity (%)')
    ax_hum.set_ylim(25,75)
    ax_hum.set_yticks(range(25,76,5))


ani = FuncAnimation(fig, animate, interval = 100)

plt.tight_layout()
plt.show()
