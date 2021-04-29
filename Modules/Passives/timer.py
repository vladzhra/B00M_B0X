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
pins = [11,12,13,15,16,18,22,7,3,5,24,26]  
bits = [BIT0, BIT1, BIT2, BIT3]  

def print_msg():  
        print ('Program is running...')  
        print ('Please press Ctrl+C to end the program...')  

def digitalWriteByte(val):  
        GPIO.output(11, val & (0x01 << 0))  
        GPIO.output(12, val & (0x01 << 1))  
        GPIO.output(13, val & (0x01 << 2))  
        GPIO.output(15, val & (0x01 << 3))  
        GPIO.output(16, val & (0x01 << 4))  
        GPIO.output(18, val & (0x01 << 5))  
        GPIO.output(22, val & (0x01 << 6))  
        GPIO.output(7,  val & (0x01 << 7))  

def display_1():   
        GPIO.output(BIT0, GPIO.LOW)  
        for i in range(10):  
                digitalWriteByte(segCode[i])  
                time.sleep(0.5)  

def display_2():  
        for bit in bits:  
                GPIO.output(bit, GPIO.LOW)   
        for i in range(10):  
                digitalWriteByte(segCode[i])  
                time.sleep(0.5)  

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
        time.sleep(0.01)  
        GPIO.output(BIT3, GPIO.HIGH)   

        GPIO.output(BIT1, GPIO.LOW)  
        digitalWriteByte(segCode[b1])  
        time.sleep(0.01)  
        GPIO.output(BIT1, GPIO.HIGH)  

        GPIO.output(BIT0, GPIO.LOW)  
        digitalWriteByte(segCode[b2])  
        time.sleep(0.01)  
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


def loop():  
        seconds = 300
        countdown = seconds
        for i in range(seconds):
                mins, secs = divmod(countdown, 60)
                dizainesec = secs % 100 / 10  
                unitesec = secs % 10
                print(countdown , mins, secs, mins, dizainesec, unitesec)
                loopdisplay(mins, dizainesec, unitesec)
                countdown -= 1
        
        print("boom")

        





        # seconds = 500
        # timeremain = 501
        # for j in range(seconds):
                
        #         timeremain = timeremain - 1
        #         if timeremain > 459 and timeremain < 500:
        #                 timeremain = 459
        #         elif timeremain > 359 and timeremain < 400:
        #                 timeremain = 359
        #         elif timeremain > 259 and timeremain < 300:
        #                 timeremain = 259
        #         elif timeremain > 159 and timeremain < 200:
        #                 timeremain = 159
        #         elif timeremain > 59 and timeremain < 100:
        #                 timeremain = 59
        #         for i in range(150):
        #                 timer(0,1,2)
        #                 time.sleep(0.5) 
                                
                
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
        loop()

    except KeyboardInterrupt:    
        destroy()    
