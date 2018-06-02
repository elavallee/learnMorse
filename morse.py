import winsound
import time
import sys

morseDict = {'a':'.-',
             'b':'-...',
             'c':'-.-.',
             'd':'-..',
             'e':'.',
             'f':'..-.',
             'g':'--.',
             'h':'....',
             'i':'..',
             'j':'.---',
             'k':'-.-',
             'l':'.-..',
             'm':'--',
             'n':'-.',
             'o':'---',
             'p':'.--.',
             'q':'--.-',
             'r':'.-.',
             's':'...',
             't':'-',
             'u':'..-',
             'v':'...-',
             'w':'.--',
             'x':'-..-',
             'y':'-.--',
             'z':'--..',
             '1':'.----',
             '2':'..---',
             '3':'...--',
             '4':'....-',
             '5':'.....',
             '6':'-....',
             '7':'--...',
             '8':'---..',
             '9':'----.',
             '0':'-----',
             '.':'.-.-.-',
             ',':'--..--',
             '?':'..--..',
             "'":'.----.',
             '!':'-.-.--',
             '/':'-..-.',
             '(':'-.--.',
             ')':'-.--.-',
             '&':'.-...',
             ':':'---...',
             ';':'-.-.-.',
             '=':'-...-',
             '+':'.-.-.',
             '-':'-....-',
             '_':'..--.-',
             '"':'.-..-.',
             '$':'...-..-',
             '@':'.--.-.'}

speedFac = 0.95
Freq = 2500
dotSpd = 300
dashSpd = dotSpd*3

def convertASCII(txt):
    """"convert the text txt into morse code with beeps"""
    txt = txt.lower()
    for char in txt:
        if char in morseDict:
            morseCode = morseDict[char]
        else:
            morseCode = ''
        print "{} {}".format(char, morseCode)
        sys.stdout.flush()
        if char in morseDict:
            for dashDot in morseDict[char]:
                if dashDot == '.':
                    winsound.Beep(Freq, int(dotSpd/speedFac))
                else:
                    winsound.Beep(Freq, int(dashSpd/speedFac))
                time.sleep((dotSpd*3/1000)/speedFac)
            time.sleep((dashSpd*3/1000)/speedFac)
        elif char == ' ':
            time.sleep((dotSpd*3/1000)*7/speedFac)

if __name__ == "__main__":
    convertASCII("Mostly cloudy, with a low around 57. Southwest wind around 5 mph becoming calm after midnight.")

