"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00M_B0X/Hardware/Displays/lcd.py
Description : LCD's code 

Module : Lcd screen
    Objective : Use the screen to write text
  
"""


from Hardware.Displays.adeeptDisplay import *

class LcdBaseClass():
    """Classe de base le l'écran lcd.

    Cette classe sert à construire les héritages.

    """

        
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
    
    """Classe hérité de LcdBaseClass.

    Cette classe sert a faire marcher l'écran lcd.

    Méthodes
    ----------
    message : str
        Permet d'afficher la chaîne de caractère mise en argument.
    clear : 
        Permet de reset tout l'affichage sur l'écran.
    begin : int1, int2
        Permet d'initialiser le nombre de colonne et de ligne de l'écran.
    setCursor : int1, int2
        Permet de placer le curseur à l'endroit voulu.
    scrollDisplayLeft :
        Permet de faire bouger tout l'écran vers la gauche.
    scrollDisplayRight :
        Permet de faire bouger tout l'écran vers la droite.
    """

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
    """Classe hérité de LcdBaseClass.

    Cette classe sert à debbuger le code de l'écran sans hardware.

    Méthodes
    ----------
    message : str
        Permet d'afficher la chaîne de caractère mise en argument.
    clear : 
        Permet de reset tout l'affichage sur l'écran.
    setCursor : int1, int2
        Permet de placer le curseur à l'endroit voulu.
    scrollDisplayLeft :
        Permet de faire bouger tout l'écran vers la gauche.
    scrollDisplayRight :
        Permet de faire bouger tout l'écran vers la droite.
    """

    def message(self,toDisplay:str):
        print("LOG LcdMock: write()")
        print("action :", toDisplay)

    def clear(self):
        print("LOG LcdMock: clear() ")

    def setCursor(self, row, column):
        print("LOG LcdMock: setCursor() ")

    def scrollDisplayLeft(self):
        print("LOG LcdMock: scrollDisplayLeft() ")

    def scrollDisplayRight(self):
        print("LOG LcdMock: scrollDisplayRight() ")
   



