from data import DICTIONARY, LETTER_SCORES

def load_words():
    '''Load in all words from the dictionary.
    allwords returns a list'''
    wholefile = open(DICTIONARY)
    allwords = wholefile.readlines()
    wholefile.close()
    print('file opened')
    return allwords

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    val = 0
    for i in word.upper():
        if i == '\n' or i == '-':
            break
        else:
            val = val + LETTER_SCORES[i]
    print(word + ' = ' + str(val))
    return val

def max_word_value(allwords):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    wordVals = {}
    highestVal = 0
    highestWord = ''
    for i in allwords:
        singleVal = calc_word_value(i)
        if singleVal > highestVal:
            highestVal = singleVal
            highestWord = i
        wordVals[i]=singleVal
    return highestWord

print(max_word_value(load_words()))
