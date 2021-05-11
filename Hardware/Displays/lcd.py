class LcdBaseClass():


        
    def write(self,toDisplay:str):
        pass

    def clear(self):
        pass
        

class Lcd(LcdBaseClass):

    def write(self,toDisplay:str):
        print("LOG Lcd: write() ")
        #### TODO To Implement
    
    def clear(self):
        print("LOG Lcd: clear() ")
        #### TODO To Implement
    
class LcdMock(LcdBaseClass):

    def write(self,toDisplay:str):
        print("LOG LcdMock: write()")
        print("action :", toDisplay)

    def clear(self):
        print("LOG LcdMock: clear() ")
   



