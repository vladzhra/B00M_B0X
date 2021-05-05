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

BZRPin = 12

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(BZRPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(BZRPin, GPIO.LOW)

p = GPIO.PWM(BZRPin, 70) # init frequency: 50HZ
# Duty cycle: 50%
print("let's go")



def minuteur():
    for i in range (10):
        p.start(100)
        time.sleep(0.5)
        p.stop()
        time.sleep(0.5)

def erreur():
    for i in range (6):
        p.start(100)
        time.sleep(0.1)
        p.stop()
        time.sleep(0.1)

start()

