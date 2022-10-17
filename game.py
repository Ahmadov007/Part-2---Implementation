#
# File: filename.py
# Descrition: A brief description of this Python module.
# Author: Steve Jobs
# Student ID: 12345678
# Email ID: jobst007
# This is my own work as defined by
# the University's Academic Misconduct Policy.
# 



class Game:
    def __init__(self, name, maxPlayer, minPlayer, playerList):
        self.__name = name
        self.__maximumPLayer = maxPlayer
        self.__minimumPLayer = minPlayer
        self.__playerList = playerList

    def findPLayer(self, name):
        pass
    
    def chipBid(self):
        pass

    def shifterValue(self, val):
        pass

    def play(self):
        pass


class Odd_Or_Even(Game):
    def __init__(self, playerList):
        super().__init__("Odd Or Even", 1, 1, playerList)
    
    def play(self):
        pass


class Maxi(Game):
    def __init__(self, playerList):
        super().__init__("Maxi", 5, 3, playerList)
    
    def play(self):
        pass

class Bunco(Game):
    def __init__(self, playerList):
        super().__init__("Bunco", 4, 2, playerList)
    
    def play(self):
        pass
      



