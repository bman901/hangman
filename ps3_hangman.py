# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def numplayers():
    players = int(input('Enter 1 to play against the computer, or 2 to play against another local player: '))
    return players

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guessed = False
    
    for char in secretWord:
        if char in lettersGuessed:
            guessed = True
        else:
            guessed = False
            break
    
    return guessed


def isLetterGuessed(secretWord, guess):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guessed = False
    
    for char in secretWord:
        if char == guess:
            guessed = True
            break
        else:
            guessed = False
    
    return guessed


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    GuessedWord = ''
    
    for char in secretWord:
        if char in lettersGuessed:
            GuessedWord += char + ' '
        else:
            GuessedWord += '_ '
    
    return GuessedWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    
    AvailableLetters = ([*string.ascii_lowercase])
    
    for char in lettersGuessed:
        if char in AvailableLetters:
            AvailableLetters.remove(char)
    
    return ''.join(AvailableLetters)
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Asks the user to supply one guess (i.e. letter) per round.
    '''
    
    secretWordlength = len(secretWord)
    guessesLeft = 8
    lettersGuessed = []
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(secretWordlength) + ' letters long.')
    
    while guessesLeft > 0:
        print ('-----------')
        if isWordGuessed(secretWord,lettersGuessed):
            print('Congratulations, you won!')
            break
        else:
            print ('You have ' + str(guessesLeft) + ' guesses left.')
            print ('Available letters: ' + getAvailableLetters(lettersGuessed))
            guess = input('Please guess a letter: ').lower()
            if guess in lettersGuessed:
                print('Oops! You'"'ve already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            elif isLetterGuessed(secretWord, guess):
                lettersGuessed.append(guess)
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(guess)
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                guessesLeft -= 1
     
    if guessesLeft == 0:
        print ('-----------')
        print ('Sorry, you ran out of guesses. The word was ' + str(secretWord + ' .'))
    


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
