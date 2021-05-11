"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Modules/Passives/ledbar.py
Description : The led bar module code

Module : Led Bar
    Objective : Randomly turn on one of the 5 leds
  
"""
class ledbar():

	LedPin1 = 29
	LedPin2 = 31
	LedPin3 = 33
	LedPin4 = 35
	LedPin5 = 37
	def __init__(self):

		GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
		GPIO.setup((LedPin1,LedPin2,LedPin3,LedPin4,LedPin5), GPIO.OUT)   # Set pin mode as output
		GPIO.output((LedPin1,LedPin2,LedPin3,LedPin4,LedPin5), GPIO.HIGH) # Set pin to high(+3.3V) to off the led

		led_pins = [LedPin1,LedPin2,LedPin3,LedPin4,LedPin5]

		GPIO.output(led_pins, GPIO.LOW) # Leds ON

	def start(self):

		for i in range (2):
			pins_choice = random.choice(led_pins)	# Choice one pin
			GPIO.output(pins_choice, GPIO.HIGH)  # Turn this pin OFF
			led_pins.remove(pins_choice)	# Remove pin

		print(led_pins)