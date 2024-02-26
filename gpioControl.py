import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.HIGH)
#GPIO.output(5, GPIO.LOW)

try:
    while True:
        time.sleep(0.1)
except:
    GPIO.cleanup()

