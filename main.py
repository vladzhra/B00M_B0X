"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Main.py
Description : The main code were everything happens
"""

from Enigmas.passwordDecoderEnigma import *

def main(kp:KeypadBaseClass, lcd:LcdBaseClass):
    pa = PasswordDecoderEnigma(kp, lcd)
    pa.resolveEnigma()



if __name__ == '__main__': 
    x = KeypadMock()

    # x = Keypad()




    y = LcdMock()

    # y = Lcd()

    main(x,y)
       