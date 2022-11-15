#
# File: filename.py
# Descrition: A brief description of this Python module.
# Author: Steve Jobs
# Student ID: 12345678
# Email ID: jobst007
# This is my own work as defined by
# the University's Academic Misconduct Policy.
# 

class ScoreBoard:
    def __init__(self, players):
        self.__playerList = players

    def displayScoreBoard(self):
        print("="*59)
        print("-", (format("Player Summary", "^55s")), "-")
        print("="*59)
        print("-", format("P", ">29s"), format("W", ">2s"), format("L", ">2s"), format("D", ">2s"), format("Chips", ">7s"), format("Score", ">7s"), format("-", ">2s"))
        print("-"*59)
        

        # Using for loop to display player stats.
        for player in self.__playerList:
            print(format("-", "<2s"), format(player.getName(), "<25s"), format(str(player.getChipBalance()), ">2s"), format(str(player.getNumberOfGamesPlayed()), ">2s"), format(str(player.getNumberOfGamesWon()), ">2s"))
            print("-"*59)

        print("="*59)
    



