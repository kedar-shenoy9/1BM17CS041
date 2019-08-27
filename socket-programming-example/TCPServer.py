from socket import *

serverPort = 12000
serverName = '10.90.2.154'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	sentence = sentence.decode()
	capSentence = sentence.upper()
	connectionSocket.send(capSentence.encode())
	connectionSocket.close()
