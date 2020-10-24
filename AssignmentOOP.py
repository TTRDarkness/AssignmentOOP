#importing assests
import abc

#Adding base classes to Assignment


#Abstract class
class Game(metaclass=abc.ABCMeta):
    #Adding abstract properties and methods
    @abc.abstractproperty
    def GameType(self):
        pass

    @abc.abstractmethod
    def GameQuit(self):
        pass


#Abstract Children
class Mastermind44(Game):
    pass

class Mastermind(Game):
    pass

class Board:
    pass

class KeyPegs:
    pass

class CodePegs:
    pass

class CodeCounters:
    pass

#Super Class
class Player:
    pass

#Child Classes
class CodeMaker(Player):
    pass

class CodeBreaker(Player):
    pass


