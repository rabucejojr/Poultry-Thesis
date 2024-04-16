import RPi.GPIO as GPIO
import time

servoPIN = 37
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
p.start(2.5)  # Initialization
try:
    while True:
        p.ChangeDutyCycle(0)
        time.sleep(2)
        p.ChangeDutyCycle(12.5)
        time.sleep(2)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
