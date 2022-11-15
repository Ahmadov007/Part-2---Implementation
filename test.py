from game import *
from player import *

pOne = Player("Faz", 100, 0, 0)
pTwo = Player("Bob", 100, 0, 0)
pThree = Player("Jon", 100, 0, 0)
playerList = [pOne, pTwo, pThree]

newList = []

maxiGame = Maxi(playerList)




for player in playerList:
    print(player.getName())

del playerList[0]
#maxiGame.remove_player(playerList, "Faz")

for player in playerList:
    print(player.getName())

for player in playerList:
    newList.append(player)

for i in newList:
    print(i.getName())













"""n = 1
n2 = 3
n3 = 5

#print(max(n, n2, n3))

thisDictionary = {"Faz": 150, "John": 200, "James":100}

print(thisDictionary["Faz"])"""

