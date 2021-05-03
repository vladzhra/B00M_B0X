"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Modules/Module_5.py
Description :

Module : 
    Objective : 
    Malus : 
"""

import random

def test():
    print("bzz test")

def un():
    print("bzz un")

def deux():
    print("bzz deux")

def trois():
    print("bzz trois")

def quatre():
    print("bzz quatre")



def shortpassword():
    print("shortpassword")


    random.choice(test, un, deux)

def mediumpassword():
    print("mediumpassword")

    for i in range(8):
        random.choice(test(), un(), deux(), trois(), quatre())

def strongpassword():
    print("strongpassword")
    for i in range(10):
        random.choice(test(), un(), deux(), trois(), quatre())


# random.choice(shortpassword(), mediumpassword(), strongpassword())
shortpassword()
