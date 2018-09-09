class Player:

    def __init__(self, name, isAI=False):
        self.name = name
        self.hasTurned = False
        self.points = 0
        self.ruins = []
        self.isAi = isAI
        self.location = -1
    
    def getName(self):
        return self.name

    def hasTurned(self):
        return self.hasTurned

    def turn(self):
        self.hasTurned = True

    def addRuin(self, ruin):
        self.ruins.append(ruin)

    def getNofRuins(self):
        return len(self.ruins)
    
    def isAI(self):
        return self.isAi

    def getLocation(self):
        return self.location
    
    def setLocation(self, newLocation):
        self.location = newLocation
        

