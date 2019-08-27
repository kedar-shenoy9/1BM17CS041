from socket import *

serverName = "10.90.2.154"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print("The server is ready to receive ")
while True:
	message, addr = serverSocket.recvfrom(1024)
	message = message.decode().upper().encode()
	serverSocket.sendto(message, addr)
	
