from Airtank import Airtank
from Dice import Dice
from Map import Map
from Player import Player
from Ui import Ui

class Game:

    def __init__(self, airtankSize=25, mapSize=16):
        self.airtank = Airtank(airtankSize)
        self.players = []
        self.currentRound = 1
        self.maxNofRounds = 3
        self.ui = Ui()
        self.dices = [Dice(3), Dice(3)]
        self.map = Map(mapSize)
        self.map.generateRuins()

    def start(self):
        self.ui.welcome()


