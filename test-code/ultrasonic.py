import RPi.GPIO as GPIO
import time

# Define GPIO pins for ultrasonic sensor
TRIG_PIN = 29
ECHO_PIN = 31

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def distance():
    # Trigger ultrasonic sensor
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Measure time for echo
    start_time = time.time()
    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()

    end_time = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        end_time = time.time()

    # Calculate distance in cm
    duration = end_time - start_time
    # 34300 represents the speed of sound in centimeters per second
    # dividing the total distance by 2 gives us the distance from the sensor to the object in centimeters
    distance_cm = (duration * 34300) / 2 
    return distance_cm

def count_eggs():
    # Initialize egg count
    egg_count = 0

    try:
        while True:
            # Measure distance
            dist = distance()

            # Assuming egg height is around 5 cm, adjust as needed
            if dist < 5:
                egg_count += 1
                print("Egg detected! Total eggs:", egg_count)
                
                # Optional delay to avoid multiple counts of the same egg
                time.sleep(1)

    except KeyboardInterrupt:
        print("\nProgram stopped by the user")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    count_eggs()
