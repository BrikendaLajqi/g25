from socket import *
import sys
import time
print("Klienti-FIEK")
print("Rrjeta Kompjuterike")
print("--------------------\n")

print("Shkruaj se cilin sherbim deshironi")

while True:
    serverName = "127.0.0.1"
    serverPort = 9000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))


    sherbimi = raw_input()
    sherbimi=sherbimi.upper()
    if sherbimi == "exit":
        break
    clientSocket.send(sherbimi.encode('ASCII'))
    pergjigjiaServerit = clientSocket.recv(1024)
    print "Pergjigjia nga serveri:", pergjigjiaServerit.decode('ASCII')
clientSocket.close()