class Ui:

    def __init__(self):
        pass

    @staticmethod
    def welcome():
        print('Welcome to play TeeQ\'s "Deep Sea Adventure"!')

    @staticmethod
    def askNewPlayerInformation():
        name = input('What is the name of a new player? ')
        return name

    @staticmethod
    def askNofPlayers(lowLimit=2, highLimit=6):
        nofPlayers = int(input('Type the number of players [{}-{}]: '.format(lowLimit, highLimit)))
        while nofPlayers < lowLimit or nofPlayers > highLimit:
            nofPlayers = int(input('{} is not suitable number of players. Please choose between {} and {}: '))
        return nofPlayers

    @staticmethod
    def askIfPlayerWillTurn():
        answer = input('Would you like to turn back [Y or N]? ')
        return self._checkAnswerQuality(answer)

    @staticmethod
    def askPlayerToRoll():
        answer = input('Press enter to roll the dice! ')
        while answer is not '':
            answer = input('Invalid command. Please press enter to roll the dice. ')

    @staticmethod
    def printDices(playerName, dice1, dice2):
        print('Player {} rolled: {} and {}, in total of {} steps!'.format(playerName, dice1, dice2, dice1+dice2))

    @staticmethod
    def askPickUp(level):
        answer = input('Would you like to pick up a level {} ruin [Y or N]? ')
        return self._checkAnswerQuality(answer)

    @staticmethod
    def askPlaceRuin(playerRuinLevels): 
        answer = input('Would you like to place ruin back [Y or N]? ')
        answer = self._checkAnswerQuality(answer)
        if answer:
            answer = int(input('Which ruin you would like to place [{}]? '.format(playerRuinLevels)))
            while answer not in playerRuinLevels:
                answer = int(input('You don\'t have that kind of ruins. Please try again [{}] '.format(playerruinLevels)))
            return answer

        #return -1 if player do not want to place a ruin
        return -1


    @staticmethod
    def printPlayerFinished(player, nextPlayer):
        print('Player {} has finished his turn! Next player is {}.'.format(player, nextPlayer))


    def _checkAnswerQuality(answer):
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


    @staticmethod
    def drawCurrentState():
        pass
