#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
from itertools import permutations

random.seed(version=2)
NUM_LETTERS = 7

def letter_draw():
    """Draw the number of letters at random, return a list of numbers.
    Note that this doesn't check for duplicates, so someone could end up with 2 Js or 2 Qs.
    I might fix that later if I'm feeling up to it."""
    hand = []
    for i in range(NUM_LETTERS):
        hand.append(POUCH[random.randrange(0,97)]
    return hand

def load_words():
    '''Load in all words from the dictionary.
    allwords returns a list. This was reused from challenge 1'''
    wholefile = open(DICTIONARY)
    allwords = wholefile.readlines()
    wholefile.close()
    print('file opened')
    return allwords

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    val = 0
    for i in word.upper():
        if i == '\n' or i == '-':
            break
        else:
            val = val + LETTER_SCORES[i]
    print(word + ' = ' + str(val))
    return val

# re-use from challenge 01
def max_word_value(words):
    """Checks the maximum word value, need to fix the allwords reference"""
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

def validate_user_input(userWord,hand,allwords):
    """Validates that the user entered valid letters and a valid word"""
    validInput = True
    validWord = True
    for i in userWord:
        if i not in hand:
            validInput = False
        else:
            del hand[hand.index(i)]
    if userWord not in allwords:
        validWord = False
    return (validInput, validWord)


def permute_and_check(userWord, hand, allwords):
    """Permute over every possible combination of letters, starting with 1 letter and going up to 7.
    Check each iteration to make sure it's a valid word, return a list of only valid words."""
    possibleWords = []
    for i in range(1, NUM_LETTERS + 1):
        j = list(permutations(hand[0:i],i))




def main():
    """Where the magic happens. This just pulls in every other function to run the game."""
    allwords = load_words()
    hand = letter_draw()
    print('Letters Drawn: ' + ', '.join(hand))
    userWord = input('Form a valid word: ')
    userWord = userWord.upper()
    if False in validate_user_input(userWord, hand, allwords):
        print('Please enter a valid input next time.')
    userVal = calc_word_value(userWord)
    print('Word chosen: ' + userWord + ' (value: ' + str(userVal) + '')

    pass