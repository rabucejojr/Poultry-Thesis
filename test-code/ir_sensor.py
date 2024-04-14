import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the IR sensor
IR_PIN = 17

# Set up the GPIO pin as input
GPIO.setup(IR_PIN, GPIO.IN)

try:
    while True:
        # Read the state of the IR sensor
        ir_state = GPIO.input(IR_PIN)

        if ir_state == True:
            print("Object detected")
        else:
            print("No object detected")

        # Add a small delay to avoid spamming the console
        time.sleep(3)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
