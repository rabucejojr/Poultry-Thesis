import RPi.GPIO as GPIO
import time

IR_PIN = 17
motion_count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(IR_PIN):
            motion_count += 1
            print("Motion detected! Count:", motion_count)
        else:
            print("No motion detected.")
        time.sleep(0.1)  # Adjust as needed
except KeyboardInterrupt:
    GPIO.cleanup()
