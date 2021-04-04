#!/usr/bin/env python
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
