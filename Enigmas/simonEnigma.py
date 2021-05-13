"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Modules/Module_2.py
Description : 

Module : 
    Objective : 
    Hardware necessaire : buzer, lcd & keypad
"""

from Enigmas.enigmaBase import *
from Hardware.Commands.keypad import *
from Hardware.Commands.button import *
from Hardware.Displays.lcd import *
from Core.error import *
import random
import time

class PasswordDecoderEnigma(EnigmaBase):
    
    
    etape = 1
    listeTouches = []
    indexLettre = 0
    MultiTap = {"A":"accept()", "C":"cancel()", "D":"", # A changer
            "0":"_",
            "8":"A", "88":"B", "888":"C", "1":"D", "11":"E", "6":"F", "66":"G", "666":"H", "3":"I", "33":"J", "7":"K", "77":"L", "#":"M", "##":"N", "###":"O", "9":"P", "99":"Q", "4":"R", "44":"S", "*":"T", "**":"U", "***":"V", "5":"W", "55":"X", "2":"Y", "22":"Z"}



    def __init__(self, kp:KeypadBaseClass, lcd:LcdBaseClass, er:Error):
        self.kp = kp
        self.lcd = lcd
        self.er = er
 
        

    def resolveEnigma(self):
        """
        Code principal de l'enigme 
        """
        return True




    def accept(self,mdp):
        """
        Code executer lorsque l'utilisateur rentre la combinaison de chiffre et appuis sur A
        """
        verification = self.conversion()
        if verification == mdp[self.indexLettre]:
            print("Lettre validé")
            self.lcd.setCursor(self.indexLettre, 1)
            self.lcd.message(verification)
            self.indexLettre += 1
            self.listeTouches.clear()
            return True
        else: # Erreur
            self.er.__add__()
            self.listeTouches.clear()
            self.lcd.setCursor(self.indexLettre, 1)
            self.lcd.message("_")
            time.sleep(0.7)
            return False

    def conversion(self):
        """
        Changement des touches rentées par l'utilisateur en lettres
        """
        chiffres = ""

        if len(self.listeTouches) != 0:

            if len(self.listeTouches) <= 3:
            
                for i in range(len(self.listeTouches)):
                    chiffres += self.listeTouches[i]    
                return (self.MultiTap.get(chiffres))
        else:
            pass
