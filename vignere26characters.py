"""
    Vignere chiper for 26 alphabet
    
    Created by: Bintang Nafsul Mutmainnah
                Kurnia Theo Rahmanto
"""

def textInput(something):
    a = False
    while a == False:
        x = str(raw_input('%s: ' % (something)))
        x = x.upper()
        a = True
        i = 0
        while i < len(x) and a == True:
            if (ord(x[i]) < 65 or ord(x[i]) > 90) and ord(x[i]) !=32:
                print 'Wrong input value. Input contains non-space non-alphabet character. Try again...\n'
                a = False
            i+=1
    return x
    """This method used to input a text to be either enchipered or dechipered.
       This method also check wether the input from user contains character other than
       the 26 alphabet or space
    """

def keyInput(something):
    a = False
    while a == False:
        x = str(raw_input('%s: ' % (something)))
        x = x.upper()
        a = True
        i = 0
        while i < len(x) and a == True:
            if ord(x[i]) < 65 or ord(x[i]) > 90:
                print 'Wrong input value. Input contains non-alphabet character. Try again...\n'
                a = False
            i+=1
    return x
    """This method used to input a word chosen as a key to enchiper or dechiper the proposed text.
       This method also check wether the input from user contains character other than
       the 26 alphabet
    """

def toOrdList(targetText):
    x = targetText.upper()
    x = list(x)
    y = []
    for z in x:
        y += [ord(z)]
    return y
    """ This method return list of uppercase ASCII number from given string
        i.e  : ('abc') => [65, 66, 67]
    """

def convOrd(stringOrd, key):
    m = []
    k = []
    for i in range(len(stringOrd)):
        m += [stringOrd[i]]
    for i in range(len(key)):
        k += [key[i]]
    for i in range(len(k)):
        k[i] -= 65
    chiperNumbers = []
    keyCounter = 0
    for i in range(len(m)):
        if m[i] != 32:
            m[i] -= 65
            c = (m[i]+k[keyCounter%len(k)]) % 26
            chiperNumbers += [c+65]
            keyCounter+=1
        else:
            chiperNumbers += [m[i]]
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

def enchiperNoSpace(someText):
    return someText.replace(' ','')
    """ This method returns given string without the space character
    """

def enchiperSpaceEveryFour(someText):
    nS = enchiperNoSpace(someText)
    eS = str('')
    counter = 0
    for x in nS:
        if counter != 0 and counter % 4 == 0:
            eS+=' '
        eS+=x
        counter+=1
    return eS
    """This method returns given string with it's original space character removed and insert
       space character every 4 letters
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

"""Below this comment is the main program of our group version of vignere chiper
"""
unaltered = textInput('Text ')

chiperKey = keyInput('Key  ')

print 'mode:'
print '1. Enchiper'
print '2. Dechiper\n'

mode = 0
while mode != 1 and mode != 2:
    mode = int(raw_input('Choose mode number: '))
    if mode != 1 and mode != 2: print 'Invalid mode. Try again...\n'


if mode == 1:
    print 'Enchiper output method:'
    print '1. Same spacing'
    print '2. No spacing'
    print '3. Space every 4 letters\n'
    method = 0
    while method != 1 and method != 2 and method != 3:
        method = int(raw_input('Choose enchiper output method: '))
        if method != 1 and method != 2 and method != 3: print 'Invalid method number. Try again...\n'
    print 'Plain text  :  %s' % (unaltered)
    if method == 1:
        print 'Chiper text : ', enchiper(unaltered, chiperKey)
    elif method == 2:
        print 'Chiper text : ', enchiperNoSpace(enchiper(unaltered, chiperKey))
    else:
        print 'Chiper text : ', enchiperSpaceEveryFour(enchiper(unaltered, chiperKey))
elif mode == 2:
    print 'Chiper Test : ', unaltered
    print 'Plain Text  : ', dechiper(unaltered, chiperKey)
else:
    print ('Wrong mode input. Program will now close')
    exit()