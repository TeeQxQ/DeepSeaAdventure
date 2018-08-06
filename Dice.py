import random

class Dice:

    def __init__(self, size):
        self.value = -1     #last rolled value of the dice
        self.size = size    #how many different numbers the dice has

    def roll(self):
        self.value = random.randint(0, self.size+1)

    def getValue(self):
        return self.value
