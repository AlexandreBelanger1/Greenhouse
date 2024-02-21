import time
import smbus
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def read_data():
    address = 0x38
    try:
        i2cbus = smbus.SMBus(1)
        time.sleep(0.5)

        data = i2cbus.read_i2c_block_data(address, 0x71,1)
        if (data[0] | 0x08) == 0:
            print('Initialization error')
            return None, None
        i2cbus.write_i2c_block_data(address,0xac,[0x33,0x00])
        time.sleep(0.1)

        data = i2cbus.read_i2c_block_data(address,0x71,7)

        Traw = ((data[3] & 0xf) << 16) + (data[4] << 8) + data[5]
        temperature = 200*float(Traw)/2**20 - 50

        Hraw = ((data[3] & 0xf0) >> 4) + (data[1] << 12) + (data[2] << 4)
        humidity = 100*float(Hraw)/2**20

        return temperature, humidity

    except Exception as e:
        print(f"Error: {e}")
        return None, None

