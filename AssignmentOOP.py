#importing assests
import random

#Adding base classes to Assignment


#Game Classes
class Board:
    def __init__(self, code):
        currentCode = []
        self.currentCode = currentCode
        self.code = code
    
    def codeAdd(self, code):
        self.currentCode.append(self.code)

class KeyPegs:
    pass

class CodePegs:
    codePegs = ["R", "B", "Y", "G", "l", "W"]

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
    
    def makeAttempt(self):
            while Original_AI.attempt <= Original_AI.totalAttempts:
                print("Enter your guess in the space below:")
                print("Attempt #" + Original_AI.attempt)
                guess = input("")
    
    
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
        index = 0
        while index < 4:
            codeColour = CodePegs.codePegs[random.randint(0, 5)]
            Board.codeAdd(codeColour)
            index = index +1

        #Player name generation and prompt
        playerNumber = 1
        name = input("Player " + str(playerNumber) + ": What is your name?")
        CodeBreaker(playerNumber, name)
    
    def GameQuit(self):
        print("Goodbye!")

m = Mastermind()
m.play()


