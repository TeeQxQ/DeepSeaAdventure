import random
from Ruin import Ruin

class Map:

    def __init__(self, size=32):
        self.size = size
        self.ruins = []

    def generateRuins(self):
        level = 0
        for points in range(0, int(self.size/2)):
            if points % 4 == 0:
                level += 1
            self.ruins.append([Ruin(level, points)])
            self.ruins.append([Ruin(level, points)])

    def ruinHasTakenAt(self, index):
        if index < self.size*2:
            if self.ruins[index][0].isBlank():
                return True
        return False

    def pickUpRuinsFrom(self, index):
        if index < self.size*2:
            ruins = self.ruins[index]
            self.ruins[index] = [Ruin()]
            return ruins

        return Ruin()

    def placeRuinsTo(self, index, ruins):
        if index < self.size*2:
            if not self.ruinHasTakenAt(index):
                self.ruins[index] = ruins

    def getSize(self):
        return self.size
