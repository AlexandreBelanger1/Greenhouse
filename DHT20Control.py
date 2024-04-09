import RPi.GPIO as GPIO
import time
from DHT20Script import read_data
from soil_moisture import read_sensor

GPIO.setmode(GPIO.BCM)

Fan_Control = 16            # GPIO pin for controlling the heating lamp
Heating_Lamp_Control = 20   # GPIO pin for controlling the heating lamp
Humidifer_Control = 26      # GPIO pin for controlling the humidifier

high_temp_thres = 24.0  # Higher Temperature threshold
low_temp_thres = 20.5   # Lower Temperature threshold
high_humid_thres = 60.0     # Humidity threshold
low_humid_thres = 35.0      # Humidity threshold


try:
    while True:
        temp_air, humidity = read_data()
        moisture, temp_soil = read_sensor()
        temp = (temp_air + temp_soil)/2             #taking average of air and soil temperature
        
        if (temp != None) and (humidity != None):

            #Logic for controlling temperature
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

            #Logic for controlling humidity
            if humidity < low_humid_thres:
                GPIO.output(Humidifer_Control, GPIO.HIGH)
                print(f"Low Humidity warning {humidity}%, turning on Humidifier")
            else:
                GPIO.output(Humidifer_Control, GPIO.LOW)
            if humidity > high_humid_thres:
                GPIO.output(Fan_Control, GPIO.HIGH)
                print(f"High Humidity warning {humidity}%, turning on Fan")
            else:
                GPIO.output(Fan_Control, GPIO.LOW)
        else:
            print("failed to read data from sensor")

        time.sleep(2)       
except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    GPIO.cleanup()
    
