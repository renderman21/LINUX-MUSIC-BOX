"""
This is the part where the mechanic is explained.
As you can see, this is the LINUX MUSIC BOX, where
you can make your own tunes using pysine.

Some reminders: Have some a bit of Python knowledge,
and music theory as, most of the time, you will be 
configuring most of the things here. 

NOTES: 
    In creating notes(such as C, C#, and etc.), you
    are encouraged to use the following numbers 
    below and put it in the method numToFrequency()
    from the class "Frequency".

    USER_NUMBER_INPUT       NOTE_NAME
            1                   C
            2                   C#/Db
            3                   D
            4                   D#/Eb
            5                   E
            6                   F
            7                   F#/Gb
            8                   G
            9                   G#/Ab
            10                  A
            11                  A#/Bb
            12                  B
            13                  C (Octave)
    
    You can play notes below USER_NUMBER_INPUT of 1 or above
    13.

    To play the lower notes, simply start at -1, thus 
    making it into a Cb, and decrease

    To play the higher notes, simply add the USER_NUMBER_INPUT
    by 12 and you will get the higher octave of that referred note

    However, inputting 0 will render it as silent. 

NOTES DURATION:
    The "Notes Duration" refers to 'Whole Notes', 'Half Notes', etc.
    It is also encouraged to use the numbers below and put it
    in the (thing).

    USER_NUMBER_INPUT       DURATION
            1                 WHOLE
            2                 HALF
            4                 QUARTER
            8                 EIGHT
            16                SIXTHTEENTH
    

That is all. Have fun!

"""

from utils import *
from pysine import sine


def main():

    freq = Frequency()
    dur = noteDuration()

    #Set your referred tempo here in BPM
    dur.setTempo(150)


    nLoopCount = 1

    
    #This is where you will put your notes

    #TETRIS THEME
    while nLoopCount >= 0:

        nCounter = 1

        while (nCounter >= 0):
            #Bar One
            sine(freq.numToFrequency(17), dur.noteToSecs(4)) # E
            sine(freq.numToFrequency(12), dur.noteToSecs(8)) # B
            sine(freq.numToFrequency(13), dur.noteToSecs(8)) # C
            sine(freq.numToFrequency(15), dur.noteToSecs(8)) # D
            sine(freq.numToFrequency(17), dur.noteToSecs(16)) # E
            sine(freq.numToFrequency(15), dur.noteToSecs(16)) # D
            sine(freq.numToFrequency(13), dur.noteToSecs(8)) # C
            sine(freq.numToFrequency(12), dur.noteToSecs(8)) # B

            #Bar Two
            sine(freq.numToFrequency(10), dur.noteToSecs(4)) # A
            sine(freq.numToFrequency(10), dur.noteToSecs(8)) # A
            sine(freq.numToFrequency(13), dur.noteToSecs(8)) # B
            sine(freq.numToFrequency(17), dur.noteToSecs(4)) # E
            sine(freq.numToFrequency(15), dur.noteToSecs(8)) # D
            sine(freq.numToFrequency(13), dur.noteToSecs(8)) # C

            #Bar Three

            sine(freq.numToFrequency(12), dur.noteToSecs(4)) # B
            sine(freq.numToFrequency(12), dur.noteToSecs(16)) #B
            sine(freq.numToFrequency(12), dur.noteToSecs(16)) # B
            sine(freq.numToFrequency(13), dur.noteToSecs(8)) # C
            sine(freq.numToFrequency(15), dur.noteToSecs(4)) # D
            sine(freq.numToFrequency(17), dur.noteToSecs(4)) # E

            #Bar Four

            sine(freq.numToFrequency(13), dur.noteToSecs(4)) # C
            sine(freq.numToFrequency(10), dur.noteToSecs(4)) # A
            sine(freq.numToFrequency(10), dur.noteToSecs(2)) # A

            #REPEAT#

            #Bar Five
            sine(freq.numToFrequency(15), dur.noteToSecs(4)) # D
            sine(freq.numToFrequency(15), dur.noteToSecs(8)) # D
            sine(freq.numToFrequency(18), dur.noteToSecs(8)) # F  
            sine(freq.numToFrequency(22), dur.noteToSecs(4)) # A 
            sine(freq.numToFrequency(20), dur.noteToSecs(8)) # G
            sine(freq.numToFrequency(18), dur.noteToSecs(8)) # F  

            #Bar Six
            sine(freq.numToFrequency(17), dur.noteToSecs(4)) # E
            sine(freq.numToFrequency(17), dur.noteToSecs(8)) # E
            sine(freq.numToFrequency(13), dur.noteToSecs(8)) # C
            sine(freq.numToFrequency(17), dur.noteToSecs(4)) # E
            sine(freq.numToFrequency(15), dur.noteToSecs(8)) # D
            sine(freq.numToFrequency(13), dur.noteToSecs(8)) # C

            #Bar Seven

            sine(freq.numToFrequency(12), dur.noteToSecs(4)) # B
            sine(freq.numToFrequency(12), dur.noteToSecs(16)) #B
            sine(freq.numToFrequency(12), dur.noteToSecs(16)) # B
            sine(freq.numToFrequency(13), dur.noteToSecs(8)) # C
            sine(freq.numToFrequency(15), dur.noteToSecs(4)) # D
            sine(freq.numToFrequency(17), dur.noteToSecs(4)) # E

            #Bar Eight

            sine(freq.numToFrequency(13), dur.noteToSecs(4)) # C
            sine(freq.numToFrequency(10), dur.noteToSecs(4)) # A
            sine(freq.numToFrequency(10), dur.noteToSecs(2)) # A

            nCounter-=1

        #CODA

        #Bar Ninth
        sine(freq.numToFrequency(17), dur.noteToSecs(2)) # E
        sine(freq.numToFrequency(13), dur.noteToSecs(2)) # C

        #Bar Tenth
        sine(freq.numToFrequency(15), dur.noteToSecs(2)) # D
        sine(freq.numToFrequency(12), dur.noteToSecs(2)) # B

        #Bar Eleventh
        sine(freq.numToFrequency(13), dur.noteToSecs(2)) # C
        sine(freq.numToFrequency(10), dur.noteToSecs(2)) # A

        #Bar Twelth
        sine(freq.numToFrequency(9), dur.noteToSecs(2)) # G#
        sine(freq.numToFrequency(12), dur.noteToSecs(2)) # B

        #Bar 13th
        sine(freq.numToFrequency(17), dur.noteToSecs(2)) # E
        sine(freq.numToFrequency(13), dur.noteToSecs(2)) # C

        #Bar 14th
        sine(freq.numToFrequency(15), dur.noteToSecs(2)) # D
        sine(freq.numToFrequency(12), dur.noteToSecs(2)) # B

        #Bar 15th 
        sine(freq.numToFrequency(13), dur.noteToSecs(4)) # C
        sine(freq.numToFrequency(17), dur.noteToSecs(4)) # E
        sine(freq.numToFrequency(22), dur.noteToSecs(4)) # A
        sine(freq.numToFrequency(22), dur.noteToSecs(4)) #A

        #Bar 16th
        sine(freq.numToFrequency(21), dur.noteToSecs(1)) # G#

        nLoopCount -=1
        



if __name__ == "__main__":
    main()
