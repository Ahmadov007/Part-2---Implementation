# Import relevant files and libraries
from os import unlink
import unittest
from scoreBoard import *
from player import *
from game import *

playerOne = Player("Matt", 100, 5, 2)
playerTwo = Player("Joe", 20, 10, 6)
playerThree = Player("Fish", 800, 8, 8)
playerList =[playerOne, playerTwo, playerThree]

myScoreBoard = ScoreBoard(playerList)

class TestGameClass(unittest.TestCase):
    
    def testOddOrEvenClass(self):
        oddOrEvenGame = OddOrEven(playerList)
        oddOrEvenGame.play()
    
    def TestMaxi(self):
        maxiGame = Maxi(playerList)
        maxiGame.play()




# Starts the unittest testing
unittest.main()