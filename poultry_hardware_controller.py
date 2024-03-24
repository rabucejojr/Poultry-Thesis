import requests
import Adafruit_DHT
import time
import math
import Adafruit_ADS1x15
import RPi.GPIO as GPIO

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
servo_pin = 17
GPIO.setup(servo_pin, GPIO.OUT)
# Create a PWM object at 50Hz (20ms period)
pwm = GPIO.PWM(servo_pin, 50)

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

def set_angle(angle):
    duty = angle / 18 + 2
    # open valve
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(3)
    # close valve
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

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
        value = adc.read_adc(MQ_sensor, gain=GAIN) # MQ137 adc reading
        VRL = value * (5.0 / 32767.0)
        ammonia = mq137(VRL) 
        if temperature is not None and humidity is not None:
            print("Temperature:", temperature)
            print("Humidity:", humidity)
            print("Ammonia:", round(ammonia,2))
            # Post sensor readin to api
            post_data(api_temp, temperature, "Temperature")
            post_data(api_humidity, humidity, "Humidity")
            post_data(api_nh3, ammonia, "Ammonia")
            print('-'* 20)
            time.sleep(300) # Reread after 5 minutes
            # Other IoT code goes here ..


if __name__ == "__main__":
    main()
