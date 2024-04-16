# Code to be executed via CRON
# Dedicated for Servo and Stepper Motor Only
# reference: https://danielwilczak101.medium.com/control-a-stepper-motor-using-python-and-a-raspberry-pi-11f67d5a8d6d

# crontab for scheduled feeder
# crontab for 8AM activation: 0 8 * * * python3 /home/admin/Desktop/Poultry-Thesis/auto-feeder.py
# crontab for 1PM activation: 0 13 * * * python3 /home/admin/Desktop/Poultry-Thesis/auto-feeder.py

# crontab for main controller to read and submit data to api and will run every boot
# @reboot python3 /home/admin/Desktop/thesis_v1/piggery_hardware_controller.py

import RPi.GPIO as GPIO
from time import sleep

# Direction pin from controller
DIR = 10
# Step pin from controller
STEP = 8
# 0/1 used to signify clockwise or counterclockwise.
CW = 1
CCW = 0
servoPIN = 29 # pin sequence number 29 as per datasheet pinout
# Setup pin layout on PI
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Establish Pins in software
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)  # pin sequence no. 37 for PWM with 50Hz
p.start(0)  					# Initialization

# Function to convert angle to duty cycle
def angle_to_duty_cycle(angle):
    duty_cycle = (angle / 18) + 2.5
    return duty_cycle
 
# Set the first direction you want it to spin
GPIO.output(DIR, CW)

stepper_status = True

while stepper_status:
	try:
		# SERVO
		#open 0 degrees
		duty_cycle = angle_to_duty_cycle(0)
		p.ChangeDutyCycle(duty_cycle)
		sleep(4)
		#open 90 degrees
		duty_cycle = angle_to_duty_cycle(90)
		p.ChangeDutyCycle(duty_cycle)
		sleep(4)

		"""Change Direction: Changing direction requires time to switch. The
		time is dictated by the stepper motor and controller. """
		GPIO.output(DIR,CW) # counterclockwise direction
		# Run for 1000 steps. This will change based on how you set you controller
		for x in range(1000):
			GPIO.output(STEP,GPIO.HIGH) # Set one coil winding to high
			sleep(0.0000001) # Dictates how fast stepper motor will run
			GPIO.output(STEP,GPIO.LOW) # Set coil winding to low
			sleep(0.0000001) # Dictates how fast stepper motor will run 
		# stepper_status = False
	# Stop stepper motor
	except KeyboardInterrupt:
		p.stop() #stop servo
		GPIO.cleanup()

