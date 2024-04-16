from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=6, trigger=5)
while True:
    print(ultrasonic.distance)   