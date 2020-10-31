#importing assests
import random
import sys

#Custom Exceptions
class InvalidChoiceError(Exception):
    pass

class InvalidGuessError(Exception):
    pass

#Adding base classes to Assignment


#Game Classes
class Board:
    def BoardClear(self):
        global currentCode
        currentCode = []
        

    
    def codeAdd(self, code):
        #Adding the generated code to a list
        currentCode.append(code)
    

    def codeCheck(self, playerCode):
        feedback = []

        #Loops for setting up the feedback
        index = 0
        k = 0
        while k <=3:
            while index <= 3:
                flag = 0
                if playerCode[k] == currentCode[index]:
                    if index == k:
                        feedback.append("B")
                        index = 4
                        flag = 1
                    else:

                        #Checking for repeats in the code
                        index = k
                        if playerCode[k] == currentCode[index]:
                            feedback.append("B")
                            index = 4
                            flag = 1
                        else:
                            feedback.append("W")
                            index = 4
                            flag =1
                else:
                    index = index+1     
            if flag == 0:
                feedback.append("")
            k = k+1
            index = 0

        #Returning the results
        if feedback == ["", "", "", ""]:
            return "No feedback Given"
        elif feedback == ["B", "B", "B", "B"]:
            Original_AI.GameWin(self)

        else: 
            return feedback
        


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
            guess = guess.upper()
            playerCode = list(guess)
            if len(playerCode) < 4:
                raise InvalidGuessError("A four digit code is required")
            else:
                print(Board().codeCheck(playerCode))
                Original_AI.attempt = Original_AI.attempt + 1

    
#Main Menu
#Parent Class
class Mastermind:
    def play(self):
        Board().BoardClear()
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


        gameTypeChoice = input("Enter A, B or C to continue:")
        gameTypeChoice = gameTypeChoice.upper()
        
        if gameTypeChoice == "A":
            Original()
        elif gameTypeChoice == "B":
            Original_AI().play()
        elif gameTypeChoice == "C":
            Mastermind44()
        else:
            raise InvalidChoiceError("Only select A, B or C")


    def GameWin(self):
        pass

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
            Board().codeAdd(codeColour)
            index = index +1

        print(currentCode)

        #Player name generation and prompt
        playerNumber = 1
        name = input("Player " + str(playerNumber) + ": What is your name?")
        CodeBreaker(playerNumber, name).makeAttempt_AI()

        
    
    def GameQuit(self):
        print("Goodbye!")
        sys.exit(0)

    def GameWin(self):
        print ("")
        print ("Well done!")
        print ("You cracked the code in " + str(Original_AI.attempt) + " attempt(s)")

        #Add exception handling later to this
        playAgain = input ("Would you like to play again? (y/n)")
        playAgain = playAgain.upper()
        if playAgain == "Y":
            Original_AI.attempt = 1
            Board().BoardClear()
            Mastermind().play()
        elif playAgain == "N":
            Original_AI().GameQuit()
        else:
            raise InvalidChoiceError("Only y or n is accepted")

    

m = Mastermind()
m.play()


