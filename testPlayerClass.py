# Import relevant files and libraries
import unittest
from player import *

# Creating player objects from the player Class
playerOne = Player("Ahmad", 100, 2, 4)

class TestPlayerClass(unittest.TestCase):
    '''This class tests the methods and attributes of the Player class.'''

    def testPlayerGetName(self):
        self.assertEqual(playerOne.getName(), "Ahmad")

    def testSetPlayerName(self):
        playerObject = Player("No Name", 100, 0, 0)
        playerObject.setName("Edwards")
        self.assertEqual(playerObject.getName(), "Edwards")

    def testSetChipBalance(self):
        playerObject = Player("John Snow", 0, 0, 0)
        playerObject.setChipBalance(100)
        self.assertEqual(playerObject.getChipBalance(), 100)

    def testGetChipBalance(self):
        playerObject = Player("John Snow", 400, 0, 0)
        self.assertEqual(playerObject.getChipBalance(), 400)

    def testIncrementChipBalance(self):
        playerObject = Player("John Snow", 400, 0, 0)
        playerObject.incrementChipBalance(100)
        self.assertEqual(playerObject.getChipBalance(), 500)

    def testDecrementChipBalance(self):
        playerObject = Player("John Snow", 400, 0, 0)
        playerObject.decrementChipBalance(100)
        self.assertEqual(playerObject.getChipBalance(), 300)

    def testSetNumberOfGamesWon(self):
        playerObject = Player("John Snow", 400, 0, 0)
        playerObject.setNumberOfGamesWon(4)
        self.assertEqual(playerObject.getNumberOfGamesWon(), 4)

    def testGetNumberOfGamesWon(self):
        playerObject = Player("John Snow", 400, 0, 4)
        self.assertEqual(playerObject.getNumberOfGamesWon(), 4)

    def testGetNumberOfGamesPlayed(self):
        playerObject = Player("John Snow", 400, 5, 4)
        self.assertEqual(playerObject.getNumberOfGamesPlayed(), 5)

    def testSetBid(self):
        playerObject = Player("John Snow", 0, 0, 0)
        playerObject.setBid(100)
        self.assertEqual(playerObject.getBid(), 100)

    def testGetBid(self):
        playerObject = Player("John Snow", 0, 0, 0)
        playerObject.setBid(255)
        self.assertEqual(playerObject.getBid(), 255)

    def testIncremenetBid(self):
        playerObject = Player("John Snow", 0, 0, 0)
        playerObject.setBid(255)
        playerObject.incrementBid(45)
        self.assertEqual(playerObject.getBid(), 300)

    def testDecremenetBid(self):
        playerObject = Player("John Snow", 0, 0, 0)
        playerObject.setBid(255)
        playerObject.decrementBid(5)
        self.assertEqual(playerObject.getBid(), 250)

    def testSetMaxValue(self):
        playerObject = Player("Matt", 0, 0, 0)
        playerObject.setMaxValue(567)
        self.assertEquals(playerObject.getMaxValue(), 567)

    def testGetMaxValue(self):
        playerObject = Player("Matt", 0, 0, 0)
        playerObject.setMaxValue(1)
        self.assertEquals(playerObject.getMaxValue(), 1)

    








# Starts the unittest testing
unittest.main()