#
# File: atd.py
# Descrition: The atd.py file contains the allThatDice class 
# as well as the run method where the game starts.  
# Author: Ahmad Mohammadi
# Student ID: 110120185
# Email ID: mohaf002@mymail.unisa.edu.au
# This is my own work as defined by
# the University's Academic Misconduct Policy.
# 
from player import *
from scoreBoard import *
from validation import Validation
from game import *


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
            #Displays the menu 
            userInput = self.displayMenu()
            
            # If user selects "r"
            if userInput == "r":
                #Call the registerPlayer() function
                self.registerPlayer()
            # If user selects "s"
            elif userInput == "s":
                scoreBoard = ScoreBoard(self.__registeredPlayers)
                scoreBoard.displayScoreBoard()
            # If user selects "p"
            elif userInput == "p":
                # Displays and returns the users choice 
                userChoice = self.displayGameOption()

                # If users choice is 'o' the execute the code 
                if userChoice == "o":
                    oddOrEvenGame = OddOrEven(self.__registeredPlayers)
                    oddOrEvenGame.play()

                
                elif userChoice == "m":
                    maxiGame = Maxi(self.__registeredPlayers)
                    maxiGame.play()
                
                        
                        
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

        # Validates the users input 
        while userInput != "r" and userInput != "s" and userInput != "p" and userInput != "q":
            print("Invalid choice!")
            print("What would you like to do?")
            print("  (r) register")
            print("  (s) show the leader board")
            print("  (p) play a game")
            print("  (q) quit")
            userInput = input("> ")
        
        # returns the users input 
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