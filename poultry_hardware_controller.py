import requests
import Adafruit_DHT
from time import sleep
import math
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
from gpiozero import OutputDevice

# ADC Configuration
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

# MQ Sensor Constants
RL = 47  # The value of resistor RL is 47K
m = -0.263  # Enter calculated Slope
b = 0.42  # Enter calculated intercept
Ro = 496.0725684427985  # Enter found Ro value
MQ_sensor = 0  # Sensor is connected to A0 on ADS1115

# DHT22 Pin Configuration
sensor = Adafruit_DHT.DHT22
# sensor = Adafruit_DHT.DHT11
pin = 27


# Servo Pin Configurations
GPIO.setmode(GPIO.BCM)
servo_pin = 5
GPIO.setup(servo_pin, GPIO.OUT)
# Create a PWM object at 50Hz (20ms period)
pwm = GPIO.PWM(servo_pin, 50)

#Servo to trigger fan for ventilation
# Relay Pin Configurations
pin= 17
relay= OutputDevice(pin1,active_high=False, initial_value=False)

# API URL FOR BACKEND POST
api_temp = "https://poultry-backend.vercel.app/api/temperature"
api_humidity = "https://poultry-backend.vercel.app/api/humidity"
api_nh3 = "https://poultry-backend.vercel.app/api/ammonia"


def dht22():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temperature = temperature * (9 / 5) + 32
    # Convert values to float
    temperature = float(temperature)
    humidity = float(humidity)
    return temperature, humidity


def mq137(VRL):
    Rs = ((5.0 * RL) / VRL) - RL  # Calculate Rs value
    ratio = Rs / Ro  # Calculate ratio Rs/Ro
    ppm = pow(10, ((math.log10(ratio) - b) / m))  # Calculate ppm
    return ppm


def set_angle(angle,delayOpen,delayClose):
    duty = (angle / 18) + 2.5
    # open to x degrees
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
<<<<<<< HEAD
    sleep(3)
    # close valve
=======
    time.sleep(delayOpen)
    # open to x degrees
>>>>>>> 1ed3cc5ea943a5c6ec23389f68e7728b7bf90784
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)
    time.sleep(delayClose)

    

def fan_exhaust(delay):  # execute relays activate water pump ot water foucets
    relay.on()
    sleep(delay)
    relay.off()
    sleep(delay)

def post_data(api, data, label):
    json_data = {"value": data}
    response = requests.post(api, json=json_data)
    if response.status_code == 201:
        print(label, "data sent successfully")
    else:
        print("Failed to send data to API:", response.text)


# Main Loop Execution
def main():
    while True:
        temperature, humidity = dht22()
        value = adc.read_adc(MQ_sensor, gain=GAIN)  # MQ137 adc reading
        VRL = value * (5.0 / 32767.0)
        ammonia = mq137(VRL)
        if temperature is not None and humidity is not None:
            print("Temperature:", temperature)
            print("Humidity:", humidity)
            print("Ammonia:", round(ammonia, 2))
            # Post sensor readin to api
            post_data(api_temp, temperature, "Temperature")
            post_data(api_humidity, humidity, "Humidity")
            post_data(api_nh3, ammonia, "Ammonia")
            print("-" * 20)
<<<<<<< HEAD
            if temperature >= 32:
                fan_exhaust(delay)
            sleep(30
                
=======
            
            #autofeeder adjustments
            if temperature >=26:
                set_angle(90,2,2) # opens 90 degrees, opens 2 secs, closes after 2 secs
            
            time.sleep(300)  # Reread after 5 minutes
            # Other IoT code goes here ..
            # if sensor reading are above set threshhold
            # autofeeder is executed
            # egg counter/detection is always activate
            # even if threshhold aren't met
            # to track egg count
>>>>>>> 1ed3cc5ea943a5c6ec23389f68e7728b7bf90784


if __name__ == "__main__":
    main()
