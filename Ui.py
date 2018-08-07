class Ui:

    def __init__(self):
        pass

    @staticmethod
    def welcome(self):
        print('Welcome to play TeeQ\'s "Deep Sea Adventure"!')

    @staticmethod
    def askNewPlayerInformation(self):
        name = raw_input('What is the name of a new player?')
        return name

    @staticmethod
    def askNofPlayers(self, lowLimit=2, highLimit=6):
        nofPlayers = int(raw_input('Type the number of players [{}-{}]: '.format(lowLimit, highLimit)))
        while nofPlayers < lowLimit or nofPlayers > highLimit:
            nofPlayers = int(raw_input('{} is not suitable number of players. Please choose between {} and {}: '))
        return nofPlayers

    @staticmethod
    def askIfPlayerWillTurn(self):
        answer = raw_input('Would you like to turn back [Y or N]? ')
        return self._checkAnswerQuality(answer)

    @staticmethod
    def askPlayerToRoll(self):
        answer = raw_input('Press enter to roll the dice! ')
        while answer is not '':
            answer = raw_input('Invalid command. Please press enter to roll the dice. ')

    @staticmethod
    def printDices(self, playerName, dice1, dice2):
        print('Player {} rolled: {} and {}, in total of {} steps!'.format(playerName, dice1, dice2, dice1+dice2))

    @staticmethod
    def askPickUp(self, level):
        answer = raw_input('Would you like to pick up a level {} ruin [Y or N]? ')
        return self._checkAnswerQuality(answer)

    @staticmethod
    def askPlaceRuin(self, playerRuinLevels): 
        answer = raw_input('Would you like to place ruin back [Y or N]? ')
        answer = self._checkAnswerQuality(answer)
        if answer:
            answer = int(raw_input('Which ruin you would like to place [{}]? '.format(playerRuinLevels)))
            while answer not in playerRuinLevels:
                answer = int(raw_input('You don\'t have that kind of ruins. Please try again [{}] '.format(playerruinLevels)))
            return answer

        #return -1 if player do not want to place a ruin
        return -1


    @staticmethod
    def printPlayerFinished(self, player, nextPlayer):
        print('Player {} has finished his turn! Next player is {}.'.format(player, nextPlayer))


    def _checkAnswerQuality(self, answer):
        if answer in ('y', 'Y'):
            return True
        elif answer in ('n', 'N', ''):
            return False
        else:
            while answer not in ('y', 'Y', 'n', 'N', ''):
                answer = raw_input('Invalid command {}. Please, choose between Y and N: '.format(answer))
                if answer in ('y', 'Y'):
                    return True
                if answer in ('n', 'N', ''):
                    return False

