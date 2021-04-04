#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import random

LedPin = 11,13,15,16    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led

def loop():
	compteur = 1
	while True:
		
		print("Led au pif ! numero : {}".format(compteur))
		GPIO.output(random.choice([11, 13, 15, 16]), GPIO.LOW)  # led on
		time.sleep(0.5)

		GPIO.output(11, GPIO.HIGH) # led off
		GPIO.output(13, GPIO.HIGH)
		GPIO.output(15, GPIO.HIGH)
		GPIO.output(16, GPIO.HIGH)
		time.sleep(0.5)
		compteur = compteur +1
'''
		print '...led on'
		GPIO.output(13, GPIO.LOW)  # led on
		time.sleep(0.2)
		print 'led off...'
		GPIO.output(13, GPIO.HIGH) # led off
		time.sleep(0.2)

		print '...led on'
		GPIO.output(15, GPIO.LOW)  # led on
		time.sleep(0.2)
		print 'led off...'
		GPIO.output(15, GPIO.HIGH) # led off
		time.sleep(0.2)

		print '...led on'
		GPIO.output(16, GPIO.LOW)  # led on
		time.sleep(0.2)
		print 'led off...'
		GPIO.output(16, GPIO.HIGH) # led off
		time.sleep(0.2)
'''

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

