"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Module_1.py
Description : The first module code

Module : Matrix keyboard 
    Objective : Write the correct password
    Malus : - 10 seconds
"""
import RPi.GPIO as GPIO  
import time  
import random
from Passives.lcd import *


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


def mdp():
    code = []
    for i in range(5):
        code.append(random.randint(1,9))
    print(code)
    return code

def affichage(code, etape):
    # Chiffre en fonction de leurs position
    lcd.display()
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns
    lcd.setCursor(11,0)
    lcd.message("*oooo")

    etape1 = {1:3, 2:1, 3:7, 4:9, 5:6, 6:5, 7:2, 8:4, 9:8}
    etape2 = {1:4, 2:etape1.get(code[0]), 3:1, 4:8, 5:7, 6:9, 7:etape1.get(code[0]), 8:etape1.get(code[0]), 9:5}
    
    """
    etape3 = {1:9, 2:etape2.get(code[1]), 3:5, 4:8, 5:2, 6:etape1.get(code[0]), 7:6, 8:1, 9:etape2.get(code[1])}
    etape4 = {1:6, 2:etape2.get(code[1]), 3:etape1.get(code[0]), 4:etape1.get(code[0]), 5:etape3.get(code[2]), 6:8, 7:etape2.get(code[1]), 8:etape3.get(code[2]), 9:4}
    etape5 = {1:etape3.get(code[2]), 2:etape1.get(code[0]), 3:etape2.get(code[1]), 4:etape4.get(code[3]), 5:etape1.get(code[0]), 6:etape3.get(code[2]), 7:etape4.get(code[3]), 8:etape2.get(code[1]), 9:etape1.get(code[0])}
    """
    # Etape 1
    if etape == 1:
        
        lcd.setCursor(6,0)
        lcd.message("[" + str(etape1.get(code[0])) + "]")
        print(etape1.get(code[0]))
    
    # Etape 2
    if etape == 2:
        lcd.setCursor(11,0)
        lcd.message("**ooo")
        print(etape2.get(code[1]))
    
    # Etape 3
    if etape == 3:
        lcd.setCursor(11,0)
        lcd.message("***oo")
        print(etape3.get(code[2]))
    
    # Etape 4
    if etape == 4:
        lcd.setCursor(11,0)
        lcd.message("****o")
        print(etape4.get(code[3]))
    
    # Etape 5
    if etape == 5:
        lcd.setCursor(11,0)
        lcd.message("*****")
        print(etape5.get(code[4]))
        

def module_1():
    print("Lancement du module 1 ...")    
    code = mdp()
    etape = 1
    # Initialize the keypad class
    kp = keypad()
    # Loop while waiting for a keypress

    while len(code) != 0:
        time.sleep(1)
        digit = None
        # Execute a chaque fois
        affichage(code, etape)
        while digit == None:
            digit = kp.getKey()
        # Quand j'appuis
        if digit == code[0]:
            lcd.setCursor(6,1)
            print("Good etape suivante")
            etape +=1
            lcd.message("Good")
        else:
            print("code faux")
       
    print("Module validé")

if __name__ == '__main__': 
    try:
        module_1()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be  executed.
        GPIO.cleanup()                     # Release resource
        lcd.clear()
        lcd.noDisplay()



