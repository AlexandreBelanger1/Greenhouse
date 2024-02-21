import RPi.GPIO as GPIO
import time
from DHT20Script import read_data

GPIO.setmode(GPIO.BCM)
temp_led = 16
humid_led = 26

GPIO.setup(temp_led, GPIO.OUT)
GPIO.setup(humid_led, GPIO.OUT)

GPIO.output(temp_led, GPIO.HIGH)
GPIO.output(humid_led, GPIO.LOW)
time.sleep(0.5)
GPIO.output(humid_led, GPIO.HIGH)
GPIO.output(temp_led, GPIO.LOW)
time.sleep(0.5)
GPIO.output(temp_led, GPIO.HIGH)
GPIO.output(humid_led, GPIO.LOW)
time.sleep(0.5)
GPIO.output(humid_led, GPIO.HIGH)
GPIO.output(temp_led, GPIO.LOW)
time.sleep(0.5)
GPIO.output(temp_led, GPIO.LOW)
GPIO.output(humid_led, GPIO.LOW)

temp_thres = 31.0
humid_thres = 42.0

try:
    while True:
        temp, humidity = read_data()
        if (temp != None) and (humidity != None):
            if temp > temp_thres:
                GPIO.output(temp_led, GPIO.HIGH)
                print(f"High Temp Detected {temp} C, Red LED turned on")
            else:
                GPIO.output(temp_led, GPIO.LOW)
            if humidity < humid_thres:
                GPIO.output(humid_led, GPIO.HIGH)
                print(f"Low Humidity warning {humidity}%, turning on Blue LED")
            else:
                GPIO.output(humid_led, GPIO.LOW)
        else:
            print("failed to read data from sensor")

        time.sleep(2)
except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    GPIO.cleanup()
    
