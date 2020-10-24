#importing assests


#Adding base classes to Assignment



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
        if gameTypeChoice == "A":
            Original()
        elif gameTypeChoice == "B":
            Original_AI()
        elif gameTypeChoice == "C":
            Mastermind44()
        #To be created and added later
        #else:
            #raise InvalidChoice Error
        #####################################
    
    def GameQuit(self):
        quit()
  

#Child Classes
class Mastermind44(Mastermind):
    pass


class Original(Mastermind):
    pass

class Original_AI(Mastermind):
    pass

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
    pass

#Child Classes
class CodeMaker(Player):
    pass

class CodeBreaker(Player):
    pass


