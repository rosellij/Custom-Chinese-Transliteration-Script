from unidecode import unidecode

def parsePinyinSyllables(inputphrase):

    inputphrase = inputphrase.lower()

    syllablelist = []
    currentsyllable = ''
    initiallist = ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'z', 'c', 's', 'zh', 'ch', 'sh', 'r', 'w', 'y']
    glidelist = []
    vowellist = ['a', 'o', 'e', 'i', 'u', 'ü']
    codalist = ['n', 'ng']

    syllabool = False

    counter = 0

    while counter < len(inputphrase):

        if inputphrase[counter] in initiallist:

            if inputphrase[counter] in ['s', 'z', 'c'] and inputphrase[counter + 1] == 'h':

                currentsyllable += inputphrase[counter] + inputphrase[counter + 1]
                syllabool = True
                counter += 1

            else:

                currentsyllable += inputphrase[counter]
                syllabool = True

        if unidecode(inputphrase[counter]) in vowellist:

            currentsyllable += inputphrase[counter]
            syllabool = True

        if inputphrase[counter] not in initiallist and unidecode(inputphrase[counter]) not in vowellist:

            counter += 1

        while syllabool == True:

            if 'subcounter' not in locals():
                
                subcounter = 1

            if counter + subcounter <= len(inputphrase) - 1 and unidecode(inputphrase[counter + subcounter]) in vowellist:

                currentsyllable += inputphrase[counter + subcounter]
                subcounter += 1

                if counter + subcounter <= len(inputphrase) - 1 and inputphrase[counter + subcounter] != 'n' and unidecode(inputphrase[counter + subcounter]) not in vowellist:

                    syllablelist += [currentsyllable]
                    
                    if unidecode(currentsyllable[-1]) not in vowellist:

                        counter += subcounter + 1

                    elif unidecode(currentsyllable[-1]) in vowellist:

                        counter += subcounter

                    currentsyllable = ''
                    subcounter = 1
                    syllabool = False
                    break

            if counter + subcounter <= len(inputphrase) - 1 and inputphrase[counter + subcounter] in codalist:

                if counter + subcounter <= len(inputphrase) - 2 and inputphrase[counter + subcounter + 1] == 'g':

                    currentsyllable += inputphrase[counter + subcounter] + inputphrase[counter + subcounter + 1]
                    syllablelist += [currentsyllable]
                    currentsyllable = ''
                    counter += subcounter + 2
                    subcounter = 1
                    syllabool = False
                    break

                else:

                    currentsyllable += inputphrase[counter + subcounter]
                    syllablelist += [currentsyllable]
                    currentsyllable = ''
                    counter += subcounter + 1
                    subcounter = 1
                    syllabool = False
                    break

    return ' '.join(syllablelist)