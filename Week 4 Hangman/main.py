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
    @classmethod
    def generate(cls):
        return "abca"

class GuessCount:
    @classmethod
    def generate(cls,word):
        return defaultGuessCount

class User:
    @classmethod
    def enterInput(cls):
        return input("Guess a character ")

class GuessCheck:
    correctGuesses = [] #list of chars
    incorrectGuesses = [] #list of chars

    @classmethod
    def alreadyGuessedChar(cls,guess):
        if ( guess in cls.correctGuesses ):
            return True
        if ( guess in cls.incorrectGuesses ):
            return True
        return False
    
    @classmethod
    def isCorrect(cls,guess,word):
        if guess in word:
            return True
        return False

class PrintString:
    @classmethod
    def initialPrint(cls,word):
        lst = []
        for i in range(len(word)):
            print("_",end=" ")
            lst.append('_ ')
        print("")
        return lst

    @classmethod
    def alreadyGuessedChar(cls):
        print("Already guessed this char")
    
    @classmethod
    def correctGuess(cls,correctGuesses,word):
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
    
    @classmethod
    def incorrectGuess(cls):
        print("Incorrect")

class Game:
    word = RandomWordGenerator.generate()
    guessCount = GuessCount.generate(word)
    wordGuessed = False
    partialGuessedString = []
    def __init__(self) -> None:
        pass
    
    @classmethod
    def play(cls):
        
        #initial print of dashed string
        cls.partialGuessedString  = PrintString.initialPrint(cls.word)

        while(cls.guessCount > 0):
            guess = User.enterInput()
            if ( GuessCheck.alreadyGuessedChar(guess) ):
                PrintString.alreadyGuessedChar()
                continue
            cls.guessCount -= 1
            if ( GuessCheck.isCorrect(guess,cls.word) ):
                GuessCheck.correctGuesses.append(guess)
                cls.partialGuessedString  =  PrintString.correctGuess(GuessCheck.correctGuesses,cls.word)
            else:
                GuessCheck.incorrectGuesses.append(guess)
                PrintString.incorrectGuess()
                print(f"You have {cls.guessCount} guesses left")
            if ( "".join(cls.partialGuessedString) == cls.word ):
                cls.wordGuessed = True
                print("You guessed the word")
                break
        
        if not cls.wordGuessed:
            print("Out of Guesses")
       

if __name__ == "__main__":
    Game.play()


