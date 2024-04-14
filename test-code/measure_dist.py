import RPi.GPIO as GPIO
import time

# Set GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set GPIO pins for trigger and echo
TRIG_PIN = 5
ECHO_PIN = 6

# Set up GPIO pins
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure_distance():
    # Ensure the trigger pin is low initially
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.1)

    # Send a 10us pulse to trigger
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)
    
    pulse_start = time.time()
    pulse_end = time.time()
    
    # Measure the pulse duration on the echo pin
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    # Speed of sound in air: 343 m/s or 34300 cm/s
    # Distance = (time taken for pulse to return * speed of sound) / 2
    distance = (pulse_duration * 34300) / 2

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = measure_distance()
            print("Distance: %.1f cm" % dist)
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()