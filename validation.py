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
      
        if len(playerList) == 0:
            print("Player does not exist (empty list).")
        else:
            for player in playerList:
                if player.getName() == name:
                    return player
                
    
    def returnPlayerIndex(self, name, playerList):

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
