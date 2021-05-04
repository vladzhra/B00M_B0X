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
import random

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

def espace():   #Espace
    p.stop()
    time.sleep(2.5)



    


def fonction0() : #0

    tiret()
    tiret()
    tiret()
    tiret()
    tiret()
    espace()

def fonction1() : #1

    point()
    tiret()
    tiret()
    tiret()
    tiret()
    espace()

def fonction2() : #2

    point()
    point()
    tiret()
    tiret()
    tiret()
    espace()

def fonction3() : #3

    point()
    point()
    point()
    tiret()
    tiret()
    espace()

def fonction4() : #4

    point()
    point()
    point()
    point()
    tiret()
    espace()

def fonction5() : #5

    point()
    point()
    point()
    point()
    point()
    espace()

def fonction6() : #6

    tiret()
    point()
    point()
    point()
    point()
    espace()

def fonction7() : #7

    tiret()
    tiret()
    point()
    point()
    point()
    espace()

def fonction8() : # 8

    tiret()
    tiret()
    tiret()
    point()
    point()
    espace()

def fonction9() : #9

    tiret()
    tiret()
    tiret()
    tiret()
    tiret()
    point()
    espace()

def fonction10() :  ##

    tiret()
    tiret()
    point()
    point()
    espace()

def fonction11() : #*

    tiret()
    point()
    tiret()
    tiret()
    espace()

def fonction12() : #A

    point()
    tiret()
    espace()

def fonction13() : #B
    
    tiret()
    point()
    point()
    espace()

def fonction14() : #C
    
    tiret()
    point()
    tiret()
    point()
    espace()

def fonction15() : #D
    tiret()
    point()
    point()
    espace()


liste =[]

        
def shortpassword():

    randintvariable = random.randint(6,8)
    for i in range(randintvariable):
        n = str(random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
        liste.append(n)
        code = compile('fonction'+n+'()','toto','exec')
        eval(code)
    print(liste)    
    
def mediumpassword():

    randintvariable = random.randint(8,10)
    for i in range(randintvariable):
        n = str(random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
        liste.append(n)
        print(n)
        code = compile('fonction'+n+'()','titi','exec')
        eval(code)
    print(liste) 

def strongpassword():

    randintvariable = random.randint(10,12)
    for i in range(randintvariable):
        n = str(random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
        liste.append(n)
        code = compile('fonction'+n+'()','tutu','exec')
        eval(code)
    print(liste) 
    



espace()
# shortpassword()
# espace()
mediumpassword()
# espace()
#strongpassword())

p.stop()
GPIO.cleanup()



# try:
#     while True:
        
#         espace()
#         # shortpassword()
#         # espace()
#         mediumpassword()
#         # espace()
#         #strongpassword())

# except KeyboardInterrupt:
#     p.stop()
#     GPIO.cleanup()


