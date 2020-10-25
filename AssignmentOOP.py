#importing assests


#Adding base classes to Assignment


#Game Classes
class Board:
    pass

class KeyPegs:
    pass

class CodePegs:
    pass

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

#Main Menu
#Parent Class
class Mastermind:
    def play(self):

        #######################################
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
        #########################################
        
        #########################################
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
        #####################################
    
    def GameQuit(self):
        print("Goodbye!")
  

#Child Classes
class Mastermind44(Mastermind):
    pass


class Original(Mastermind):
    pass

class Original_AI(Mastermind):
    def play(self):
        playerNumber = 1
        name = input("Player " + str(playerNumber) + ": What is your name?")
        CodeBreaker(playerNumber, name)
    
    def GameQuit(self):
        print("Goodbye!")

m = Mastermind()
m.play()


