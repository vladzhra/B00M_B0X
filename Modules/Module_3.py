"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Modules/Modules_3.py
Description : Buzer's code

Module : Morse
    Objective : Set a buzer to use it for the morse module
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

def point() :  #Son court
            p.start(100)
            time.sleep(0.5)
            p.stop()
            time.sleep(0.5)

def tiret() :   #Son long
    p.start(100)
    time.sleep(1)
    p.stop()
    time.sleep(0.5)

def espace(): 
    p.stop()
    time.sleep(2.5)

def A() :

    point()
    tiret()

def B() :
    
    tiret()
    point()
    point()

def C() :
    
    tiret()
    point()
    tiret()
    point()

def D() :
    
    tiret()
    point()
    point()

def zero() :

    tiret()
    tiret()
    tiret()
    tiret()
    tiret()

def un() :

    point()
    tiret()
    tiret()
    tiret()
    tiret()

def deux() :

    point()
    point()
    tiret()
    tiret()
    tiret()

def trois() :

    point()
    point()
    point()
    tiret()
    tiret()

def quatre() :

    point()
    point()
    point()
    point()
    tiret()

def cinq() :

    point()
    point()
    point()
    point()
    point()

def six() :

    tiret()
    point()
    point()
    point()
    point()

def sept() :

    tiret()
    tiret()
    point()
    point()
    point()

def huit() :

    tiret()
    tiret()
    tiret()
    point()
    point()

def neuf() :

    tiret()
    tiret()
    tiret()
    tiret()
    tiret()
    point()

def Diez() : 

    tiret()
    tiret()
    point()
    point()

def Etoile() :

    tiret()
    point()
    tiret()
    tiret()

try:
    while True:
        
        cinq()
        espace()
        C()
        espace()
        neuf()




except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
