from Enigmas.passwordDecoderEnigma import * 
from Enigmas.enigmaBase import *
from Hardware.Commands.keypad import *
from Hardware.Displays.lcd import *
import sys

class GameEngine():

    enigmasCount = 5
    enigmasList = []

    def __init__(self, kp:KeypadBaseClass, lcd:LcdBaseClass, er:Error):
        self.kp = kp
        self.lcd = lcd
        self.er = er


    def process(self):
        self.displayInit()
        self.selectEnigmas()
        self.displayEnigmas()
        self.launchCountdown() #include displaying coundown
        self.mainEngineLoop()
        self.endOfGame(True)

    
    def displayInit(self):
        print("START !!!!")
        
    def selectEnigmas(self):
        self.enigmasList = [1, 3, 4] #TODO

    def displayEnigmas(self):
        print(self.enigmasList)

    def launchCountdown(self):   #include displaying countdown
        print("LOG launchCountdown ")#c'est vraiment TODO

    def mainEngineLoop(self):
        for i in range(len(self.enigmasList)):
            print("Enigma ", i)
            eng = None
            crtEnigma = self.enigmasList[i]
            if crtEnigma == 1:
                print("PasswordDecoderEnigma")
                eng = PasswordDecoderEnigma(self.kp, self.lcd, self.er)
            elif crtEnigma == 2:
                print("enigma 2")
                
            elif crtEnigma == 3:
                print("enigma 3")

            elif crtEnigma == 4:
                print("enigma 4")
            else:
                print("enigma 5")
            
            enigmaResult = eng.resolveEnigma()

            if enigmaResult == False: # GAME LOST
                print("end of game")
                self.endOfGame(False) 


    def endOfGame(self, gameSucceeded):
        if gameSucceeded == True:
            print("bravoooooos")
        else:
            print("nuuuuul")

        sys.exit()