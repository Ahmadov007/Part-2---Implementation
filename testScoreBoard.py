# Import relevant files and libraries
import unittest
from scoreBoard import *
from player import *

playerOne = Player("Matt", 100, 5, 2)
playerTwo = Player("Joe", 20, 10, 6)
playerList =[playerOne, playerTwo]

myScoreBoard = ScoreBoard(playerList)

class TestScoreBoardClass(unittest.TestCase):
    '''Tests the attributes and methods of the ScoreBoard class.'''
    
    def testDisplayScoreBoard(self):
        myScoreBoard.displayScoreBoard()




# Starts the unittest testing
unittest.main()