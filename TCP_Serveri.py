from socket import *
import time
from random import randint

print("Server-FIEK")
print("Rrjeta Kompjuterike")
print("--------------------\n")

serverPort = 9000
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))
serverSocket.listen(1)


print("Serveri eshte i gatshem per pranim te te dhenave")
#qeky o funksioni qe e merr ip 
def getIP():
    ip = gethostbyname(gethostname()) 
    return ip

def getPort():
    port=getsockname()
    return port

def Keno():
    keno=[randint(0,80) for i in range (0,20)]
    for n in range(20):
        return keno

def Time():
  ora= time.ctime()
  return ora

def HOST():
    host = gethostname()
    return host

def getPrint():
    port=getPrintname()
    return port

def prapa(fjala):
    if len(fjala)<=1:
        return fjala
    return prapa(fjala[1:])+fjala[0]




def faktoriel(n):
    rez = 1
    while n>0:
        rez *= n
        n -= 1
    return rez
def zanoret(ch):
    return "aeiouyAEIOUY".count(ch)>0
def numriZanoreve(fjala):
    numri=0
    for ch in fjala:
        if zanoret(ch):
            numri=numri+1
    return numri
def konverto(opcioni,numri):
    if opcioni=="CELSIUSTOKELVIN":
        kelvin = 273.15 +numri
        return kelvin
    elif opcioni == "KELVINTOFAHRENHEIT":
        fahrenhajt = (numri*9/5)-459.67
        return fahrenhajt
    elif opcioni == "CELSIUSTOFAHRENHEIT":
        fahrenhajt = 32 + (numri*9/5)
        return fahrenhajt
    
    elif opcioni == "KELVINTOCELSIUS": 
          celsius = numri - 273.15
          return celsius
    elif opcioni == "POUNDTOKILOGRAM":
        kilogram = numri*0.45359237
        return kilogram
    elif opcioni == "FAHRENHEITTOCELSIUS":
        celsius = (numri -32)*5/9
        return celsius
    elif opcioni == "KILOGRAMTOPOUND":
        pound = numri/0.45359237
        return pound
    elif opcioni == "FAHRENHEITTOKELVIN":
        kelvin = (numri + 459.67) *5/9
        return kelvin
    
    

mesazhiIP =str(getIP())
mesazhiPORT = str(serverPort)
mesazhiHOST = str(HOST())
mesazhiKoha=str(Time())
mesazhiKeno=str(Keno())



while True:
    connectionSocket, addresa = serverSocket.accept()
    sherbimi = connectionSocket.recv(1024).decode("ASCII")
    sherbimiUP = sherbimi.upper()
    if(sherbimiUP == "IP"):
        connectionSocket.send(mesazhiIP.encode('ASCII'))
    elif (sherbimiUP == "PORT"):
        connectionSocket.send(mesazhiPORT.encode('ASCII'))
    elif (sherbimiUP == "HOST"):
        connectionSocket.send(mesazhiHOST.encode('ASCII'))
    elif (sherbimiUP=="KOHA"):
        connectionSocket.send(mesazhiKoha.encode('ASCII'))
    elif (sherbimiUP=="KENO"):
        connectionSocket.send(mesazhiKeno.encode('ASCII'))  
    elif "PRINTO" in sherbimiUP:
        connectionSocket.send(sherbimiUP.encode("ASCII"))
        fjala=connectionSocket.recv(1024).decode("ASCII")
        connectionSocket.send(str(prapa(fjala)).encode("ASCII"))
    elif "ZAN" in sherbimiUP:
        sherbimi,fjala=sherbimiUP.split(' ')
        mesazhiZANORE=str(numriZanoreve(fjala))
        connectionSocket.send(mesazhiZANORE.encode("ASCII"))
    elif "FAKT" in sherbimiUP:
        sherbimi,vlera=sherbimi.split(' ')
        vleraInt = int(vlera)
        mesazh=faktoriel(vleraInt)
        mesazhiFAKTORIEL=str(mesazh)
        connectionSocket.send(mesazhiFAKTORIEL.encode("ASCII"))
    elif "KONVERTO" in sherbimiUP:
        sherbimi,opcioni,vlera=sherbimiUP.split(' ')
        vleraInt= int(vlera)

        mesazhiKonverto=str(konverto(opcioni,vleraInt))
        connectionSocket.send(mesazhiKonverto.encode("ASCII"))
    connectionSocket.close()