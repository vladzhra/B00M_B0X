"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Start.py
Description : The start code, were modules are choosen, time is starting
"""

"""
/!/!/!/!/!/!/!/!/!
ATTENTION : 
VERIFIER LES PINS
SI UN PIN MODIFIER, MODIFIER LE CODE D'EXECUTION DES MODULES
/!/!/!/!/!/!/!/!/!
"""

# Librairies 
import RPi.GPIO as GPIO
import time
import random 

# Importation des modules
from Modules.Module_1 import module_1
from Modules.Module_2 import module_2
from Modules.Module_3 import module_3
from Modules.Module_4 import module_4
from Modules.Module_5 import module_5

# Choose the modules
def Modules_Choice():

	LedPin1 = 29
	LedPin2 = 31
	LedPin3 = 33
	LedPin4 = 35
	LedPin5 = 37

	GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
	GPIO.setup((LedPin1,LedPin2,LedPin3,LedPin4,LedPin5), GPIO.OUT)   # Set pin mode as output
	GPIO.output((LedPin1,LedPin2,LedPin3,LedPin4,LedPin5), GPIO.HIGH) # Set pin to high(+3.3V) to off the led

	led_pins = [LedPin1,LedPin2,LedPin3,LedPin4,LedPin5]

	GPIO.output(led_pins, GPIO.LOW) # Leds ON
	for i in range (2):
		pins_choice = random.choice(led_pins)	# Choice one pin
		GPIO.output(pins_choice, GPIO.HIGH)  # Turn this pin OFF
		led_pins.remove(pins_choice)	# Remove pin

	print(led_pins)

	for index in range(29, 39, 2):
		if led_pins.count(index) != 0:	# Test if the module is choosen
			if index == 29:
				module_1()
			elif index == 31:
				module_2()
			elif index == 33:
				module_3()
			elif index == 35:
				module_4()
			elif index == 37:
				module_5()


Modules_Choice()