"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Modules/Passives/buzzer.py
Description : The buzer module code

Module : Buzer
    Objective : Set a buzer every second / we'll use it for the morse module
"""
-


import RPi.GPIO as GPIO
import time
import board
import busio
import digitalio
from adafruit_mcp230xx.mcp23017 import MCP23017

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c, address=0x27)
BZRPin = mcp.get_pin(15)
BZRPin.switch_to_output(value=True)

# GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
# GPIO.setup(SonPin, GPIO.OUT)   # Set pin mode as output
# GPIO.output(SonPin, GPIO.LOW)
try:
    while True:
        # Blink pin 0 on and then off.
        BZRPin.value = True
        time.sleep(0.5)
        print("Pin 0 is at a high level: {0}".format(BZRPin.value))
        BZRPin.value = False
        time.sleep(0.5)
        # Read pin 1 and print its state.
        print("Pin 0 is at a high level: {0}".format(BZRPin.value))




# p = GPIO.PWM(SonPin, 100000) # init frequency: 50HZ

def sonCompteur():

    for i in range (10):
        p.ChangeFrequency(900) # init frequency: 50HZ
        p.start(10)
        time.sleep(0.2)
        p.stop()
        time.sleep(1)
    p.stop()

def sonErreur():
    for i in range (3):
        p.ChangeFrequency(50) # frequency: 50HZ
        p.start(10) # Duty cycle: 50%
        time.sleep(0.1)
        p.stop()
        time.sleep(0.1)
    p.stop()

def sonExplosion():
    for freq in range (8000, 100, -200):
        p.start(10) # Duty cycle: 50%
        p.ChangeFrequency(freq) # frequency: 50HZ
        time.sleep(0.05)
    p.stop()

def sonFinModule():
    for freq in range (100, 8000, 200):
        p.start(10) # Duty cycle: 50%
        p.ChangeFrequency(freq) # frequency: 50HZ
        time.sleep(0.01)
    p.stop()

def sonFinEtape():
    for i in range (2):
        p.ChangeFrequency(4000) # frequency: 50HZ
        p.start(10) # Duty cycle: 50%
        time.sleep(0.1)
        p.stop()
        time.sleep(0.1)
    p.stop()


