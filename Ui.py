from Map import Map
from Player import Player
from Ruin import Ruin

class Ui:

    def __init__(self):
        pass

    @staticmethod
    def welcome():
        print('Welcome to play TeeQ\'s "Deep Sea Adventure"!')
    
    @staticmethod
    def goodbye():
        print('')
        print('Thanks for playing!')

    @staticmethod
    def askNewPlayerInformation(playerNumber=-1):
        name = ''
        while name == '':
            if playerNumber != -1:
                name = input('Give {}. player name? '.format(playerNumber))
            else:
                name = input('Give new player name? ')
            if name == '':
                print('Name cannot be empty')
        print('Welcome {}!'.format(name))
        return name
    
    @staticmethod
    def printNofAIPlayers(AIplayers):
        print('Number of AI players in this game: {}'.format(AIplayers))
    
    @staticmethod
    def askNofPlayers(lowLimit=2, highLimit=6):
        nofPlayers = int(input('Type the number of regular players [{}-{}]: '.format(lowLimit, highLimit)))
        while nofPlayers < lowLimit or nofPlayers > highLimit:
            nofPlayers = int(input('{} is not suitable number of players. Please choose between {} and {}: '.format(nofPlayers, lowLimit, highLimit)))
        return nofPlayers
    
    @staticmethod
    def printCurrentPlayer(player):
        print('Next player: {}'.format(player))
    
    @staticmethod
    def printRoundInfo(roundNro):
        print('---------------')
        print('ROUND NUMBER {}'.format(roundNro))
        print('')
    
    @staticmethod
    def askIfPlayerWillTurn(self):
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
    def askPickUp(self, level):
        answer = input('Would you like to pick up a level {} ruin [Y or N]? ')
        return self._checkAnswerQuality(answer)

    @staticmethod
    def askPlaceRuin(self, playerRuinLevels): 
        answer = input('Would you like to place ruin back [Y or N]? ')
        answer = self._checkAnswerQuality(answer)
        if answer:
            answer = int(input('Which ruin you would like to place [{}]? '.format(playerRuinLevels)))
            while answer not in playerRuinLevels:
                answer = int(input('You don\'t have that kind of ruins. Please try again [{}] '.format(playerRuinLevels)))
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
                answer = input('Invalid command {}. Please, choose between Y and N: '.format(answer))
                if answer in ('y', 'Y'):
                    return True
                if answer in ('n', 'N', ''):
                    return False

    
    @staticmethod
    def drawMap(currentMap, players):
        pen = MapDrawer()
        pen.draw(currentMap, players)
    
    @staticmethod
    def drawCurrentState():
        pass


class MapDrawer:
    
    #currentMap: Map object representing a map
    #players: An array of players
    def __init__(self, currentMap, players):
        self.map = currentMap
        self.players = players
        self.line = ''
        self.piecesPerLine = 9
        self.currentPiece = 0
        
        self.playerLocations = []
        for player in self.players:
            self.playerLocations.append(player.getLocation())
    

    def draw(self):
        
        #array of arrays
        ruins = self.map.getMap()
        
        mapLine = 0
        piecesDrawn = 0
        coordinatesToBeDrawn = []
        
        while piecesDrawn < self.map.getSize():
            
            print('')
            
            #----------------------------------------------------------------
            #At first, determine which coordinates must be drawn in this round:
            #----------------------------------------------------------------
            
            coordinatesToBeDrawn = []
            #draw full line
            if mapLine %2 == 0:
                #draw from left to right
                if mapLine %4 == 0:
                    for coord in range(piecesDrawn, min(piecesDrawn + self.piecesPerLine, self.map.getSize())):
                        coordinatesToBeDrawn.append(coord)
                #draw from right to left:
                else:
                    for coord in range(min(piecesDrawn + self.piecesPerLine-1, self.map.getSize()-1), piecesDrawn-1, -1):
                        coordinatesToBeDrawn.append(coord)
            #draw only one piece
            else:
                coordinatesToBeDrawn = [piecesDrawn]
            
            #-----------------------
            #Draw one line of pieces.
            #-----------------------
            
            #one piece is combination of three subrows
            for subLine in range(3):
                
                #draw full line
                if mapLine %2 == 0:
                    
                    if len(coordinatesToBeDrawn) < self.piecesPerLine and mapLine %4 != 0:
                        for _ in range(self.piecesPerLine - len(coordinatesToBeDrawn)):
                            self.drawNothing()
                    
                    for coord in coordinatesToBeDrawn:
                        
                         #if player is in this location
                        if coord in self.playerLocations:
                            for player in self.players:
                                if player.getLocation() == coord:
                                    if subLine == 1:
                                        self.drawPlayer(player)
                                    else:
                                        self.drawEmpty()
                        
                        else:
                            ruinStack = ruins[coord]
                            if len(ruinStack) == 1:
                                if subLine == 1:
                                    self.drawRuin(ruinStack[0])
                                else:
                                    self.drawEmpty()
                            elif len(ruinStack) == 2:
                                if subLine == 2:
                                    self.drawEmpty()
                                else:
                                    self.drawRuin(ruinStack(subLine))
                            else:
                                self.drawRuin(ruinStack(subLine))

                #draw only one piece    
                else:
                    
                    #draw from right to left
                    if (mapLine-1) %4 == 0:
                        for _ in range(self.piecesPerLine - 1):
                            self.drawNothing()
                    
                    #if player is in this location
                    if coordinatesToBeDrawn[0] in self.playerLocations:
                        for player in self.players:
                            if player.getLocation() == coordinatesToBeDrawn[0]:
                                if subLine == 1:
                                    self.drawPlayer(player)
                                else:
                                    self.drawEmpty()

                    else:
                        ruinStack = ruins[coordinatesToBeDrawn[0]]

                        if len(ruinStack) == 1:
                            if subLine == 1:
                                self.drawRuin(ruinStack[0])
                            else:
                                self.drawEmpty()
                        elif len(ruinStack) == 2:
                            if subLine == 3:
                                self.drawEmpty()
                            else:
                                self.drawRuin(ruinStack[subLine])
                        else:
                            self.drawRuin(ruinStack[subLine])
                    
                    #draw from left to right
                    if (mapLine-1) %4 != 0:
                        for _ in range(self.piecesPerLine - 1):
                            self.drawNothing()
                
                self.drawLine()
                        
            
            #-----------------------------------------------
            #Keep note how many pieces has already been drawn
            #-----------------------------------------------
            
            if mapLine %2 == 0:
                piecesDrawn += self.piecesPerLine
            else:
                piecesDrawn += 1
            
            mapLine += 1

            
        
    
    def drawPlayer(self, player):
        self.line += '| {} |'.format(player.getName()[0:3].capitalize())
    
    def drawRuin(self, ruin):
        if ruin.isBlank():
            self.line += '|  x  |'
        else:
            self.line += '|  {}  |'.format(ruin.getLevel())

    
    def drawEmpty(self):
        self.line += '|     |'
        
    def drawNothing(self):
        self.line += '       '
        
    def drawLine(self):
        print(self.line)
        self.line = ''



if __name__ == '__main__':
    testMap = Map()
    testMap.generateRuins()
    testPlayers = []
    
    
    p1 = Player('Alfa')
    p2 = Player('Beta')
    p3 = Player('Gamma')
    
    p1.setLocation(9)
    p2.setLocation(12)
    p3.setLocation(3)
    
    testPlayers.append(p1)
    testPlayers.append(p2)
    testPlayers.append(p3)
    
    
    testMap.pickUpRuinsFrom(5)
    testMap.pickUpRuinsFrom(0)
    testMap.pickUpRuinsFrom(25)
    
    pen = MapDrawer(testMap, testPlayers)
    pen.draw()
    
    