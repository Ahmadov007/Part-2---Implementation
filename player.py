#
# File: filename.py
# Descrition: A brief description of this Python module.
# Author: Steve Jobs
# Student ID: 12345678
# Email ID: jobst007
# This is my own work as defined by
# the University's Academic Misconduct Policy.
# 


class Player:
    def __init__(self, name, chipBalance, numOfGamesPlayed, numOfGamesWon):
        self.__name = name
        self.__chipBalance = chipBalance
        self.__numOfGamesPlayed = numOfGamesPlayed
        self.__numOfGamesWon = numOfGamesWon

    def getName(self):
        """Returns the player name"""
        return self.__name

    def setName(self, name):
        """Sets the player name using the name parameter"""
        self.__name = name

    def getChipBalance(self):
        """Returns the players chip balance"""
        return self.__chipBalance

    def setChipBalnce(self, chipBalance):
        """Sets the players chip balance by chipBalance value"""
        self.__chipBalance = chipBalance

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
        return self.__numOfGamesPlayed




