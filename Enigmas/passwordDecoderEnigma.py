from Enigmas.enigmaBase import *
from Hardware.Commands.keypad import *
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
        # kpstr = self.kp.readKey()
        # self.lcd.write(kpstr)
    
        # kp = keypad()
        self.lcd.clear()
        self.er.__str__()
        motDePasse = choixMot()
        print(motDePasse)
        # Loop while waiting for a keypress
        while self.etape != 4:
            digit = None
            while digit == None:
                digit = self.kp.getKey()   
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
                self.listeTouches.append(str(digit))
            print(self.listeTouches)
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

        if self.etape == 1:
            mot = motsCourt[random.randint(0, len(motsCourt)-1)] # Longueur -1 car l'indexage d'une liste commence à 0
            self.lcd.setCursor(4,0)
            self.lcd.message(mot)
            return mot
        elif self.etape == 2:
            mot = motsNormaux[random.randint(0, len(motsNormaux)-1)]
            self.lcd.setCursor(4,0)
            self.lcd.message(mot)
            return mot
        elif self.etape == 3:
            mot = motsLongs[random.randint(0, len(motsLongs)-1)]
            self.lcd.setCursor(4,0)
            self.lcd.message(mot)
            return mot

    def accept(mdp):
        """
        Code executer lorsque l'utilisateur rentre la combinaison de chiffre et appuis sur A
        """
        verification = conversion()
        if verification == mdp[self.indexLettre]:
            print("Lettre validé")
            self.lcd.setCursor(self.indexLettre, 1)
            self.lcd.message(verification)
            self.indexLettre += 1
            self.listeTouches.clear()
            if self.indexLettre >= len(mdp):
                print("Fin du mot") # Mot réussi
                self.indexLettre = 0
                finEtape()
        else:
            self.er.__add__()
            self.listeTouches.clear()
            self.lcd.setCursor(self.indexLettre, 1)
            self.lcd.message("_")
            time.sleep(0.7)

    def conversion():
        """
        Changement des touches rentées par l'utilisateur en lettres
        """
        chiffres = ""

        if len(self.listeTouches) != 0:

            if len(self.listeTouches) <= 3:
            
                for i in range(len(self.listeTouches)):
                    chiffres += self.listeTouches[i]    
                return (MultiTap.get(chiffres))
        else:
            pass

    def finEtape():
        
        self.etape += 1
        if self.etape == 4:
            pass
        else:
            self.lcd.clear()
            self.lcd.setCursor(0, 0)
            
            for i in range(18):
                self.lcd.scrollDisplayLeft()
            self.lcd.message(" == Mot suivant == \n =-=-=-=-=-=-=-=- ")
            sonFinEtape()
            for i in range(28):      
                self.lcd.scrollDisplayRight()
                time.sleep(0.2)

        return 
        resolveEnigma()
