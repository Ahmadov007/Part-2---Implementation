#
# File: filename.py
# Descrition: A brief description of this Python module.
# Author: Steve Jobs
# Student ID: 12345678
# Email ID: jobst007
# This is my own work as defined by
# the University's Academic Misconduct Policy.
# 
from validation import *
import random

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

    def shiftTheValue(self, shiftValue, randomNumberValue):
        sumOfValue = shiftValue+randomNumberValue
        resultValue = 0
        if sumOfValue > 6:
            resultValue = sumOfValue-6
        elif sumOfValue <= 6:
            resultValue = sumOfValue
        
        return resultValue

    def play(self):
        pass


class Odd_Or_Even(Game):
    def __init__(self, playerList):
        super().__init__("Odd Or Even", 1, 1, playerList)
    
    def play(self):
        randomNmber = random.randint(1, 6)
        validation = Validation()
        playerName = input("What is the name of player?\n> ")
        
        if validation.findPlayer(playerName, self.__playerList) == False:
            print("Sorry Player does not exist.")
        else:
            print("Hey " + playerName, + " Odd (o) or Even (e)?")
            userInput = input("> ")

            while userInput != "o" and userInput != "e":
                print("Invalid choice.")
                print("Odd (o) or Even (e)?")
                userInput = input("> ")

            print("How strong will you throw (0-5)?")
            
    
  
            




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
      
