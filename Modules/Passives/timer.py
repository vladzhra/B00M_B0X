"""
Author : Gabriel Lepinay | Vlad Zaharia
Version : Python 3.7.3 - 32 bits
IDE : Visual Studio Code
Directory : /home/pi/Documents/Dev/B00mB0x/Modules/Passives/timer
Description : Timer's code

Module : Timer
    Objective : Set the timer of the bomb
  
"""

import RPi.GPIO as GPIO  
import time  
import threading

BIT0 = 3   
BIT1 = 5  
BIT2 = 24
BIT3 = 26


        

segCode = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]  #0~9  
pins = [11,12,13,15,16,18,22,7,3,5,26]  # Here to change pins 
bits = [BIT0, BIT1, BIT2, BIT3]  



def digitalWriteByte(val):  
        GPIO.output(11, val & (0x01 << 0))  
        GPIO.output(12, val & (0x01 << 1))  
        GPIO.output(13, val & (0x01 << 2))  
        GPIO.output(15, val & (0x01 << 3))  
        GPIO.output(16, val & (0x01 << 4))  
        GPIO.output(18, val & (0x01 << 5))  
        GPIO.output(22, val & (0x01 << 6))  
        GPIO.output(7,  val & (0x01 << 7))  


def timer(b0, b1, b2):  

        # if num < 10:  
        #         GPIO.output(BIT0, GPIO.LOW)   
        #         GPIO.output(BIT1, GPIO.HIGH)   
        #         GPIO.output(BIT2, GPIO.HIGH)   
        #         GPIO.output(BIT3, GPIO.HIGH)   
        #         digitalWriteByte(segCode[b0])
        # elif num >= 10 and num < 100:  
        #         GPIO.output(BIT0, GPIO.LOW)  
        #         digitalWriteByte(segCode[b0])  
        #         time.sleep(0.002)  
        #         GPIO.output(BIT0, GPIO.HIGH)   
        #         GPIO.output(BIT1, GPIO.LOW)  
        #         digitalWriteByte(segCode[b1])  
        #         time.sleep(0.002)  
        #         GPIO.output(BIT1, GPIO.HIGH)  
        # elif num >= 100 and num < 1000:  

        GPIO.output(BIT3, GPIO.LOW)  
        digitalWriteByte(segCode[b0])  
        time.sleep(0.005)  
        GPIO.output(BIT3, GPIO.HIGH)   

        GPIO.output(BIT1, GPIO.LOW)  
        digitalWriteByte(segCode[b1])  
        time.sleep(0.005)  
        GPIO.output(BIT1, GPIO.HIGH)  

        GPIO.output(BIT0, GPIO.LOW)  
        digitalWriteByte(segCode[b2])  
        time.sleep(0.005)  
        GPIO.output(BIT0, GPIO.HIGH)   


                
        # elif num >= 1000 and num < 10000:  
        #         GPIO.output(BIT0, GPIO.LOW)  
        #         digitalWriteByte(segCode[b0])  
        #         time.sleep(0.002)  
        #         GPIO.output(BIT0, GPIO.HIGH)   
        #         GPIO.output(BIT1, GPIO.LOW)  
        #         digitalWriteByte(segCode[b1])  
        #         time.sleep(0.002)  
        #         GPIO.output(BIT1, GPIO.HIGH)  
        #         GPIO.output(BIT2, GPIO.LOW)  
        #         digitalWriteByte(segCode[b2])  
        #         time.sleep(0.002)  
        #         GPIO.output(BIT2, GPIO.HIGH)   
        #         GPIO.output(BIT3, GPIO.LOW)  
        #         digitalWriteByte(segCode[b3])  
        #         time.sleep(0.002)  
        #         GPIO.output(BIT3, GPIO.HIGH)   
        # else:  
        #         print ('Out of range, num should be 0~9999 !' ) 
temp =1




def setup():  
        GPIO.setmode(GPIO.BOARD)    #Number GPIOs by its physical location  
        GPIO.setwarnings(False)
        for pin in pins:  
                GPIO.setup(pin, GPIO.OUT)    #set all pins' mode is output  
                GPIO.output(pin, GPIO.HIGH)  #set all pins are high level(3.3V)  
        
countdown = 0

def loop():  
        seconds = 300
        countdown = seconds
        while countdown > 0:
                mins, secs = divmod(countdown, 60)
                dizainesec = secs % 100 / 10  
                unitesec = secs % 10
                print("                 {} secondes !        {}:{} ".format(countdown, mins, secs))
                loopdisplay(mins, dizainesec, unitesec)
                countdown -= 1
        
        print("Boom")

def erreur():
        countdown -= 10


def loopdisplay(a,b,c):
        timeout = time.time() + 1   # 1 sec from now
        while time.time() < timeout:
                
                timer(a,b,c)

                   

def destroy():   #When program ending, the function is executed.   
    for pin in pins:    
        GPIO.output(pin, GPIO.LOW) #set all pins are low level(0V)   
        GPIO.setup(pin, GPIO.IN)   #set all pins' mode is input  



if __name__ == '__main__': #Program starting from here   
    setup()   
    try:  
        print("\n\nVous avez 300 secondes pour desamorcer la bombe, bonne chance !\n")
        print("[Il vous reste] :")
        loop()

    except KeyboardInterrupt:    
        destroy()    
