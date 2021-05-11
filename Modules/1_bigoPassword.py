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
import random
from Hardware.display import *
from Hardware.Software.erreur import Error
from Hardware.buzzer import sonFinModule, sonFinEtape

from Passives.buzzer import sonFinEtape, sonFinModule
from Passives.erreur import Error
from Passives.lcd import *

mcp.output(3,1)     # Allume la lumiere du display
display.begin(16,2)     # Met le nombre du colonne et de ligne de l'écran
Erreurs = Error()
etape = 1
listeTouches = []
indexLettre = 0


class keypad():
    # CONSTANTS   
    KEYPAD = [
    [1,2,3,"A"],
    [4,5,6,"B"],
    [7,8,9,"C"],
    ["*",0,"#","D"]
    ]
     
    # ROW = [11,12,13,15]        #C'est tes pins gabys
    # COLUMN = [16,18,22,7]

    ROW = [18,16,15,13]      #la c'est les miens
    COLUMN = [12,10,8,7]

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

# Mot Court < 7 
# 7 < Mot Normal < 11
# Mot long > 11

def finEtape():
    global etape
    etape += 1
    if etape == 4:
        pass
    else:
        display.clear()
        display.setCursor(0, 0)
        
        for i in range(18):
            display.scrollDisplayLeft()
        display.message(" == Mot suivant == \n =-=-=-=-=-=-=-=- ")
        sonFinEtape()
        for i in range(28):      
            display.scrollDisplayRight()
            time.sleep(0.2)

    module_1()

def choixMot():
    """
    Permet de choisir le mot a deviner pour cette enigme 
    La difficulté est croissante
    """           
    mot = ""
    motsCourt = ["FLUX", "LINUX", "HTML", "LOG", "WI_FI", "LIEN", "INTEL", "OCTET", "VIRUS", "PYTHON"]
    motsNormaux = ["LOGICIEL", "CONSOLE", "ORDINATEUR", "HACKEUR", "PIRATAGE", "INTERNET", "RESEAUX", "STOCKAGE", "ROUTEUR", "PARE_FEU"]    
    motsLongs = ["CRYPTOLOGIE", "APPLICATION", "DEVELOPPEUR","GABY_ET_VLAD"]

    if etape == 1:
        mot = motsCourt[random.randint(0, len(motsCourt)-1)] # Longueur -1 car l'indexage d'une liste commence à 0
        display.setCursor(4,0)
        display.message(mot)
        return mot
    elif etape == 2:
        mot = motsNormaux[random.randint(0, len(motsNormaux)-1)]
        display.setCursor(4,0)
        display.message(mot)
        return mot
    elif etape == 3:
        mot = motsLongs[random.randint(0, len(motsLongs)-1)]
        display.setCursor(4,0)
        display.message(mot)
        return mot

def accept(mdp):
    """
    Code executer lorsque l'utilisateur rentre la combinaison de chiffre et appuis sur A
    """
    global indexLettre
    verification = conversion()
    if verification == mdp[indexLettre]:
        print("Lettre validé")
        display.setCursor(indexLettre, 1)
        display.message(verification)
        indexLettre += 1
        listeTouches.clear()
        if indexLettre >= len(mdp):
            print("Fin du mot") # Mot réussi
            indexLettre = 0
            finEtape()
    else:
        Erreurs.__add__()
        listeTouches.clear()
        display.setCursor(indexLettre, 1)
        display.message("_")
        time.sleep(0.7)


def clear():
    """
    Code executer lorsque l'utilisateur appuis sur D
    Permet de reset les chiffres sur lequels il à appuyer
    """
    listeTouches.clear()
    print("cleared")

MultiTap = {"A":"accept()", "C":"cancel()", "D":"", # A changer
            "0":"_",
            "8":"A", "88":"B", "888":"C", "1":"D", "11":"E", "6":"F", "66":"G", "666":"H", "3":"I", "33":"J", "7":"K", "77":"L", "#":"M", "##":"N", "###":"O", "9":"P", "99":"Q", "4":"R", "44":"S", "*":"T", "**":"U", "***":"V", "5":"W", "55":"X", "2":"Y", "22":"Z"}

def conversion():
    """
    Changement des touches rentées par l'utilisateur en lettres
    """
    chiffres = ""

    if len(listeTouches) != 0:

        if len(listeTouches) <= 3:
        
            for i in range(len(listeTouches)):
                chiffres += listeTouches[i]    
            return (MultiTap.get(chiffres))
    else:
        pass


def module_1():
    """
    Code principal de l'enigme 
    """
    print("Lancement du module 1 ...")    
    # Initialize the keypad class
    kp = keypad()
    display.clear()
    Erreurs.__str__()
    motDePasse = choixMot()
    print(motDePasse)
    # Loop while waiting for a keypress
    while etape != 4:
        digit = None
        while digit == None:
            digit = kp.getKey()   
        # Print the result
        if digit == "A":
            accept(motDePasse)
        elif digit == "B":
            pass
        elif digit == "C":
            clear()
        elif digit == "D":
            pass
        else:
            listeTouches.append(str(digit))
        print(listeTouches)
        time.sleep(0.5)

    else:
        sonFinModule()
        display.clear()
        display.setCursor(0, 0)
        
        for i in range(18):
            display.scrollDisplayLeft()
        display.message("-- Module suivant -- \n -_-_-_-_-_-_-_-_ ")
        for i in range(28):      
            display.scrollDisplayRight()
            time.sleep(0.2)

        

#Supprimer par la suite pour mettre une variable de module finit (lorsque = nb max fin du jeu)
if __name__ == '__main__': 
    try:
        module_1()
    except KeyboardInterrupt:  # Quand 'Ctrl+C' est pressé, le code si dessous s'éxecute.                 
        display.clear() # Clear l'écran
        GPIO.cleanup() # Laisse les ressources


