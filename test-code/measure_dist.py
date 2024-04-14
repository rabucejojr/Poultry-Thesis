from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(5, 6)

distance_cm = sensor.distance * 100

while True:
    print('Distance to nearest object is', distance_cm, 'cm')
    sleep(1)