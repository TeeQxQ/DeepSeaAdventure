# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 19:31:21 2018

@author: Teemu
"""

import socket
import sys
import threading

class DeepSeaAdventureServer():

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.clients = []
    
    def addClient(self):
        self.sock.listen(5)
        print('Server listening for new connection...')
        client, address = self.sock.accept()
        print('New client from {}'.format(address))
        self.clients.append(client)
        clientThread = ClientThread(threadCounter, client, address, self)
        clientThread.start()
        print("New client succesfully added.")
        

    def listen(self):
        threadCounter = 0
        self.sock.listen(5)
        print('Server listening for new connections...')
        while True:
            client, address = self.sock.accept()
            print('New client from {}'.format(address))
            threadCounter += 1
            clientThread = ClientThread(threadCounter, client, address, self)
            clientThread.start()


#Conctants
MSG_NOF_PLAYERS = 'MNP'
MSG_BREAK = 'MBR'

class ClientThread(threading.Thread):

    def __init__(self, threadID, client, address, server):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.playerName = 'unknown'
        self.client = client
        self.address = address
        self.server = server

    #thread.start() will call run()-method
    def run(self):
        self.onlyListen()
        print('Client thread {} exiting'.format(self.threadID))

    def send(self, msg):
        self.client.sendall(msg)

    def onlyListen(self):
        while True:
            cmd = self.client.recv(1024)

            if cmd == MSG_NOF_PLAYERS:
                self.send('99')
            elif cmd == MSG_BREAK:
                break



if __name__ == '__main__':

    PORT = 1234
    host = '192.168.0.102'

    print('Starting TeeQ\'s Deep Sea Adventure game server...')
    print('Host: {}, port: {}'.format(host, PORT))

    server = DeepSeaAdventureServer(host, PORT)
    server.listen()
