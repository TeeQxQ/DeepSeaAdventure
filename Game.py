from Airtank import Airtank
from Dice import Dice
from Map import Map
from Player import Player
from Ui import Ui
import random

MIN_NOF_PLAYERS = 2
MAX_NOF_PLAYERS = 6

class Game:

    def __init__(self, airtankSize=25, mapSize=16):
        self.airtank = Airtank(airtankSize)
        self.players = []
        self.currentPlayer = 0
        self.currentRound = 0
        self.maxNofRounds = 3
        self.ui = Ui()
        self.dices = [Dice(3), Dice(3)]
        self.map = Map(mapSize)
        #self.server = DeepSeaAdventureServer('192.168.0.102', 1234)


    def start(self, useUI=True, AIPlayers=0):
        
        #-----GAME PREPARATIONS-----
        
        #Welcome messages
        if useUI:
            self.ui.welcome()
        
        #Create and clear a map
        self.map.generateRuins()
        
        #Initialize the airtank
        self.airtank.fill()
        
        #Clear players:
        self.players = []
        self.currentPlayer = 0
        self.currentRound = 0
        
        #Create AI players
        AICount = 0
        while AICount < AIPlayers:
            name = 'AI{}'.format(AICount)
            self.addPlayer(name, True)
            AICount += 1
        
        if useUI:
            self.ui.printNofAIPlayers(self.getNofAIPlayers())
        
        #Create normal players
        if useUI:
            playerCount = 0
            lowLimit = max(0, MIN_NOF_PLAYERS - self.getNofAIPlayers())
            highLimit = min(MAX_NOF_PLAYERS, MAX_NOF_PLAYERS - self.getNofAIPlayers())
            playersToBeAdded = self.ui.askNofPlayers(lowLimit, highLimit)
            while playerCount < playersToBeAdded:
                self.addPlayer(self.ui.askNewPlayerInformation(playerCount + 1))
                playerCount += 1
        
        #-----ROUNDS-----
        
        
        while self.currentRound < self.maxNofRounds:
            
            self.ui.printRoundInfo(self.currentRound+1)
            
            
            #Fill the airtank
            self.airtank.fill()
            
            
            '''
            while not self.airtank.isEmpty:
                #1 REDUCE AIR
                self.airtank.consume(self.players[self.currentPlayer].getNofRuins())
                
                #2 DECLARE TURN
                if not self.players[self.currentPlayer].hasTurned():
                    willTurn = self.ui.askIfPlayerWillTurn()
                    if willTurn:
                        self.players[self.currentPlayer].turn()
                
                #3 ROLL THE DICE
                
                #4 SEARCH
            
            '''
            
            self.currentRound += 1
        
        #-----GAME CONCLUSION-----
        
        #TODO
        
        
        if useUI:
            self.ui.goodbye()
            

    def addPlayer(self, name, isAI=False, addRandomly=True):
        newPlayer = Player(name, isAI)
        
        if addRandomly:
            self.players.insert(random.randint(0, self.getNofPlayers()), newPlayer)
        else:
            self.players.append(newPlayer)

    
    def getNofPlayers(self):
        return len(self.players)

    
    def getNofAIPlayers(self):
        count = 0
        for player in self.players:
            if player.isAI():
                count += 1
        
        return count
                
    
if __name__ == '__main__':
    game = Game()
    #game.start()
    game.start(True, 2)

