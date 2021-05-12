"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Main.py²
Description : The main code were everything happens
"""
from Core.error import *
from Core.gameEngine import *
from Enigmas.passwordDecoderEnigma import *
from Hardware.Commands.keypad import *
from Hardware.Displays.lcd import *

def main(kp:KeypadBaseClass, lcd:LcdBaseClass, er: Error):
    
    engine = GameEngine(kp, lcd, er)
    engine.process()



if __name__ == '__main__': 
    kp = KeypadMock()
    # kp = Keypad()

    lcd = LcdMock()
    # lcd = Lcd()

    er = Error()

    
    main(kp, lcd, er)
       