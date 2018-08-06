from Airtank import Airtank

class Game:

    def __init__(self, airtankSize = 25):
        self.airtank = Airtank(airtankSize)
        self.players = []
        self.currentRound = 1
        self.maxNofRounds = 3

    def 
