"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Modules/Passives/lcd.py
Description : LCD's code 

Module : Lcd screen
    Objective : Use the screen to write text
  
"""


from Hardware.Displays.adeeptDisplay import *

class LcdBaseClass():


        
    def message(self,toDisplay:str):
        pass

    def clear(self):
        pass
    
    def begin(self):
        pass
    
    def setCursor(self, row, column):
        pass
    
    def scrollDisplayLeft(self):
        pass

    def scrollDisplayRight(self):
        pass



class Lcd(LcdBaseClass):

    def __init__(self):
        mcp.output(3,1)     # Allume la lumiere du display
        self.begin(16,2)     # Met le nombre du colonne et de ligne de l'écran

    def message(self,toDisplay:str):
        print("LOG Lcd: write() ")
        #### TODO To Implement
    
    def clear(self):
        print("LOG Lcd: clear() ")
        #### TODO To Implement
    
    def begin(self):
        pass
    
    def setCursor(self, row, column):
        pass
    
    def scrollDisplayLeft(self):
        pass

    def scrollDisplayRight(self):
        pass

class LcdMock(LcdBaseClass):

    def message(self,toDisplay:str):
        print("LOG LcdMock: write()")
        print("action :", toDisplay)

    def clear(self):
        print("LOG LcdMock: clear() ")

    def begin(self):
        print("LOG LcdMock: begin() ")

    
    def setCursor(self, row, column):
        print("LOG LcdMock: setCursor() ")

    
    def scrollDisplayLeft(self):
        print("LOG LcdMock: scrollDisplayLeft() ")


    def scrollDisplayRight(self):
        print("LOG LcdMock: scrollDisplayRight() ")
   



