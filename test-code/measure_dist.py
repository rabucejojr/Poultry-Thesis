from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(5, 6)

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    sleep(1)