import unittest
from main import PrintString

class TestPrintString(unittest.TestCase):
    
    def test_initialPrint(self):
        printString = PrintString()
        self.assertEqual( printString.initialPrint("") , [] , "The dashed string is not of same length as input word" )
        self.assertEqual( printString.initialPrint("abcd") , ['_','_','_','_'] , "The dashed string is not of same length as input word" )
    
    def test_correctGuess(self):
        printString = PrintString()
        self.assertEqual( printString.correctGuess( ['a','b'] , "abcd" ) , ['a','b','_','_'] )


