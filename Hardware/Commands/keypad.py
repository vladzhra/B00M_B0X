from Hardware.Commands.commandBase import *
import RPi.GPIO as GPIO  

class KeypadBaseClass(CommandBase):
    """Classe de base du keypad.

    Cette classe sert à construire les héritages.

    """
    def getKey(self):
        print("LOG KeypadBaseClass: getKey")
        return None

    def exit(self):
        print("LOG KeypadBaseClass: exit")
        return None





class Keypad(KeypadBaseClass):
    """Classe hérité de KeypadBaseClass.

    Cette classe sert a faire marcher le keypad.

    Méthodes
    ----------
    getKey :
        Permet de récuperer la touche sur laquelle l'utilisateur à appuyé.
    exit :
        Permet de libérer les gpio utilisés pour le keypad
    """
    # CONSTANTS   
    KEYPAD = [
    [1,2,3,"A"],
    [4,5,6,"B"],
    [7,8,9,"C"],
    ["*",0,"#","D"]
    ]
     
    # ROW = [11,12,13,15]        #C'est tes pins gabys
    # COLUMN = [16,18,22,7]

    ROW = [18,16,15,13]      #la c'est les miens
    COLUMN = [12,10,8,7]



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

class KeypadMock(KeypadBaseClass):
    """Classe hérité de KeypadBaseClass.

    Cette classe sert à debbuger le code du keypad sans le hardware.

    Méthodes
    ----------
    getKey :
        Permet de récuperer la touche sur laquelle l'utilisateur à appuyé.
    """
    
    def getKey(self):
        print("LOG KeypadMock: Keypad Mock read key")
        nb = str(input("Input : "))
        return nb



