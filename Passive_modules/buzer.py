"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/buzer.py
Description : The buzer module code

Module : Buzer
    Objective : Set a buzer every second / we'll use it for the morse module
"""


import RPi.GPIO as GPIO
import time

BZRPin = 32

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(BZRPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(BZRPin, GPIO.LOW)

p = GPIO.PWM(BZRPin, 500) # init frequency: 50HZ
p.start(50)  # Duty cycle: 50%

try:
	while True:
        
		print '...led on'
		p.start(50)
		time.sleep(1)
		print 'led off...'
		p.stop()
		time.sleep(1)
        
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
