from gpiozero import OutputDevice
from time import sleep

pin1 = 17

relay1 = OutputDevice(pin1,active_high=True, initial_value=True)
try:
    while True:
        relay1.on()
        sleep(2)
        relay1.off()
        sleep(2)
except KeyboardInterrupt:
    print("Exiting Program")

finally:
    relay1.close()