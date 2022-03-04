"""
This is a file that deals with converting the duration and
notes, coded by the user for convinience. 

Note: Classes are used. 

"""

#This is a class that will convert the note duration in seconds.
class noteDuration():

    def setTempo(self, nTempo):
        self.nTempoSet = nTempo 

    def noteToSecs(self, nEnteredNoteDuration):

        self.nNoteDuration = nEnteredNoteDuration

        self.nWhole = 60/(self.nTempoSet/4)

        self.nReturnValue = 0


        if (self.nNoteDuration == 1):
            self.nReturnValue = self.nWhole
        
        #Half Note
        elif (self.nNoteDuration == 2):
            self.nReturnValue = self.nWhole / 2 

        #Quarter Note
        elif (self.nNoteDuration == 4):
            self.nReturnValue = self.nWhole / 4
        
        #Eight Note
        elif (self.nNoteDuration == 8):
            self.nReturnValue = self.nWhole / 8
        
        #Sixthteenth Note
        elif (self.nNoteDuration == 16):
            self.nReturnValue = self.nWhole / 16

        else:
            print("Error")

        return self.nReturnValue - 0.001

#This class will take care on converting the numbers into their 
#respective frequency.

class Frequency:

    #TAKE NOTE! This is using Middle C in 12-Tone Equal Temperment
    def numToFrequency(self, nEnteredNote):

        self.nNote = nEnteredNote

        #This is Middle C
        self.nBaseNote = 261.626

        if (self.nNote >= 2):
            self.nReturnValue = self.increaseNote(self.nNote)
        
        elif (self.nNote < 0):
           self.nReturnValue = self.decreaseNote(self.nNote)
        
        elif(self.nNote == 1):
            self.nReturnValue = self.nBaseNote
        
        else:
            self.nReturnValue = 0.0
        
        return self.nReturnValue

    def increaseNote(self, nNote):
        self.nCounter = nNote - 1
        self.nBaseNoteCh = self.nBaseNote
        self.nProduct = 1

        while (self.nCounter > 0):
            self.nProduct = self.nBaseNoteCh * 1.05946309435929
            self.nBaseNoteCh = self.nProduct
            self.nCounter -= 1

        return self.nBaseNoteCh
    
    def decreaseNote(self,nNote):
        self.nCounter = nNote
        self.nBaseNoteCh = self.nBaseNote
        self.nQuotient = 1

        while (self.nCounter < 0):
            self.nQuotient = self.nBaseNoteCh / 1.05946309435929
            self.nBaseNoteCh = self.nQuotient
            self.nCounter += 1
        
        return self.nBaseNoteCh