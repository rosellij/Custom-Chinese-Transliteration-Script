import unidecode

def pinyintopersonal(inputsentence):

    inputsentence = [' ', ' ', ' '] + list(inputsentence) + [' ', ' ', ' ']

    for anyindex, anychar in enumerate(inputsentence):

        if type(anychar) == str and unidecode.unidecode(anychar) == 'a' and inputsentence[anyindex - 1] in ['i', 'y'] and inputsentence[anyindex + 1] == 'n' and inputsentence[anyindex + 2] != 'g':
            inputsentence[anyindex] = ('e', 'replaced')
        if type(anychar) == str and unidecode.unidecode(anychar) == 'a' and inputsentence[anyindex - 2] == 'y' and inputsentence[anyindex - 1] == 'u' and inputsentence[anyindex + 1] == 'n' and inputsentence[anyindex + 1] != 'g':
            inputsentence[anyindex] = ('e', 'replaced')
        if type(anychar) == str and unidecode.unidecode(anychar) == 'o' and inputsentence[anyindex - 1] in ['b', 'p', 'm', 'f', 'l'] and inputsentence[anyindex - 2] == ' ' and inputsentence[anyindex + 1] == ' ':
            inputsentence.insert(anyindex, ('u', 'inserted'))
        if type(anychar) == str and unidecode.unidecode(anychar) == 'e' and inputsentence[anyindex + 1] == 'n':
            inputsentence[anyindex] = ('ę', 'replaced')
        if type(anychar) == str and unidecode.unidecode(anychar) == 'u' and inputsentence[anyindex + 1] == 'n' and inputsentence[anyindex - 1] not in ['j', 'q', 'x', 'y']:
            inputsentence.insert(anyindex + 1, ('ę', 'inserted'))
        if type(anychar) == str and unidecode.unidecode(anychar) == 'i' and inputsentence[anyindex - 1] in ['z', 'c', 's', 'r']:
            inputsentence[anyindex] = ('į', 'replaced')
        if type(anychar) == str and unidecode.unidecode(anychar) == 'i' and inputsentence[anyindex - 2] in ['z', 'c', 's'] and inputsentence[anyindex - 1] == 'h':
            inputsentence[anyindex] = ('į', 'replaced')

    for anyindex, anychar in enumerate(inputsentence):

        if type(anychar) == str and anychar == 'b':
            inputsentence[anyindex] = ('p', 'replaced')
        if type(anychar) == str and anychar == 'p':
            inputsentence[anyindex] = ("p'", 'replaced')
        if type(anychar) == str and anychar == 'd':
            inputsentence[anyindex] = ('t', 'replaced')
        if type(anychar) == str and anychar == 't':
            inputsentence[anyindex] = ("t'", 'replaced')
        if type(anychar) == str and anychar == 'z' and inputsentence[anyindex + 1] != 'h':
            inputsentence[anyindex] = ('ts', 'replaced')
        if type(anychar) == str and anychar == 'c' and inputsentence[anyindex + 1] != 'h':
            inputsentence[anyindex] = ("ts'", 'replaced')
        if type(anychar) == str and anychar == 'r' and inputsentence[anyindex - 1] != 'e' and inputsentence[anyindex + 1] != ' ':
            inputsentence[anyindex] = ('zh', 'replaced')
        if type(anychar) == str and anychar == 'j':
            inputsentence[anyindex] = ('hch', 'replaced')
        if type(anychar) == str and anychar == 'q':
            inputsentence[anyindex] = ("hch'", 'replaced')
        if type(anychar) == str and anychar == 'x':
            inputsentence[anyindex] = ('hsh', 'replaced')
        if type(anychar) == str and anychar == 'g' and inputsentence[anyindex - 1] != 'n':
            inputsentence[anyindex] = ('k', 'replaced')
        if type(anychar) == str and anychar == 'k':
            inputsentence[anyindex] = ("k'", 'replaced')
        if type(anychar) == str and anychar == 'z' and inputsentence[anyindex + 1] == 'h':
            inputsentence[anyindex] = ('c', 'replaced')
        if type(anychar) == str and anychar == 'c' and inputsentence[anyindex + 1] == 'h':
            inputsentence[anyindex] = ("c", 'replaced')
            inputsentence.insert(anyindex + 2, ("'", 'inserted'))

    for anyindex, anychar in enumerate(inputsentence):

        if type(anychar) == str and unidecode.unidecode(anychar) == 'e' and inputsentence[anyindex + 1] == ' ':
            inputsentence[anyindex] = ("ę", 'replaced')
        if type(anychar) == str and anychar == 'r' and inputsentence[anyindex - 1] == 'e' and inputsentence[anyindex + 1] == ' ':
            inputsentence[anyindex - 1] = ('a', 'replaced')
        if type(anychar) == str and anychar == 'y':
            inputsentence[anyindex] = ('', 'replaced')
        if type(anychar) == str and anychar == 'u' and inputsentence[anyindex - 1] == 'w':
            inputsentence[anyindex - 1] = ('', 'replaced')

    return ''.join([unidecode.unidecode(anyentry) if type(anyentry) == str else anyentry[0] for anyentry in inputsentence]).strip(' ')