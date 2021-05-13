"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Modules/Module_4.py
Description : 

Module : 
    Objective :
    Malus : 
"""

import RPi.GPIO as GPIO
import time
import random

pins = [11, 12, 13]     # define the pins for R:11,G:12,B:13 
buttonPin = 19  # define buttonPin

def setup():
    global pwmRed,pwmGreen,pwmBlue  
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(pins, GPIO.OUT)     # set RGBLED pins to OUTPUT mode
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set buttonPin to PULL UP INPUT mode
    GPIO.output(pins, GPIO.HIGH)   # make RGBLED pins output HIGH level
    pwmRed = GPIO.PWM(pins[0], 2000)      # set PWM Frequence to 2kHz
    pwmGreen = GPIO.PWM(pins[1], 2000)  # set PWM Frequence to 2kHz
    pwmBlue = GPIO.PWM(pins[2], 2000)    # set PWM Frequence to 2kHz
    pwmRed.start(0)      # set initial Duty Cycle to 0
    pwmGreen.start(0)
    pwmBlue.start(0)

def setColor(r_val,g_val,b_val):      # change duty cycle for three pins to r_val,g_val,b_val
    pwmRed.ChangeDutyCycle(r_val)     # change pwmRed duty cycle to r_val
    pwmGreen.ChangeDutyCycle(g_val)   
    pwmBlue.ChangeDutyCycle(b_val)
        
def destroy():
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    GPIO.cleanup()

def blanc():
    setColor(50, 50, 50)
def noir():
    setColor(100, 100, 100)
def rouge():
    setColor(0, 100, 100)
def vert():
    setColor(100, 0, 100)
def bleu():
    setColor(100, 100, 0)
def violet():
    setColor(80, 100, 0)
def rose():
    setColor(0, 100, 90)
def cyan():
    setColor(100, 10, 10)
def orange():
    setColor(0, 95, 100)



def module_4():

    print("Lancement du module 4 ...")
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW: # if button is pressed
            if buttonPin == 13:
                return Bleu
            
            print("Button is pressed")
            blanc()
            time.sleep(0.1)
            rouge()
            time.sleep(0.1)
            vert()
            time.sleep(0.1)
            bleu()
            time.sleep(0.1)
            cyan()
            time.sleep(0.1)
            orange()
            time.sleep(0.1)
            rose()
            time.sleep(0.1)
            violet()
            time.sleep(0.1)             

        else : # if button is relessed
            noir()






if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        module_4()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()



