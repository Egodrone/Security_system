#! /usr/bin/python3
import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = "11.11.11.11" //external IP
host = "22,22,22,22"
port = 8000
print (host)
print (port)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            savedData = self.sock.recv(1024).decode('utf-8')
            if(len(savedData) != 0):
                print('Client sent:', savedData)
                print(len(savedData))
                self.sock.send(b'Oi you sent something to me'
		# Write data to the file
                with open('data.txt', 'a') as file:
                    file.write(savedData + "\n")

serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
