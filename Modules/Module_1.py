"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Modules/Module_1.py
Description : The first module code

Module : Matrix keyboard 
    Objective : Write the correct password
    Malus : - 10 seconds
"""
import RPi.GPIO as GPIO  
import time  
import random
from Passives.lcd import *
from Passives.erreur import Error

Erreurs = Error()
etape = 1

class keypad():
    # CONSTANTS   
    KEYPAD = [
    [1,2,3,"A"],
    [4,5,6,"B"],
    [7,8,9,"C"],
    ["*",0,"#","D"]
    ]
     
    ROW = [11,12,13,15]
    COLUMN = [16,18,22,7]
     
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

    def getKey(self):
         
        # Set all columns as output low
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)
         
        # Set all rows as input
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
         
        # Scan rows for pushed key/button
        # A valid key press should set "rowVal"  between 0 and 3.
        rowVal = -1
        for i in range(len(self.ROW)):
            tmpRead = GPIO.input(self.ROW[i])
            if tmpRead == 0:
                rowVal = i
                 
        # if rowVal is not 0 thru 3 then no button was pressed and we can exit
        if rowVal < 0 or rowVal > 3:
            self.exit()
            return
         
        # Convert columns to input
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
         
        # Switch the i-th row found from scan to output
        GPIO.setup(self.ROW[rowVal], GPIO.OUT)
        GPIO.output(self.ROW[rowVal], GPIO.HIGH)
 
        # Scan columns for still-pushed key/button
        # A valid key press should set "colVal"  between 0 and 2.
        colVal = -1
        for j in range(len(self.COLUMN)):
            tmpRead = GPIO.input(self.COLUMN[j])
            if tmpRead == 1:
                colVal=j
                 
        # if colVal is not 0 thru 2 then no button was pressed and we can exit
        if colVal < 0 or colVal > 3:
            self.exit()
            return
 
        # Return the value of the key pressed
        self.exit()
        return self.KEYPAD[rowVal][colVal]
         
    def exit(self):
        # Reinitialize all rows and columns as input at exit
        for i in range(len(self.ROW)):
                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)

class Module1():
    """
    init : object = mot("") # Nothing into ""
    """

    def __init__(self, input):

        self.input = input
        self.MultiTap = {"A":x.accept(), "C":x.cancel(), "D":x.delete(), "0":" ", "8":"A", "88":"B", "888":"C", "1":"D", "11":"E", "6":"F", "66":"G", "666":"H",
                        "3":"I", "33":"J", "7":"K", "77":"L", "#":"M", "##":"N", "###":"O", "9":"P", "99":"Q", "4":"R", "44":"S", "*":"T", "**":"U", "***":"V", 
                        "5":"W", "55":"X", "2":"Y", "22":"Z"}
        self.lettre = ""
        self.motFinal = ""
        self.index = 0
        self.conversion()

    def __str__(self, mot):
        lcd.setCursor(0,0)
        lcd.message(mot)
        print(mot)       

    def accept(self):
        print("Accpet")

    def cancel(self):
        print("Cancel")

    def delete(self):
        print("Delete")

    def conversion(self):

        if len(self.lettre) == 0:
            self.lettre += self.input
            lcd.setCursor(self.index,1)
            lcd.message(self.MultiTap.get(self.lettre))
            print(self.lettre)

        elif len(self.lettre) == 1:
            print("coucou")
            if self.lettre[0] == self.input:
                self.lettre += self.input
                lcd.setCursor(self.index,1)
                lcd.message(self.lettre)
                
            else:
                self.index += 1
                self.motFinal += self.MultiTap.get(lettre)
                self.lettre.clear()
                self.lettre += self.input
                lcd.setCursor(self.index,1)
                lcd.message(self.MultiTap.get(self.input))
            
                
    """
        elif len(lettre) == 2:
            if lettre[0] == nb:
                lettre += nb
            else:
                lcd.setCursor(index,1)
                lcd.message(MultiTap.get(nb))
                motFinal = motFinal + MultiTap.get(lettre)
                index += 1
                lettre.clear()
                lettre += nb

        elif len(lettre) >= 3:
                lcd.setCursor(index,1)
                lcd.message(MultiTap.get(nb))
                motFinal = motFinal + MultiTap.get(lettre)
                index += 1
                lettre.clear()
                lettre += nb
    """

    def verifierMot(self):
        if code == motFinal:
            etape += 1
            choixMot()





# Mot Court < 7 
# 7 < Mot Normal < 11
# Mot long > 11
        
def choixMot():        
        motsCourt = ["FLUX", "LINUX", "HTML", "LOG", "WI FI", "LIEN", "INTEL", "OCTET", "VIRUS", "PYTHON"]
        motsNormaux = ["LOGICIEL", "CONSOLE", "ORDINATEUR", "HACKEUR", "PIRATAGE", "INTERNET", "RESEAUX", "STOCKAGE", "ROUTEUR", "PARE FEU"]    
        motsLongs = ["CRYPTOLOGIE", "APPLICATION", "DEVELOPPEUR", "DEVELOPPEMENT", "CARTE GRAPHIQUE", "GABY ET VLADOU", "MICRO ORDINATEUR", "INTERFACE RESEAU"]

        mot = ""

        if etape == 1:
            mot = motsCourt[random.randint(0, len(motsCourt)-1)]
        elif etape == 2:
            mot = motsNormaux[random.randint(0, len(motsCourt)-1)]
        elif etape == 3:
            mot = motsLongs[random.randint(0, len(motsCourt)-1)]




def module_1():
    print("Lancement du module 1 ...")    
    # Initialize the keypad class
    kp = keypad()
    choixMot()
    # Loop while waiting for a keypress
    while etape != 4:
        digit = None
        while digit == None:
            digit = kp.getKey()   
        # Print the result
        x = Module1(digit)

        traduction(str(digit), lettre, index)
        time.sleep(0.3)

    else:
        print("Module reussi")

    # Loop while waiting for a keypress
   



if __name__ == '__main__': 
    try:
        mcp.output(3,1)     # turn on LCD backlight
        lcd.begin(16,2)     # set number of LCD lines and columns
        module_1()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be  executed.
        GPIO.cleanup()                     # Release resource
        lcd.clear()
        lcd.noDisplay()


