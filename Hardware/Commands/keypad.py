from Hardware.Commands.commandBase import *

class KeypadBaseClass(CommandBase):
   
    def readKey(self):
        print("LOG KeypadBaseClass: Keypad Base read key")
        return None

class Keypad(KeypadBaseClass):

    def readKey(self):
        print("LOG Keypad: Keypad the real read key")
        return None
    
class KeypadMock(KeypadBaseClass):

    def readKey(self):
        print("LOG KeypadMock: Keypad Mock read key")
        return "A" 




