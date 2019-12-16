import sys

MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.', 
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-', 
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-', 
    '(': '-.--.',
    ')': '-.--.-'} 


try:
    if len(sys.argv) == 1:
        sys.exit()
    cipher = ''
    length = len(sys.argv)
    for index, word in enumerate(sys.argv):
        if index == 0:
            continue
        assert word.isalnum() or ' ' in word
        for letter in word:
            if letter != ' ':
                cipher += MORSE_CODE_DICT[letter.upper()] + ' '
            else:
                cipher += ' '
        if index < length - 1:
            cipher += ' / '
    print(cipher)
except AssertionError:
    print('ERROR')
