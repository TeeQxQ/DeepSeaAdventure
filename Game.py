from Airtank import Airtank
from Dice import Dice
from Ui import Ui

class Game:

    def __init__(self, airtankSize=25):
        self.airtank = Airtank(airtankSize)
        self.players = []
        self.currentRound = 1
        self.maxNofRounds = 3
        self.ui = Ui()
        self.dices = [Dice(3), Dice(3)]

    def start():
        self.ui.welcome()

        for i in range(self.ui.askNofPlayers()):
            self.players.append(Player(self.ui.askNewPlayerInformation()))
