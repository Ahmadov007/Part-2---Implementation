#
# File: validation.py
# Descrition: The validation.py file contains the Validation class, 
# which is used to validate and contain methods that can help find players 
# in a list.  
# Author: Ahmad Mohammadi
# Student ID: 110120185
# Email ID: mohaf002@mymail.unisa.edu.au
# This is my own work as defined by
# the University's Academic Misconduct Policy.
# 


class Validation:
    """This class contains methods to validate our code"""
    
    def findPlayer(self, name, playerList):
        '''Finds a player using the name parameter'''
        isFound = False

        if len(playerList) == 0:
            isFound = False
        else:
            for player in playerList:
                if player.getName() == name:
                    isFound = True
                    break
                else:
                    isFound = False
        return isFound
    
    def getPlayer(self, name, playerList):
        '''Used to return a player object given a name and a list'''
        if len(playerList) == 0:
            print("Player does not exist (empty list).")
        else:
            for player in playerList:
                if player.getName() == name:
                    return player
                
    
    def returnPlayerIndex(self, name, playerList):
        '''Returns an index of the name found in the playerList'''

        index = 0
        count = 0
        isReturned = False

        while(count < len(playerList) and isReturned == False):

            if(playerList[index].getName() == name):
                isReturned = True
                break
            

            count += 1
            index += 1

        if(isReturned == True):
            return index
        else:
            return -1
