#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from random import *

"""
MATRIX_KEYBOARD

"""
class keypad():
    # CONSTANTS   
    KEYPAD = [
    [1,2,3,"A"],
    [4,5,6,"B"],
    [7,8,9,"C"],
    ["*",0,"#","D"]
    ]
     
    ROW         = [11,12,13,15]
    COLUMN      = [16,18,22,7]
     
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

    def getKey(self):
         
        # Set all columns as output low
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)
         
        # Set all rows as input
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
         
        # Scan rows for pushed key/button
        # A valid key press should set "rowVal"  between 0 and 3.
        rowVal = -1
        for i in range(len(self.ROW)):
            tmpRead = GPIO.input(self.ROW[i])
            if tmpRead == 0:
                rowVal = i
                 
        # if rowVal is not 0 thru 3 then no button was pressed and we can exit
        if rowVal < 0 or rowVal > 3:
            self.exit()
            return
         
        # Convert columns to input
        for j in range(len(self.COLUMN)):
			GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
         
        # Switch the i-th row found from scan to output
        GPIO.setup(self.ROW[rowVal], GPIO.OUT)
        GPIO.output(self.ROW[rowVal], GPIO.HIGH)
 
        # Scan columns for still-pushed key/button
        # A valid key press should set "colVal"  between 0 and 2.
        colVal = -1
        for j in range(len(self.COLUMN)):
            tmpRead = GPIO.input(self.COLUMN[j])
            if tmpRead == 1:
                colVal=j
                 
        # if colVal is not 0 thru 2 then no button was pressed and we can exit
        if colVal < 0 or colVal > 3:
            self.exit()
            return
 
        # Return the value of the key pressed
        self.exit()
        return self.KEYPAD[rowVal][colVal]
         
    def exit(self):
        # Reinitialize all rows and columns as input at exit
        for i in range(len(self.ROW)):
                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)


def module1():
        
    try:

        if __name__ == '__main__':
            # Initialize the keypad class
            kp = keypad()
            code = [1,2,3,"A","*"]
            code_test = []
            # Loop while waiting for a keypress

            while True:
                digit = None
                while digit == None:
                    digit = kp.getKey()    
                            
                # Print the result
                if len(code_test) < 5:
                    code_test.append(digit)
                else:
                    if code == code_test:
                        print("=======================\nCode bon")
                        print(code_test)
                    else:
                        print("Code mauvais \n[TIMER] -10 secondes \n=======================")
                        print(code_test)
                        for nb in range(len(code_test)):
                            code_test.pop()
                print(digit)
                time.sleep(0.5)

            
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be  executed.
        GPIO.output(LedPin1, GPIO.HIGH)     # led off
        GPIO.cleanup()                     # Release resource
'''
def module2():
    try:


            
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be  executed.
        GPIO.output(LedPin1, GPIO.HIGH)     # led off
        GPIO.cleanup()    

'''



print("zepartie")

LedPin1 = 29
LedPin2 = 31
LedPin3 = 33
LedPin4 = 35
LedPin5 = 37

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup((LedPin1,LedPin2,LedPin3,LedPin4,LedPin5), GPIO.OUT)   # Set pin mode as output
GPIO.output((LedPin1,LedPin2,LedPin3,LedPin4,LedPin5), GPIO.HIGH) # Set pin to high(+3.3V) to off the led

led_pins = [LedPin1,LedPin2,LedPin3,LedPin4,LedPin5]

for i in range (randint(2,5)):
	temp = choice(led_pins)
	GPIO.output(temp, GPIO.LOW)  # led on
	
	led_pins.remove(temp)
print(led_pins)



module1()   






"""
nb_aleatoire = randint(0,nb_max - 1)   
led_pins = [LedPin1,LedPin2,LedPin3,LedPin4]
nb_max = 4






except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be  executed.
    GPIO.output(LedPin1, GPIO.HIGH)     # led off
    GPIO.cleanup()                     # Release resource


"""

