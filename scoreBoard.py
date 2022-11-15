#
# File: scoreBoard.py
# Descrition: The scoreBoard.py file contains the ScoreBoard class which is 
# used to display the scores and game statistics of the players resgistered
# in the game. 
# Author: Ahmad Mohammadi
# Student ID: 110120185
# Email ID: mohaf002@mymail.unisa.edu.au
# This is my own work as defined by
# the University's Academic Misconduct Policy.
# 

class ScoreBoard:
    def __init__(self, players):
        self.__playerList = players

    def displayScoreBoard(self):
        '''Displays the players results and game stats'''
       
        print("="*35)
        print(format("Name", ""), format("Played", ">20s"), format("Won", ">2s"), format("Chips", ">2s"))
        print("="*35)
        

        # Using for loop to display player stats.
        for player in self.__playerList:
            print(format(player.getName(), "<18s"), format(str(player.getNumberOfGamesPlayed()), "<2s"), format(str(player.getNumberOfGamesWon()) , ">5s"), format(str(player.getChipBalance()), ">5s"))
            

        print("="*35)
    



