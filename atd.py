#
# File: filename.py
# Descrition: A brief description of this Python module.
# Author: Steve Jobs
# Student ID: 12345678
# Email ID: jobst007
# This is my own work as defined by
# the University's Academic Misconduct Policy.
# 
from player import *
from scoreBoard import *



class AllThatDice:
    def __init__(self):
        self.__registeredPlayers = []

    def run(self):
        '''Runs AllThatDice'''

        print("Welcome to All-That-Dice !")
        print("Developed by Alan Turing")
        print("COMP 1048 Object-Oriented Programming")
        print()
       
        playingGame = True

        while playingGame == True:
            userInput = self.displayMenu()
            if userInput == "r":
                self.registerPlayer()
            elif userInput == "s":
                scoreBoard = ScoreBoard(self.__registeredPlayers)
                scoreBoard.displayScoreBoard()
            elif userInput == "p":
                userChoice = self.displayGameOption()

                if userChoice == "o":
                    playerName = input("What is the name of player?\n> ")
                    
                    if self.findPlayer(playerName) == False:
                        print("Sorry " + playerName + " does not exist.")
                    else:
                        print("Hey ")
                    print(self.findPlayer(playerName, self.__registeredPlayers))

                elif userChoice == "m":
                    pass
                elif userChoice == "b":
                    pass

            elif userInput == "q":
                playingGame = False

        
        


    def registerPlayer(self):
        '''Registers a player using the name parameter'''
        print("What is the name of the new player?")
        playerName = input("> ")

        if len(self.__registeredPlayers) == 0:
            playerObject = Player(playerName, 100, 0, 0)
            self.__registeredPlayers.append(playerObject)
            print("Welcome, "+ playerName)
        else:
            isPlayerInList = False
            for player in self.__registeredPlayers:
                if player.getName() == playerName:
                    isPlayerInList = True
                    break
            
            if isPlayerInList == True:
                print("Sorry, the name is already taken.")
            else:
                playerObject = Player(playerName, 100, 0, 0)
                self.__registeredPlayers.append(playerObject)
                print("Welcome, "+ playerName)




    
    def displayMenu(self):
        '''Displays the menu'''
        print("What would you like to do?")
        print("  (r) register")
        print("  (s) show the leader board")
        print("  (p) play a game")
        print("  (q) quit")
        userInput = input("> ")

        while userInput != "r" and userInput != "s" and userInput != "p" and userInput != "q":
            print("Invalid choice!")
            print("What would you like to do?")
            print("  (r) register")
            print("  (s) show the leader board")
            print("  (p) player a game")
            print("  (q) quit")
            userInput = input("> ")
        
        return userInput


    


    def displayGameOption(self):
        '''Displays the game option'''
        print("Which game would you like to play?")
        print("  (o) Odd-or-Even")
        print("  (m) Maxi")
        print("  (b) Bunco")
        userInput = input("> ")
        while userInput != "o" and userInput != "m" and userInput != "b":
            print("Invalid choice")
            print("Which game would you like to play?")
            print("  (o) Odd-or-Even")
            print("  (m) Maxi")
            print("  (b) Bunco")
            userInput = input("> ")
        
        return userInput


        


#STARTS THE GAME
game = AllThatDice()
game.run()