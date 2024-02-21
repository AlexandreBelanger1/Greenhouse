import subprocess
import time

def capture_image(filename):
    command = f"libcamera-still -o {filename}"
    subprocess.run(command, shell = True, check = True)

image_file = "/home/mosaovirkhan/captured_image.jpg"
capture_image(image_file)
