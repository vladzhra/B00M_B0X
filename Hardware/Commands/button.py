"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00M_B0X/Hardware/Commands/button.py
Description : python file for all buttons in project

Module : 
    Objective : The objective is to have an only one file for all buttons (with parameters)
    Malus : 
"""
from Hardware.Commands.commandBase import *
import RPi.GPIO as GPIO  
import time
import random

class ButtonBaseClass(CommandBase):
   
    def setup(self):
        print("LOG ButtonBaseClass: setup")
        return None



class Button(ButtonBaseClass):
    # CONSTANTS   

    def __init__(self, buttonPin):
        self.buttonPin = buttonPin 
        GPIO.setmode(GPIO.BOARD)

    def setup(self):
        GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
        GPIO.setup(self.buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set buttonPin to PULL UP INPUT mode
        print("Button {} is pressed".format(self.buttonPin))

    def isPressed(self):
        if GPIO.input(self.buttonPin)==GPIO.LOW:
            return True
        else:
            return False
         
    def destroy(self):
        GPIO.cleanup()


class ButtonMock(ButtonBaseClass):

    def setup(self):
        print("LOG ButtonMock: setup")
        return None





class RedButton():

    pin = 19
    
    def __init__(self):
        myButton = Button(self.pin)

    def isPressed(self):
        return self.myButton.isPressed() #n'a rien a voir avec la fonction une ligne au dessus!


class BlueButton():

    pin = 21
    
    def __init__(self):
        myButton = Button(self.pin)

    def isPressed(self):
        return self.myButton.isPressed() #n'a rien a voir avec la fonction une ligne au dessus!



class WhiteButton():

    pin = 23
    
    def __init__(self):
        myButton = Button(self.pin)

    def isPressed(self):
        return self.myButton.isPressed() #n'a rien a voir avec la fonction une ligne au dessus!


class PurpleButton():

    pin = 24
    
    def __init__(self):
        myButton = Button(self.pin)

    def isPressed(self):
        return self.myButton.isPressed() #n'a rien a voir avec la fonction une ligne au dessus!



 





