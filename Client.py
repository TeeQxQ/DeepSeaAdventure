# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 18:52:49 2018

@author: Teemu
"""

import socket
import sys

from Ui import Ui

#Constants:
MSG_SIZE = 1024
MSG_NOF_PLAYERS = 'MNP'
MSG_BREAK = 'MBR'

class DeepSeaAdventureClient():
    
    def __init__(self, name, serverAddress, serverPort):
        self.name = name
        self.serverAddress = serverAddress
        self.serverPort = serverPort
        
        #Create and connect a socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    
    def connect(self):
        try:
            self.sock.connect((self.serverAddress, self.serverPort))
            return True
        except ConnectionRefusedError:
            print('Game server is currently offline')
            return False
    
    def send(self, msg):
        self.sock.sendAll(msg)
    
    def recv(self):
        return self.sock.recv()
    
    def sendAndRecv(self, msg):
        self.send(msg)
        return self.recv()
    


if __name__ == '__main__':
    ui = Ui()
    ui.welcome()
    name = ui.askNewPlayerInformation()
    
    if len(sys.argv) > 1:
        address = sys.args[1]
    else:
        address = 'localhost'
    
    print('Let\'s connect to the game server..')
    client = DeepSeaAdventureClient(name, address, 1234)
    if not client.connect():
        print('Closing the game...')
        print('Closed')
        sys.exit()
        
    print('Connected to the game server!')
    print(client.sendAndRecv(MSG_NOF_PLAYERS))
    client.send(MSG_BREAK)
    
    