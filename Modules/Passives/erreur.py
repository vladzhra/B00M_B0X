"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Modules/Passives/erreur.py
Description : Mistakes's code

Module : Aucun
    Objective : Code to work mistakes
"""

from lcd import *
from buzzer import *

class Error: 
    """
    Class Error :

    Methode :
    """

    def __init__(self, nbError):

        self.nbError = nbError

    def clear(self):
        lcd.clear()
        lcd.noDisplay()

    def boom(self):
        for i in range(5):
            lcd.noDisplay()
            time.sleep(0.5)
            lcd.display()

    def __str__(self):
        lcd.display()
        mcp.output(3,1)     # turn on LCD backlight
        lcd.begin(16,2)     # set number of LCD lines and columns
        lcd.setCursor(0, 0)
        if self.nbError == 0: 
            lcd.message("[  ]")
        elif self.nbError == 1: 
            lcd.message("[X ]")
        elif self.nbError == 2: 
            lcd.message("[XX]")
        else:
            lcd.message("BOOM")
        

    def __add__(self):
        if self.nbError < 3 : 
            self.nbError += 1
            self.__str__()
            sonErreur()
        else:
            boom()



Erreurs = Error(0)

Erreurs.__str__()
time.sleep(1)
Erreurs.__add__()
time.sleep(1)
Erreurs.__add__()
time.sleep(1)
Erreurs.__add__()

time.sleep(3)
Erreurs.clear()