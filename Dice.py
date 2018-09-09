import random

class Dice:

    def __init__(self, size=3):
        self.value = -1     #last rolled value of the dice
        self.size = size    #how many different numbers the dice has

    def roll(self):
        self.value = random.randint(1, self.size)

    def getValue(self):
        if self.value == -1:
            self.roll()

        return self.value


if __name__ == '__main__':
    testDice = Dice(6)
    
    print('Initial value of the created dice: {}'.format(testDice.value))
    print('Initial value of the dice via getValue: {}'.format(testDice.getValue()))
    
    print('Let\'s roll the dice!')
    testDice.roll()
    print('New value: {}'.format(testDice.getValue()))
    print('Ask it again: {}'.format(testDice.getValue()))
    
    print('Let\'s roll it again 100 times!')
    maxValue = -1
    minValue = 99999
    for i in range(0, 100):
        testDice.roll()
        minValue = min(minValue, testDice.getValue())
        maxValue = max(maxValue, testDice.getValue())
    
    print('After 100 rolls, the minimum and maximum values were: {} and {}'.format(minValue, maxValue))
    print('Thanks for rolling!')