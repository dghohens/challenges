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
    draw = []
    for i in range(NUM_LETTERS):
        draw.append(POUCH[random.randrange(0,97)])
    hand = tuple(draw)
    return hand

'''def load_words():
    wholefile = open(DICTIONARY)
    allWords = wholefile.readlines()
    wholefile.close()
    print('file opened')
    return allWords
'''


def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    val = 0
    for i in word.upper():
        if i == '\n' or i == '-':
            break
        else:
            val = val + LETTER_SCORES[i]
    return val

def max_word_value(wordset):
    """Checks the maximum word value"""
    wordVals = {}
    highestVal = 0
    highestWord = ''
    for i in wordset:
        singleVal = calc_word_value(i)
        if singleVal > highestVal:
            highestVal = singleVal
            highestWord = i
        wordVals[i]=singleVal
    return (highestWord, highestVal)


def validate_user_input(userWord, hand):
    """Validates that the user entered valid letters and a valid word."""
    validInput = True
    validWord = True
    handCheck = list(hand)
    for i in userWord:
        if i not in handCheck:
            validInput = False
        else:
            del handCheck[handCheck.index(i)]
    if userWord.lower() not in DICTIONARY:
        validWord = False
    return (validInput, validWord)


def permute_and_check(hand):
    """Permute over every possible combination of letters, starting with 1 letter and going up to 7.
    Check each iteration to make sure it's a valid word, return a list of only valid words.
    Seems to only run against the last 1-3 letters right now, need to debug this section."""
    possibleWords = []
    for i in range(1, 8):
        j = []
        j = list(permutations(hand, i))
        for k in j:
            m = ''.join(k)
            if m.lower() in DICTIONARY and m.upper not in possibleWords:
                possibleWords.append(m)
    return possibleWords


def main():
    """Where the magic happens. This just pulls in every other function to run the game."""
    hand = letter_draw()

    print('Letters Drawn: ' + ', '.join(hand))

    userWord = input('Form a valid word: ')

    if False in validate_user_input(userWord.upper(), hand):
        print('Please enter a valid input next time.')

    userVal = calc_word_value(userWord)
    print('Word chosen: ' + userWord + ' (value: ' + str(userVal) + ')')

    possibleWords = permute_and_check(hand)
    bestWord, bestVal = max_word_value(possibleWords)
    print('Optimal word possible: ' + bestWord + ' (value: ' + str(bestVal) + ')')

    print('You scored: ' + str(userVal/bestVal))
    pass

if __name__ == "__main__":
    main()