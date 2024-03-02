
# import time
# import board
# from adafruit_seesaw.seesaw import Seesaw
# i2c_bus = board.I2C()

# ss = Seesaw(i2c_bus, addr=0x36)
# while True:
#  # read moisture level through capacitive touch pad
#  touch = ss.moisture_read()
#  # read temperature from the temperature sensor
#  temp = ss.get_temp()
#  print("temp: " + str(temp) + " moisture: " + str(touch))
#  time.sleep(1)

import board
import time
import RPi.GPIO as GPIO
from adafruit_seesaw.seesaw import Seesaw #This library will not work until,
                                          #you have activated the 'env' virtual environment!


#remember to activate the "env" environment before running this script
#testing out github setup on my local machine

# Setup
i2c_bus = board.I2C()
ss = Seesaw(i2c_bus, addr=0x36)

pump_pin = 17  # GPIO pin for the pump
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
GPIO.setup(pump_pin, GPIO.OUT)  # Set pump pin to output mode

moisture_threshold = 300  # This value needs to be tuned after some testing

def pump_control(turn_on):
    """Controls the pump based on the turn_on flag."""
    GPIO.output(pump_pin, turn_on)  # True to turn on, False to turn off

try:
    while True:
        # Read moisture level and temperature
        moisture = ss.moisture_read()
        temp = ss.get_temp()
        print(f"temp: {temp}, moisture: {moisture}")

        # Control pump based on moisture level
        if moisture < moisture_threshold:
            pump_control(True)  # Turn the pump ON if soil is dry
            print("Soil is dry, turning pump ON")
        else:
            pump_control(False)  # Turn the pump OFF if soil is moist
            print("Soil is moist, turning pump OFF")

        time.sleep(1)  # Need to decide the smapling frequency, right now it is smapling at 1000Hz

except KeyboardInterrupt:
    # Clean up GPIO state and exit
    GPIO.cleanup()
    print("Program exited cleanly")
