
# import board
# import time
# import RPi.GPIO as GPIO
# from adafruit_seesaw.seesaw import Seesaw #This library will not work until,
#                                           #you have activated the 'env' virtual environment!


# #remember to activate the "env" environment before running this script
# #testing out github setup on my local machine

# # Setup
# i2c_bus = board.I2C()
# ss = Seesaw(i2c_bus, addr=0x36)

# pump_pin = 17  # GPIO pin for the pump
# GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
# GPIO.setup(pump_pin, GPIO.OUT)  # Set pump pin to output mode

# moisture_threshold = 300  # This value needs to be tuned after some testing

# def pump_control(turn_on):
#     """Controls the pump based on the turn_on flag."""
#     GPIO.output(pump_pin, turn_on)  # True to turn on, False to turn off

# try:
#     while True:
#         # Read moisture level and temperature
#         moisture = ss.moisture_read()
#         temp = ss.get_temp()
#         print(f"temp: {temp}, moisture: {moisture}")

#         # Control pump based on moisture level
#         if moisture < moisture_threshold:
#             pump_control(True)  # Turn the pump ON if soil is dry
#             print("Soil is dry, turning pump ON")
#         else:
#             pump_control(False)  # Turn the pump OFF if soil is moist
#             print("Soil is moist, turning pump OFF")
        
#         time.sleep(1)  # Need to decide the smapling frequency, right now it is smapling at 1000Hz

# except KeyboardInterrupt:
#     # Clean up GPIO state and exit
#     GPIO.cleanup()
#     print("Program exited cleanly")



#Latest Version
import board
import time
import RPi.GPIO as GPIO
from adafruit_seesaw.seesaw import Seesaw

# Setup
i2c_bus = board.I2C()
ss = Seesaw(i2c_bus, addr=0x36)

pump_pin = 17  # GPIO pin for the pump
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
GPIO.setup(pump_pin, GPIO.OUT)  # Set pump pin to output mode

moisture_threshold = 300  # Tune this value based on testing
pump_on_duration = 5  # Pump will stay on for 5 seconds
last_pump_activation_time = 0  # Time when the pump was last activated

def pump_control(turn_on):
    """Controls the pump based on the turn_on flag."""
    global last_pump_activation_time
    if turn_on:
        GPIO.output(pump_pin, True)  # Turn the pump on
        time.sleep(pump_on_duration)  # Keep the pump on for 5 seconds
        GPIO.output(pump_pin, False)  # Then turn the pump off
        last_pump_activation_time = time.time()
    else:
        GPIO.output(pump_pin, False)  # Ensure the pump is off

try:
    while True:
        # Read moisture level and temperature
        moisture = ss.moisture_read()
        temp = ss.get_temp()
        print(f"temp: {temp}, moisture: {moisture}")

        current_time = time.time()
        # Check if enough time has passed since last activation
        if (current_time - last_pump_activation_time) > pump_on_duration:
            if moisture < moisture_threshold:
                print("Soil is dry, turning pump ON")
                pump_control(True)
            else:
                print("Soil is moist, turning pump OFF")
                pump_control(False)

        time.sleep(1)  # Adjust the sleep time as needed for your application

except KeyboardInterrupt:
    # Clean up GPIO state and exit
    GPIO.cleanup()
    print("Program exited cleanly")
