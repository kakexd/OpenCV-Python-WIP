import RPi.GPIO as GPIO
import dht11
from gpiozero import Button
from gpiozero import LED
from signal import pause
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin = 14)
result = instance.read()
button = Button(2)
led = LED(3)



def tempr():

	while True:

		if result.is_valid():
			print("Temperature: %3.1f C" % result.temperature)
			print("Humidity %3.1f %%" % result.humidity)
			led.on()
			time.sleep(2)
		elif button.is_pressed:
			button.when_pressed = tempstop
			break
		else:
			print("Error: %d" % result.error_code)


def tempstop():

	print("loop will be cancelled.")


# Pressing a button runs temperature infinity
button.when_pressed = tempr
pause()
