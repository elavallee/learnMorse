from itertools import chain

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
             'z':'--..'}

def smorse(word):
    "Convert the word to morse code with no spaces."
    txt = ''
    for letter in word:
        txt += morseDict[letter]
    return txt

print(smorse('three'))

reverseMorseDict = {y: x for x, y in zip(morseDict.keys(), morseDict.values())}

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def solve(txt, alphabet=alphabet, solution=''):
    "Solve all permutations of the alphabet in Morse code with no spaces between letters."
    solutions = []
    for letter in alphabet:
        morseLetter = morseDict[letter]
        if morseLetter == txt and len(alphabet) == 1: return solution + letter
        if morseLetter == txt[:len(morseLetter)]:
            sol = solve(txt[len(morseLetter):],
                         alphabet.replace(letter, ''), solution + letter)
            if sol != []:
                if isinstance(sol[0], list):
                    sol = list(chain(*sol))
                solutions.append(sol)
    return solutions

print(solve(''.join(morseDict[x] for x in alphabet)))

sol = list(chain(*solve('..-...-..-....--.---.---.---..-..--....-.....-..-.--.-.-.--.-..--.--..--.----..-..')))

print(sol)

assert 'uvfsqmjazxthbidyrkcwegponl' in sol


