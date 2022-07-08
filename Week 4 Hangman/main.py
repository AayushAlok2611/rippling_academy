# def getRandomWord():
#     ''' 
#     Generate a random word from SOWPODS 
#     Return a list of chars i.e the random word
#     '''

# def generateMap(word):
#     '''
#     Accepts string and genrate a dictionary of lists
#     with key as letter and value as a list of indices at which the letter appears in the provided string
#     '''
#     map = {}
#     for i in range(len(word)):
#         if word[i] in map:
#             map[word[i]].append(i)
#         else:
#             map[word[i]] = [i]
#     return map

# def modifyStr(s,guess,map):
#     ''' 
#     Modify the list of char that will be printed everytime 
#     Returns a list of chars i.e the modified string that will be printed to the console
#     '''
#     s1 = s
#     for idx in map[guess]:
#         s1[idx] = guess
#     return s1

# if __name__ == "__main__":
#     # word = getRandomWord()
#     word = ['a','b','c','a']
#     map = generateMap(word)
#     s = ['_ ' for i in range(len(word))]
#     guessCount  = 6
#     guessedChars = []

#     print(s)

#     guessed = False

#     while guessCount > 0:
#         guess = input("Guess a character  ")

#         if len(guess) > 1:
#             guess = input("Guess only single characters,no strings ")

#         #check if already guessed this char or not
#         if guess in guessedChars:
#             print("Already guessed this char")
#             continue
#         else:
#             guessedChars.append(guess)
#             guessCount-=1

#         if guess in word:
#             s = modifyStr(s,guess,map)
#             print(s)
#         else:
#             print("Incorrect")
        
#         if(s==word):
#             guessed = True
#             print("You got it")
#             break
    
#     if not guessed:
#         print('Out of guesses')

defaultGuessCount = 6

class RandomWordGenerator:
    def generate(self) -> str:
        return "abca"

class GuessCount:
    def generate(self) -> int:
        return defaultGuessCount

class User:
    def enterInput(self) -> str:
        s = input("Guess an alphabet ")
        while(len(s)==0 or len(s) > 1 or not(s[0]>='a' and s[0]<='z') or not (s[0]>='a' and s[0]<='z') ):
            s = input("Enter a single alphabet ")
        return s
    
class GuessCheck:
    def __init__(self) -> None:
        self.correctGuesses = [] #list of chars
        self.incorrectGuesses = [] #list of chars

    def alreadyGuessedChar(self,guess) -> bool:
        if ( guess in self.correctGuesses ):
            return True
        if ( guess in self.incorrectGuesses ):
            return True
        return False
    
    def isCorrect(self,guess,word) -> bool:
        if guess in word:
            return True
        return False
    
    def wordGuessed(self,partialGuessedString,word) -> bool:
        return ( "".join(self._partialGuessedString) == self._word )


class PrintString:
    def initialPrint(self,word) -> list[str]:
        lst = []
        for i in range(len(word)):
            print("_",end=" ")
            lst.append('_ ')
        print("")
        return lst

    def alreadyGuessedChar(self) -> None:
        print("Already guessed this char")
    
    def correctGuess(self,correctGuesses,word) -> list[str]:
        lst = []
        for i in range(len(word)):
            if (word[i] in correctGuesses):
                print(word[i],end=" ")
                lst.append(word[i])
            else:
                print("_",end=" ")
                lst.append('_')
        print("")
        return lst
    
    def incorrectGuess(self) -> None:
        print("Incorrect")

class Game:
    
    def __init__(self) -> None:
        self._printString = PrintString()
        self._guessCheck = GuessCheck()
        self._guessCount = GuessCount().generate()
        self._word = RandomWordGenerator().generate()
        self._wordGuessed = False
        self._user = User()
        self._partialGuessedString = []

    def play(self) -> None:
        
        #initial print of dashed string
        self._partialGuessedString  = self._printString.initialPrint(self._word)

        while(self._guessCount > 0):

            guess = self._user.enterInput()
            
            if ( self._guessCheck.alreadyGuessedChar(guess) ):
                self._printString.alreadyGuessedChar()
                continue
            
            self._guessCount -= 1
            if ( self._guessCheck.isCorrect(guess,self._word) ):
                self._guessCheck.correctGuesses.append(guess)
                self._partialGuessedString  =  self._printString.correctGuess(self._guessCheck.correctGuesses,self._word)
            else:
                self._guessCheck.incorrectGuesses.append(guess)
                self._printString.incorrectGuess()
                print(f"You have {self._guessCount} guesses left")

            
                self._wordGuessed = self._guessCheck.wordGuessed(self._partialGuessedString,self._word)

                if self._wordGuessed:
                    print("You guessed the word")
                    break
        
        if not self._wordGuessed:
            print("Out of Guesses")
            print("The word was ",self._word)
        
        newGame = input("Type y for new game , else n for end ->  ")
        if newGame == 'y':
            self.play()
       

if __name__ == "__main__":
    Game().play()


