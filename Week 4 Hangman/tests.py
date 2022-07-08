import unittest
from main import PrintString,GuessCheck

class TestPrintString(unittest.TestCase):
    def test_initialPrint(self):
        printString = PrintString()
        self.assertEqual( printString.initialPrint("") , [] , "The dashed string is not of same length as input word" )
        self.assertEqual( printString.initialPrint("abcd") , ['_','_','_','_'] , "The dashed string is not of same length as input word" )
    
    def test_correctGuess(self):
        printString = PrintString()
        self.assertEqual( printString.correctGuess( ['a','b'] , "abcd" ) , ['a','b','_','_'] )

class TestGuessCheck(unittest.TestCase):
    def test_alreadyGuessedChar(self):
        guessCheck = GuessCheck()
        
        guessCheck.correctGuesses.append('a')
        guessCheck.correctGuesses.append('b')
        guessCheck.incorrectGuesses.append('c')
        guessCheck.incorrectGuesses.append('d')

        self.assertEqual(guessCheck.alreadyGuessedChar('e'),False)
        self.assertEqual(guessCheck.alreadyGuessedChar('a'),True)
        
    def test_isCorrect(self):
        guessCheck = GuessCheck()

        self.assertEqual(guessCheck.isCorrect('e','abcd') , False)
        self.assertEqual(guessCheck.isCorrect('a','abcd') , True)

    def test_wordGuessed(self):
        guessCheck = GuessCheck()

        self.assertEqual(guessCheck.wordGuessed(["a","b"] ,"ab" ) , True)
        self.assertEqual(guessCheck.wordGuessed(["a","b"] ,"ac" ) , False)

unittest.main()

