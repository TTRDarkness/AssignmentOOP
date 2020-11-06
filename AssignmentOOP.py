import random
import sys
import os


class InvalidChoiceError(Exception):
    """Custom Exception for game selection"""
    pass

class InvalidGuessError(Exception):
    """Custom Exception for guess attempts made by the CodeBreaker"""
    pass

class InvalidCodeError(Exception):
    """Custom Exception for code made by the CodeMaker"""
    pass

def StringConverter(org_list, seperator=''):
    """Function that allows lists to be converted to strings
    org_list is the list that is to be converted """
    return seperator.join(org_list)

def ScreenClear():
    """Allows the screen to be cleared between players and after each game
    takes no arguments """
    if os.name == 'posix':
      _ = os.system('clear')
    else:
        _ = os.system("cls")


class Board:
    """The Board stores the current code and runs the feedback"""
    def BoardClear(self):
        """This function takes no paramters and clears the current code list"""
        global currentCode
        currentCode = []

    
    def codeAdd(self, code):
        """This function adds code to the current code, it takes a single parameter of code """

        currentCode.append(code)
    

    def codeCheck(self, playerCode):
        """This function takes a single parameter of playerCode and checks if the code matches the current code on the board
        it will then display feedback to the screen depending on the colour and position of the guess made by the CodeBreaker"""
        feedback = []
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

        feedbackStr = StringConverter(feedback)


        if feedbackStr == "    ":
            return "No feedback Given"
        else:
            return feedbackStr
        

class CodePegs:
    """This class creates a list that is accessed by the random code generation is the Original_AI Class"""
    codePegs = ["R", "G", "L", "Y", "B", "W"] 


class Player:
    """This is a parent class of both CodeBreaker and CodeMaker, two parameters must be passed PlayerNumber and name"""
    def __init__(self, playerNumber, name):
        self.playerNumber = playerNumber
        self.name = name

class CodeMaker(Player):
    """This class is responsible for the generation of the code in Original"""
    def __init__(self, playerNumber, name):
        super().__init__(playerNumber, name)

    def MakeCode(self):
        """This function allows the CodeMaker to create the code that the CodeBreaker will be trying to crack"""
        codeGen = input("")
        if len(codeGen) < 4:
            raise InvalidCodeError("Code must be 4 digits long.")
        else:   
            codeGen = list(codeGen)
            return codeGen



class CodeBreaker(Player):
    """This class is responsible for the breaking of the code in both Original and Original_AI"""
    def __init__(self, playerNumber, name):
        super().__init__(playerNumber, name)
    
    def makeAttempt_AI(self):
        """This allows the CodeBreaker to make attempts and crack the code in Original_AI"""
        guess = input("")
        guess = guess.upper()
        playerCode = list(guess)
        if len(playerCode) < 4:
            raise InvalidGuessError("A four digit code is required.")
        else:
            playerFeedback = Board().codeCheck(playerCode)
            if playerFeedback == "BBBB":
                print ("")
                print ("Well done!")
                print ("You cracked the code in " + str(Original.attempt) + " attempt(s)")

                Original_AI().GameWin()
            else:
                print(playerFeedback)
            Original_AI.attempt = Original_AI.attempt + 1

    def makeAttempt(self):
        """This allows the CodeBreaker to make attempts and crack the code in Original"""
        guess = input("")
        guess = guess.upper()
        playerCode = list(guess)
        if len(playerCode) < 4:
            raise InvalidGuessError("A four digit code is required.")
        else:
            playerFeedback = Board().codeCheck(playerCode)
            if playerFeedback == "BBBB":
                print ("")
                print ("Well done!")
                print ("You cracked the code in " + str(Original.attempt) + " attempt(s)")
                Original().GameWin()
            else:
                print(playerFeedback)
            Original.attempt = Original.attempt + 1


class Mastermind:
    """This Class is where the game is played and is a parent to both Original and Original_AI"""
    def play(self):
        """This function allows the user to select which game mode is going to be played"""
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
            sys.exit(0)
        else:
            raise InvalidChoiceError("Only select A, B or C")

    def GameWin(self):
        pass

    def GameQuit(self):
        """This ends the game and exits the program"""
        print("Goodbye!")
        sys.exit(0)



class Original(Mastermind):
    """This class is where the 2 Player version of mastermind is played"""
    totalAttempts = 12
    attempt = 1
    def play(self):
        """This function instantiates both the CodeMaker and CodeBreaker classes, allowing the game to be played"""

        playerNumber = 1
        name = input("Player " + str(playerNumber) + ": What is your name?")
        print ("Welcome " + name + ". You can now generate the code. Please enter below a 4 letter combination of [B]lack, B[l]ue, [Y]ellow, [G]reen, [W]hite, [R]ed")

        codeInit = CodeMaker(playerNumber, name).MakeCode()
        print(codeInit)

        print("Enter the same code again")
        codeConfirm = CodeMaker(playerNumber, name).MakeCode()

        if codeInit == codeConfirm:
            for index in range(0, len(codeConfirm)):
                Board().codeAdd(codeConfirm[index])

            print(currentCode)
            print("code stored successfully")


            input("Press any key to clear code and continue")
            ScreenClear()

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
                if Original().attempt == Original().totalAttempts:
                    print("You were unable to break the code in 12 attempts!")
                    print("You lose!")
                    print("")
                    Original().GameWin()
        else:
            raise InvalidCodeError("Codes do not match")
            
    def GameQuit(self):
        """This ends the game and exits the program"""
        print("Goodbye!")
        sys.exit(0)

    def GameWin(self):
        """This function allows the game to be played multiple times without the system rebooting"""
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
    """This class is where the 1 Player version of mastermind is played"""
    totalAttempts = 12
    attempt = 1
    def play(self):
        """This function instantiates the CodeBreaker and generates the code, allowing the game to be played"""
        index = 1
        
        while index <= 4:
            codeColour = CodePegs.codePegs[random.randint(0, 5)]
            Board().codeAdd(codeColour)
            index = index +1


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
            if Original().attempt == Original().totalAttempts:
                print("You were unable to break the code in 12 attempts!")
                print("You lose!")
                print("")
                Original().GameWin()

    def GameQuit(self):
        """This ends the game and exits the program"""
        print("Goodbye!")
        sys.exit(0)

    def GameWin(self):
        """This function allows the game to be played multiple times without the system rebooting"""
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

