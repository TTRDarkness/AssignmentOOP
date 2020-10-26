#importing assests
import random

#Adding base classes to Assignment


#Game Classes
class Board:
    currentCode = {}
    
    def codeAdd(self, code, position):
        #Adding the generated code to a dictionary
        Board.currentCode[position] = code

    def codeCheck(self):
        global feedback
        feedback = []
        #Creating a method for checking the guesses





class KeyPegs:
    pass

class CodePegs:
    #Code peg list setup
    codePegs = ["R", "G", "L", "Y", "B", "W"] 

class CodeCounters:
    pass

#Parent Class
class Player:
    def __init__(self, playerNumber, name):
        self.playerNumber = playerNumber
        self.name = name
    
#Child Classes
class CodeMaker(Player):
    def __init__(self, playerNumber, name):
        super().__init__(playerNumber, name)


class CodeBreaker(Player):
    def __init__(self, playerNumber, name):
        super().__init__(playerNumber, name)
        print("Welcome "+ self.name + ". You can now start by guessing the code")
    
    def makeAttempt_AI(self):
        global playerCode
        #First loop to go through all of the attempts
        while Original_AI.attempt <= Original_AI.totalAttempts:
            print("Enter your guess in the space below:")
            print("Attempt #" + str(Original_AI.attempt))
            guess = input("")
            playerGuess = list(guess)
            index2 = 0

            #Second loop to convert the user input into a dictionary
            playerCode = {}
            while index2 < len(playerGuess):
                playerCode[index2+1] = playerGuess[index2]
                index2 = index2+1
            print(playerCode)
            #Board.codeCheck(self)
            Original_AI.attempt = Original_AI.attempt + 1
            #print(feedback)

    
    
#Main Menu
#Parent Class
class Mastermind:
    def play(self):
        #Text block for user-interface
        print("Welcome to Mastermind!")
        print("Developed by Adam Chandler")
        print("COMP 1046 Object-Orientated Programming")
        print("")
        print("")
        print("Select which Game you want to play")
        print ("    (A) Original Mastermind for 2 players")
        print ("    (B) Original Mastermind for 1 player")
        print ("    (C) Matsermind44 for 2-4 players")

        #Add Exception Handling later
        gameTypeChoice = input("Enter A, B or C to continue:")
        gameTypeChoice = gameTypeChoice.upper()
        
        if gameTypeChoice == "A":
            Original()
        elif gameTypeChoice == "B":
            Original_AI().play()
        elif gameTypeChoice == "C":
            Mastermind44()

        #To be created and added later
        #else:
            #raise InvalidChoice Error

    
    def GameQuit(self):
        pass
  

#Child Classes
class Mastermind44(Mastermind):
    pass


class Original(Mastermind):
    pass

class Original_AI(Mastermind):
    totalAttempts = 6
    attempt = 1
    def play(self):

        #Generating random code
        index = 1
        while index <= 4:
            codeColour = CodePegs.codePegs[random.randint(0, 5)]
            Board.codeAdd(self, codeColour, index)
            index = index +1
        #Remove this before final test
        print(Board.currentCode)

        #Player name generation and prompt
        playerNumber = 1
        name = input("Player " + str(playerNumber) + ": What is your name?")
        CodeBreaker(playerNumber, name).makeAttempt_AI()

        
    
    def GameQuit(self):
        print("Goodbye!")

m = Mastermind()
m.play()


