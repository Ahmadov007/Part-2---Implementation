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
        self.__InGamePlayers = []

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

    def getPlayerList(self):
        return self.__playerList

    def setPlayerList(self, newList):
        self.__playerList = newList

    def appendToInGameList(self, thePlayer):
        self.__InGamePlayers.append(thePlayer)

    def getInGamePlayerList(self):
        return self.__InGamePlayers

class OddOrEven(Game):
    def __init__(self, playerList):
        super().__init__("Odd Or Even", 1, 1, playerList)
    
    def play(self):
        updatedList = self.getPlayerList()
        randomNumber = random.randint(1, 6)
        validation = Validation()
        playerName = input("What is the name of player?\n> ")
        
        playerObject = validation.getPlayer(playerName, self.getPlayerList())
        playerChips = int(input("How many chips would you bid " + playerName + " (1-" + str(playerObject.getChipBalance()) + ")?"))

        if validation.findPlayer(playerName, self.getPlayerList()) == False:
            print("Sorry Player does not exist.")
        else:
            print("Hey " + playerName + " Odd (o) or Even (e)?")
            userInput = input("> ")

            while userInput != "o" and userInput != "e":
                print("Invalid choice.")
                print("Odd (o) or Even (e)?")
                userInput = input("> ")
            

            howStrongInput = int(input("How strong will you throw (0-5)?\n> "))

            while howStrongInput < 0 or howStrongInput > 5:
                print("Invalid choice.")
                howStrongInput = int(input("How strong will you throw (0-5)?\n> "))

                
            print("Your number is: ", howStrongInput)
            print("Random Number: " + str(randomNumber))
            finalNumber = randomNumber + howStrongInput
            if(finalNumber > 6):
                finalNumber -= 6
           
            if(finalNumber == 1):
                print("⚀")
            elif(finalNumber == 2):
                print("⚁")
            elif(finalNumber == 3):
                print("⚂")
            elif(finalNumber == 4):
                print("⚃")
            elif(finalNumber == 5):
                print("⚄")
            elif(finalNumber == 6):
                print("⚅")
            
            if userInput == "e" and finalNumber % 2 == 0:
                print("Congratulations, " + playerName + "! You win!")

                #Add the chip balance to the players chipBalance attributes
               
                updatedList[validation.returnPlayerIndex(playerName, self.getPlayerList())].incrementChipBalance(playerChips)
                self.setPlayerList(updatedList)
            elif userInput == "o" and finalNumber % 2 != 0:
                print("Congratulations, " + playerName + "! You win!")
                updatedList[validation.returnPlayerIndex(playerName, self.getPlayerList())].incrementChipBalance(playerChips)
                self.setPlayerList(updatedList)
                
            elif userInput == "e" and finalNumber % 2 != 0:
                print("Sorry, " + playerName + "! You lose!")

                updatedList[validation.returnPlayerIndex(playerName, self.getPlayerList())].decrementChipBalance(playerChips)
                self.setPlayerList(updatedList)
            elif userInput == "o" and finalNumber % 2 == 0:
                print("Sorry, " + playerName + "! You lose!")
                updatedList[validation.returnPlayerIndex(playerName, self.getPlayerList())].decrementChipBalance(playerChips)
                self.setPlayerList(updatedList)
                
         
            
            

  
            




class Maxi(Game):
    def __init__(self, playerList):
        super().__init__("Maxi", 5, 3, playerList)

    def removePlayer(self, theIndex, playerList):
        newList = []
        del playerList[theIndex]

        for player in playerList:
            newList.append(player)
        
        return newList

    def returnIndexOfHighestValue(self, playerList):

        highestValue = 0
        index = 0
        count = 0 
        while(count < len(playerList)):
            if playerList[count].getMaxValue() > highestValue:
                index = count
            count += 1
        
        return index
    
    def returnIndexOfLowestValue(self, playerList):
        lowestValue = playerList[0].getMaxValue()
        index = 0
        count = 0 
        while(count < len(playerList)):
            if playerList[count].getMaxValue() < lowestValue:
                index = count
            count += 1
        
        return index
           
    def returnHighestFaceUpValue(self, playerList):
        highestValue = 0
        playerName = ""
        index = -1
        # For loop to compare players chip value and display the highest chip holder.    
        for player in playerList:
            if player.getMaxValue() > highestValue:
               highestValue = player.getMaxValue()
               playerName = player.getName()
               
        print("Highest Chip Holder =>", playerName, " with", str(highestValue), "face up value!")
        print()
        return highestValue

    def returnLowestFaceUpValue(self, playerList):
        lowestValue = 10000
        playerName = ""

        for player in playerList:
            if player.getMaxValue() < lowestValue:
                lowestValue = player.getMaxValue()
                playerName = player.getName()
        print("Lowest Face Up Value =>", playerName, " with", str(lowestValue), "face up value!")
        return lowestValue

        
    def play(self):
        print("Let’s play the game of Maxi!")
        playerCount = int(input("How many players (3-5)?\n> "))

        while playerCount < 3 or playerCount > 5:
            print("Invalid amount of players!")
            print("It has to be between 3 - 5 players.")
            playerCount = int(input("How many players (3-5)?\n> "))
        
        for number in range(playerCount):
            playerName = input("What is the name of player #" + str(number+1) + "?")
            validFunction = Validation()

            while(validFunction.findPlayer(playerName, self.getPlayerList()) == False):
                print("There is no player named " + playerName + ".")
                playerName = input("What is the name of player #" + str(number+1) + "?")
            
            playerChips = int(input("How many chips would you bid " + playerName + " (1-" + str(self.getPlayerList()[validFunction.returnPlayerIndex(playerName, self.getPlayerList())].getChipBalance()) + ")?"))
            self.getPlayerList()[validFunction.returnPlayerIndex(playerName, self.getPlayerList())].setBid(playerChips)
            self.appendToInGameList(validFunction.getPlayer(playerName, self.getPlayerList()))

        print("Let the game begin!")
        
        updatedList = self.getPlayerList()

        isPlaying = True

        while(isPlaying):
            
            


            for player in self.getInGamePlayerList():
                diceOne = random.randint(1, 6)
                diceTwo = random.randint(1, 6)
                print("it's " + player.getName()+"'s turn.")
                
                howStrongInput = int(input("How strong will you throw (0-5)?\n> "))

                while howStrongInput < 0 or howStrongInput > 5:
                    print("Invalid choice.")
                    howStrongInput = int(input("How strong will you throw (0-5)?\n> "))

               
               

            
            

                finalNumberForD1 = diceOne + howStrongInput
                finalNumberForD2 = diceTwo + howStrongInput

                if(finalNumberForD1 > 6 ):
                    finalNumberForD1 -= 6
                
                if(finalNumberForD2 > 6):
                    finalNumberForD2 -= 6


                player.setMaxValue(finalNumberForD1+finalNumberForD2)
                
                finalString = ""
                
                match finalNumberForD1:
                    case 1:
                        finalString += "⚀"
                    case 2:
                        finalString += "⚁"
                    case 3:
                        finalString += "⚂"
                    case 4:
                        finalString += "⚃"
                    case 5:
                        finalString += "⚄"
                    case 6:
                        finalString += "⚅"

                match finalNumberForD2:
                    case 1:
                        finalString += "⚀"
                    case 2:
                        finalString += "⚁"
                    case 3:
                        finalString += "⚂"
                    case 4:
                        finalString += "⚃"
                    case 5:
                        finalString += "⚄"
                    case 6:
                        finalString += "⚅"
                print(finalString)  
            
            self.setPlayerList(self.removePlayer(self.returnIndexOfLowestValue(self.getInGamePlayerList()), self.getInGamePlayerList()))
            
            remaining = "Players remaining: "
            for player in self.getInGamePlayerList():
                
                if(player == self.getInGamePlayerList()[-1]):
                    remaining += player.getName()
                else:
                    remaining += player.getName() + ", "

            
    
            if(len(self.getInGamePlayerList()) == 1):
                for i in self.getInGamePlayerList():
                    print("Congratulations, " + i.getName() + "! You win!")
                isPlaying = False
            else:
                print(remaining)

            
            
               
               
   
                            
                

           
          
            
        
            


       

class Bunco(Game):
    def __init__(self, playerList):
        super().__init__("Bunco", 4, 2, playerList)
    
    def play(self):
        pass
      

