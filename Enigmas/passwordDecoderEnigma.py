from Enigmas.enigmaBase import *
from Hardware.Commands.keypad import *
from Hardware.Displays.lcd import *
from Core.error import *

class PasswordDecoderEnigma(EnigmaBase):
    
    def __init__(self, kp:KeypadBaseClass, lcd:LcdBaseClass, er:Error):
        self.kp = kp
        self.lcd = lcd
        self.er = er
        

    def resolveEnigma(self):
        """
        Code principal de l'enigme 
        """
        # kpstr = self.kp.readKey()
        # self.lcd.write(kpstr)
    
        # kp = keypad()
        self.lcd.clear()
        self.er.__str__()
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
        self.lcd.clear()
        self.lcd.setCursor(0, 0)
        
        for i in range(18):
            self.lcd.scrollDisplayLeft()
        self.lcd.message("-- Module suivant -- \n -_-_-_-_-_-_-_-_ ")
        for i in range(28):      
            self.lcd.scrollDisplayRight()
            time.sleep(0.2)

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
            self.lcd.setCursor(4,0)
            self.lcd.message(mot)
            return mot
        elif etape == 2:
            mot = motsNormaux[random.randint(0, len(motsNormaux)-1)]
            self.lcd.setCursor(4,0)
            self.lcd.message(mot)
            return mot
        elif etape == 3:
            mot = motsLongs[random.randint(0, len(motsLongs)-1)]
            self.lcd.setCursor(4,0)
            self.lcd.message(mot)
            return mot
