import RPi.GPIO as GPIO
import time
from datetime import datetime

light_pin = 18  # GPIO pin for the lights
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
GPIO.setup(light_pin, GPIO.OUT)  # Set light pin to output mode

def get_current_time():
    """Returns the current hour and minute."""
    now = datetime.now()
    return now.hour, now.minute

try:
    while True:
        current_hour, current_minute = get_current_time()

        # Check if current time is within the desired light on period
        if 7 <= current_hour < 17:  # From 7:00 am to 4:59 pm
            GPIO.output(light_pin, True)  # Turn lights on
        else:
            GPIO.output(light_pin, False)  # Turn lights off

        time.sleep(60*30)  # Check every half hour

except KeyboardInterrupt:
    # Clean up GPIO state and exit
    GPIO.cleanup()
    print("Program exited cleanly")
