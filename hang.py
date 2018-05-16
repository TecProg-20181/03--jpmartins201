import random
import string

WORDLIST_FILENAME = "words.txt"

class Hangman:

    def __init__(self, file_name='', attempts = 8):
        self.attempts = attempts
        self.lettersGuessed = []
        self.secretWord = ''
        self.loadWords()


    def checkDifferentLetters(self):
        letters = set()
        letters.update(self.secretWord)
        print 'The secret word has ', len(letters), 'equal letters!'

        return len(letters)

    def newWord(self, wordlist):
        while self.checkDifferentLetters() > self.attempts:
            self.secretWord = random.choice(wordlist)
            print 'A new word has been selected due to many different letters in the word! '

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """

        print "Loading word list from file..."

        inFile = open(WORDLIST_FILENAME, 'r', 0)# inFile: file
        line = inFile.readline()# line: string
        wordlist = string.split(line)# wordlist: list of strings

        print " ", len(wordlist), "words loaded."
        self.secretWord = random.choice(wordlist)
        self.newWord(wordlist)

    def isWordGuessed(self):
        self.secretLetters = []

        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False

        return True

    def getGuessedWord(self):
        guessed = ''
        return guessed

    def getAvailableLetters(self):

        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase
        return available

    def initialMessage(self):

        print 'Welcome to the game, Hangman!'
        print 'I am thinking of a word that is', len(self.secretWord), ' letters long.'
        print '-------------'

    def availableLetters(self,available):
        for letter in available:
            if letter in self.lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available

    def result(self):

        if self.isWordGuessed() == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of attempts. The word was', self.secretWord, '.'

    def checkGuessedLetter(self, letter):

        guessed = self.getGuessedWord()
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                guessed += letter
            else:
                guessed += '_'
        print guessed

    def gameEngine(self):

        while self.isWordGuessed() == False and self.attempts > 0:
            print 'You have ', self.attempts, 'attempts left.'

            available = self.getAvailableLetters()
            self.availableLetters(available)

            letter = raw_input('Please guess a letter: ')
            if letter in self.lettersGuessed:
                print 'Oops! You have already guessed that letter: '

            elif letter in self.secretWord:
                self.lettersGuessed.append(letter)


                print 'Good guess: '
            else:
                self.attempts -=1
                self.lettersGuessed.append(letter)
                print 'Oops! That letter is not in my word: '

            self.checkGuessedLetter(letter)
            print '------------'

        else:
            self.result()


if __name__ == "__main__":

    hangman = Hangman()
    hangman.initialMessage()
    hangman.gameEngine()
