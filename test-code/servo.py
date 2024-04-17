import RPi.GPIO as GPIO
import time

servoPIN = 37
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
p.start(2.5)  # Initialization
start = True  #set loop status to true to execute while loop
try:
    while start:
        p.ChangeDutyCycle(5)
        time.sleep(4) # 4 seconds delay after open
        p.ChangeDutyCycle(12.5)
    start = False  # set start status to false to break while loop

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
