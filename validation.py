class Validation:
    """This class contains methods to validate our code"""
    
    def findPlayer(self, name, playerList):
        '''Finds a player using the name parameter'''
        if len(playerList) == 0:
            return False
        else:
            for player in playerList:
                if player.getName() == name:
                    return True
                else:
                    return False