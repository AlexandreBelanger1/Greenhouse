import RPi.GPIO as GPIO
import time
from DHT20Script import read_data

GPIO.setmode(GPIO.BCM)

Fan_Control = 16            # GPIO pin for controlling the heating lamp
Heating_Lamp_Control = 20   # GPIO pin for controlling the heating lamp
Humidifer_Control = 26      # GPIO pin for controlling the humidifier

high_temp_thres = 26.0  # Higher Temperature threshold
low_temp_thres = 20.0       # Lower Temperature threshold
humid_thres = 42.0      # Humidity threshold

try:
    while True:
        temp, humidity = read_data()
        if (temp != None) and (humidity != None):
            if temp > high_temp_thres:
                GPIO.output(Fan_Control, GPIO.HIGH)
                print(f"High Temp Detected {temp} C, Fan turned on")
            else:
                GPIO.output(Fan_Control, GPIO.LOW)
            
            if temp < low_temp_thres:
                GPIO.output(Heating_Lamp_Control, GPIO.HIGH)
                print(f"Low Temp Detected {temp} C, Heating Lamp turned on")
            else:
                GPIO.output(Heating_Lamp_Control, GPIO.LOW)
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
    
