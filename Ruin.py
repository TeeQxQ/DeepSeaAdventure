class Ruin:

    def __init__(self, level=-1, value=-1):
        self.level = level
        self.value = value

    def getValue(self):
        return self.value

    def getLevel(self):
        return self.level

    #Ruin is 'blank' if it's level is -1 (normal levels 1-4)
    def isBlank(self):
        if self.level == -1:
            return True
        return False
