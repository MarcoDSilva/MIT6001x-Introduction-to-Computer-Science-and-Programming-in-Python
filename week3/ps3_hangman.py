# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

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

# end of helper code
# -----------------------------------

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
    tempWord = list(secretWord)
    
    for char in lettersGuessed:
        if char in tempWord:
            index = tempWord.index(char)
            del(tempWord[index])
    
    return not tempWord



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    tempWord = list(secretWord)
    
    # list comprehension, (false,true) [if this happened] 
    hiddenWord = [['_ ', char][char in lettersGuessed] for char in secretWord]
    
    return "".join(hiddenWord)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    letters = [char for char in string.ascii_lowercase 
               if char not in lettersGuessed]
    
    return "".join(letters)
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    availableLetters = getAvailableLetters('')
    hiddenWord = getGuessedWord(secretWord, lettersGuessed)    
    numberOfLetters = len(secretWord)
    mistakesMade = 8
    
    startGame(numberOfLetters)
    
    while mistakesMade > 0:
        printInfo(mistakesMade, availableLetters)
        guess = input('Please guess a letter: ')
        
        if guess not in secretWord and guess not in lettersGuessed:
            print('Oops! That letter is not in my word: ' + hiddenWord)
            lettersGuessed.append(guess)
            availableLetters = getAvailableLetters(lettersGuessed)
            mistakesMade -= 1
        else:
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter: " + hiddenWord)
            else:
                lettersGuessed.append(guess)
                hiddenWord = getGuessedWord(secretWord, lettersGuessed)  
                availableLetters = getAvailableLetters(lettersGuessed)
                print("Good guess: " + hiddenWord)
                
        if '_ ' not in hiddenWord:
            print('-----------')
            return 'Congratulations, you won!'
        
        if mistakesMade == 0:   
            print('-----------')
            return 'Sorry, you ran out of guesses. The word was ' + secretWord
            

def startGame(numberOfLetters):
     print('Welcome to the game, Hangman! \n'
          'I am thinking of a word that is ' + str(numberOfLetters) + 
          ' letters long.')

def printInfo(plays, availableLetters):
    print('-------------')
    print('You have ' + str(plays) + ' guesses left.')
    print('Available letters: ' + availableLetters)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
