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

SonPin = 12

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(SonPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(SonPin, GPIO.LOW)

p = GPIO.PWM(SonPin, 100000) # init frequency: 50HZ

def count():

    for i in range (10):
        p.ChangeFrequency(900) # init frequency: 50HZ
        p.start(10)
        time.sleep(0.2)
        p.stop()
        time.sleep(1)

def erreur():
    for i in range (3):
        p.ChangeFrequency(50) # frequency: 50HZ
        p.start(10) # Duty cycle: 50%
        time.sleep(0.1)
        p.stop()
        time.sleep(0.1)

try:
    while True:
        print("Rien à éxecuter ici")
        time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
