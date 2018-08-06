import Ruin

class Player:

    def __init__(self, name):
        self.name = name
        self.hasTurned = False
        self.points = 0
        self.ruins = []

    def hasTurned(self):
        return self.hasTurned

    def turn(self):
        self.hasTurned = True

    def addRuin(self, ruin):
        self.ruins.append(ruin)

    def getNofRuins(self):
        return len(self.ruins)

