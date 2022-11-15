#
# File: player.py
# Descrition: The player.py file contains the Player class, its attributes and methods. 
# Player objects will be used to play the game. 
# Author: Ahmad Mohammadi
# Student ID: 110120185
# Email ID: mohaf002@mymail.unisa.edu.au
# This is my own work as defined by
# the University's Academic Misconduct Policy.
# 

class Player:
    '''The Player class is used to create objects of player.'''
    def __init__(self, name, chipBalance, numOfGamesPlayed, numOfGamesWon):
        self.__name = name
        self.__chipBalance = chipBalance
        self.__numOfGamesPlayed = numOfGamesPlayed
        self.__numOfGamesWon = numOfGamesWon
        self.__numOfBid = 0
        self.__maxValue = 0

    def getName(self):
        """Returns the player name"""
        return self.__name

    def setName(self, name):
        """Sets the player name using the name parameter"""
        self.__name = name

    def getChipBalance(self):
        """Returns the players chip balance"""
        return self.__chipBalance

    def setChipBalance(self, chipBalance):
        """Sets the players chip balance by chipBalance value"""
        self.__chipBalance = chipBalance
    
    def incrementChipBalance(self, chipBalance):
        self.__chipBalance += chipBalance
    
    def decrementChipBalance(self, chipBalance):
        self.__chipBalance -= chipBalance

    def incrementGamesPlayed(self, num):
        """Increment the number of games played by num value"""
        self.__numOfGamesPlayed += num

    def setNumberOfGamesWon(self, num):
        """Sets the number of games won by num value"""
        self.__numOfGamesWon = num

    def getNumberOfGamesWon(self):
        """Returns the number of games won"""
        return self.__numOfGamesWon
    
    def getNumberOfGamesPlayed(self):
        '''Returns the number of games the player has played'''
        return self.__numOfGamesPlayed

    def setBid(self, number):
        '''sets the bid value of the player in the game'''
        self.__numOfBid = number
    
    def getBid(self):
        '''Returns the bid value'''
        return self.__numOfBid

    def incrementBid(self, number):
        '''increments the bid value'''
        self.__numOfBid += number
    
    def decrementBid(self, number):
        '''decrements the bid value'''
        self.__numOfBid -= number

    def setMaxValue(self, theValue):
        '''sets the sum of the face up value of the dies'''
        self.__maxValue = theValue

    def getMaxValue(self):
        '''Returns the sum of the face up value of the dies'''
        return self.__maxValue
    



