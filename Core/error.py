"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Modules/Passives/erreur.py
Description : Mistakes's code

Module : Aucun
    Objective : Code to work mistakes
"""

class Error: 
    """
    Class Error : Object = Error()

    Methode :
        clear : reset to 0 the number of mistakes
        explosion : start the code to loose the game
        __str__ : print on the lcd sreen number of mistakes
        __add__ : add one mistakes to the count
    """

    nbError = 0

    def clear(self):
        self.nbError = 0


    def explosion(self):
        # sonExplosion()    #TODO
        # lcd.clear()
        # lcd.setCursor(0, 0)
        # for i in range(12):
        #     lcd.scrollDisplayLeft()

        # lcd.message("Game Over ! \n    :(")
        # for i in range(28):      
        #     lcd.scrollDisplayRight()
        #     time.sleep(0.3)
        # sys.exit()
        pass
        # TODO



    def __str__(self):
        # lcd.display()
        # mcp.output(3,1)     # turn on LCD backlight
        # lcd.begin(16,2)     # set number of LCD lines and columns
        # lcd.setCursor(0, 0)
        # if self.nbError <= 0: 
        #     lcd.message("[  ]")
        # elif self.nbError == 1: 
        #     lcd.message("[X ]")
        # elif self.nbError >= 2: 
        #     lcd.message("[XX]")      
        pass 
        # TODO

    def __add__(self):
        if self.nbError < 2 : 
            self.nbError += 1
            self.__str__()
            # timer.erreur()
            # sonErreur()
        else:
            # lcd.clear()
            # lcd.setCursor(0, 0)
            # lcd.message("BOOM")
            # time.sleep(1.5)
            self.explosion()
        pass
        # TODO

    def count(self):
        return self.nbError
