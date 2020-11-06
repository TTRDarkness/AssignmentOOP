#importing assests
import random
import sys
import os


#Custom Exceptions
class InvalidChoiceError(Exception):
    pass

class InvalidGuessError(Exception):
    pass

class InvalidCodeError(Exception):
    pass

#Non class functions
def StringConverter(org_list, seperator=''):
    return seperator.join(org_list)

def ScreenClear():
    #clear function that works on Mac, Linux and Windows
    if os.name == 'posix':
      _ = os.system('clear')
    else:
        _ = os.system("cls")

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
                feedback.append(" ")
            k = k+1
            index = 0
        #Converts list to string

        feedbackStr = StringConverter(feedback)

        #Returning the results

        if feedbackStr == "    ":
            return "No feedback Given"
        else:
            return feedbackStr
        

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

    def MakeCode(self):
        codeGen = input("")
        if len(codeGen) < 4:
            raise InvalidCodeError("Code must be 4 digits long.")
        else:   
            codeGen = list(codeGen)
            return codeGen



class CodeBreaker(Player):
    def __init__(self, playerNumber, name):
        super().__init__(playerNumber, name)
    
    def makeAttempt_AI(self):
        guess = input("")
        guess = guess.upper()
        playerCode = list(guess)
        if len(playerCode) < 4:
            raise InvalidGuessError("A four digit code is required.")
        else:
            playerFeedback = Board().codeCheck(playerCode)
            if playerFeedback == "BBBB":
                Original_AI().GameWin()
            else:
                print(playerFeedback)
            Original_AI.attempt = Original_AI.attempt + 1

    def makeAttempt(self):
        guess = input("")
        guess = guess.upper()
        playerCode = list(guess)
        if len(playerCode) < 4:
            raise InvalidGuessError("A four digit code is required.")
        else:
            playerFeedback = Board().codeCheck(playerCode)
            if playerFeedback == "BBBB":
                Original().GameWin()
            else:
                print(playerFeedback)
            Original.attempt = Original.attempt + 1

    
#Main Menu
#Parent Class
class Mastermind:
    def play(self):
        print ("Would you like to")
        print ("(p)lay")
        print("(q)uit")
        print("")
        playChoice = input("")
        playChoice = playChoice.upper()
        if  playChoice == "P":
            pass
        elif playChoice == "Q":
            Mastermind.GameQuit
        else:
            raise InvalidChoiceError("Please choice either play or quit")
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
        print ("    (C) Matsermind44 for 2-4 players (Not Working)")


        gameTypeChoice = input("Enter A, B or C to continue:")
        gameTypeChoice = gameTypeChoice.upper()
        if gameTypeChoice == "A":
            Original().play()
        elif gameTypeChoice == "B":
            Original_AI().play()
        elif gameTypeChoice == "C":
            Mastermind44().play()
        else:
            raise InvalidChoiceError("Only select A, B or C")

    def GameWin(self):
        pass

    def GameQuit(self):
        print("Goodbye!")
        sys.exit(0)
  

#Child Classes
class Mastermind44(Mastermind):
    pass


class Original(Mastermind):
    totalAttempts = 12
    attempt = 1
    def play(self):
        #Setting up the code maker
        playerNumber = 1
        name = input("Player " + str(playerNumber) + ": What is your name?")
        print ("Welcome " + name + ". You can now generate the code. Please enter below a 4 letter combination of [B]lack, B[l]ue, [Y]ellow, [G]reen, [W]hite, [R]ed")

        codeInit = CodeMaker(playerNumber, name).MakeCode()
        print(codeInit)

        print("Enter the same code again")
        codeConfirm = CodeMaker(playerNumber, name).MakeCode()
        #checking if the codes match
        if codeInit == codeConfirm:
            for index in range(0, len(codeConfirm)):
                Board().codeAdd(codeConfirm[index])

            print(currentCode)
            print("code stored successfully")
            #clearing the screen for when player 2 must guess

            input("Press any key to clear code and continue")
            ScreenClear()
            #setting up player 2
            playerNumber = 2
            name = input("Player " + str(playerNumber) + ": What is your name?")
            print("")
            print("Welcome "+ name + ". You can now start by guessing the code. Please enter below a 4 letter combination of [B]lack, B[l]ue, [Y]ellow, [G]reen, [W]hite, [R]ed")
            while Original().attempt <= Original().totalAttempts:
                print("Attempt #" + str(Original().attempt))
                print("Enter your guess in the space below:")
                print("")
                CodeBreaker(playerNumber, name).makeAttempt()
                Original().attempt = Original().attempt + 1
        else:
            raise InvalidCodeError("Codes do not match")
            
    def GameQuit(self):
        print("Goodbye!")
        sys.exit(0)

    def GameWin(self):
        print ("")
        print ("Well done!")
        print ("You cracked the code in " + str(Original.attempt) + " attempt(s)")

        playAgain = input ("Would you like to play again? (y/n)")
        playAgain = playAgain.upper()
        if playAgain == "Y":
            Original.attempt = 1
            Board().BoardClear()
            ScreenClear()
            Mastermind().play()
        elif playAgain == "N":
            Original_AI().GameQuit()
        else:
            raise InvalidChoiceError("Only y or n is accepted")
        


class Original_AI(Mastermind):
    totalAttempts = 12
    attempt = 1
    def play(self):

        #Generating random code
        index = 1
        
        while index <= 4:
            codeColour = CodePegs.codePegs[random.randint(0, 5)]
            Board().codeAdd(codeColour)
            index = index +1

        #Player name generation and prompt
        playerNumber = 1
        name = input("Player " + str(playerNumber) + ": What is your name?")
        print("")
        print("Welcome "+ name + ". You can now start by guessing the code. Please enter below a 4 letter combination of [B]lack, B[l]ue, [Y]ellow, [G]reen, [W]hite, [R]ed")
        while Original_AI().attempt <= Original_AI().totalAttempts:
            print("Attempt #" + str(Original_AI().attempt))
            print("Enter your guess in the space below:")
            print("")
            CodeBreaker(playerNumber, name).makeAttempt_AI()
            Original_AI().attempt = Original_AI().attempt + 1

    def GameQuit(self):
        print("Goodbye!")
        sys.exit(0)

    def GameWin(self):
        print ("")
        print ("Well done!")
        print ("You cracked the code in " + str(Original_AI.attempt) + " attempt(s)")

        playAgain = input ("Would you like to play again? (y/n)")
        playAgain = playAgain.upper()
        if playAgain == "Y":
            Original_AI.attempt = 1
            Board().BoardClear()
            ScreenClear()
            Mastermind().play()
        elif playAgain == "N":
            Original().GameQuit()
        else:
            raise InvalidChoiceError("Only y or n is accepted")

m = Mastermind()
m.play()

