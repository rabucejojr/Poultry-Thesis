# Code to be executed via CRON
# Dedicated for Servo and Stepper Motor Only
# reference: https://danielwilczak101.medium.com/control-a-stepper-motor-using-python-and-a-raspberry-pi-11f67d5a8d6d
import RPi.GPIO as GPIO
from time import sleep

# Direction pin from controller
DIR = 10
# Step pin from controller
STEP = 8
# 0/1 used to signify clockwise or counterclockwise.
CW = 1
CCW = 0
servoPIN = 17
# Setup pin layout on PI
GPIO.setmode(GPIO.BOARD)

# Establish Pins in software
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
# GPIO.setup(servoPIN, GPIO.OUT)
# p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
# p.start(2.5)  					# Initialization

# Set the first direction you want it to spin
GPIO.output(DIR, CW)
try:
	# Run forever.
	while True:
# 		# SERVO
# 		p.ChangeDutyCycle(5)
# 		sleep(3)
# 		p.ChangeDutyCycle(12.5)
# 		sleep(3)
		"""Change Direction: Changing direction requires time to switch. The
		time is dictated by the stepper motor and controller. """
		sleep(1.0)
		# Esablish the direction you want to go
		GPIO.output(DIR,CW)

		# Run for 200 steps. This will change based on how you set you controller
		for x in range(200):

			# Set one coil winding to high
			GPIO.output(STEP,GPIO.HIGH)
			# Allow it to get there.
			sleep(.005) # Dictates how fast stepper motor will run
			# Set coil winding to low
			GPIO.output(STEP,GPIO.LOW)
			sleep(.005) # Dictates how fast stepper motor will run

		# """Change Direction: Changing direction requires time to switch. The
		# time is dictated by the stepper motor and controller. """
		# sleep(1.0)
		# GPIO.output(DIR,CCW)
		# for x in range(200):
		# 	GPIO.output(STEP,GPIO.HIGH)
		# 	sleep(.005)
		# 	GPIO.output(STEP,GPIO.LOW)
		# 	sleep(.005)

# Once finished clean everything up
except KeyboardInterrupt:
   p.stop() #stop servo
   GPIO.cleanup()