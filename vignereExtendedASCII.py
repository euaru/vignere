"""
    Vignere chiper for 256 ASCII character
    
    Created by: Bintang Nafsul Mutmainnah
                Kurnia Theo Rahmanto
"""

import sys

def toOrdList(targetText):
    y  = []
    for x in targetText:
        y += [ord(x)]
    return y
    """ This method return list of ASCII number of every character from given string
        i.e  : ('ABC') => [65, 66, 67]
    """

def convOrd(stringOrd, key):
    m = []
    k = []
    for i in range(len(stringOrd)):
        m += [stringOrd[i]]
    for i in range(len(key)):
        k += [key[i]]
    chiperNumbers = []
    for i in range(len(m)):
        c = (m[i]+k[i%len(k)]) % 256
        chiperNumbers += [c]
    return chiperNumbers
    """ This method return list of altered ASCII number from given list of ASCII Number
        based on the given key
        i.e  :  ([65, 66, 67], [82]) ==> [82, 83, 84]
    """

def ordToString(stringOrd):
    rText = []
    for x in stringOrd:
        rText += [chr(x)]
    rText = ''.join(rText)
    return rText
    """ This method return a string from given list ASCII numbers
        i.e  : ([82, 83, 84]) ==> 'RST'
    """

def enchiper(unalteredText, chiperKey):
    alteredText = ordToString(convOrd(toOrdList(unalteredText),toOrdList(chiperKey)))
    return alteredText
    """This method calls all the method needed to enchiper given string using the given key.
       This method return the enchipered text with the same spacing as the plain text.
    """

def dechiper(unalteredText, chiperKey):
    x = toOrdList(unalteredText)
    y = toOrdList(chiperKey)
    for i in range(len(y)):
        y[i] *= (-1)
    alteredText = ordToString(convOrd(x, y))
    return alteredText
    """This method calls all the method needed to dechiper given string using the given key.
       This method return the dechipered text with the same spacing as the chiper text.
    """

textFile = open(sys.argv[1])
keyFile = open(sys.argv[2])
outFile = open(sys.argv[3], 'w')
outFile.truncate()

unaltered = textFile.read(-1)
key = keyFile.read(-1)

print 'mode:'
print '1. Enchiper'
print '2. Dechiper\n'

mode = 0
while mode != 1 and mode != 2:
    mode = int(raw_input('Choose mode number: '))
    if mode != 1 and mode != 2: print 'Invalid mode. Try again...\n'

if mode == 1:
    outFile.write(enchiper(unaltered, key))
else:
    outFile.write(dechiper(unaltered, key))

textFile.close()
keyFile.close()
outFile.close()