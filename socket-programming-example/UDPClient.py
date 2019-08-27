from socket import *

serverPort = 12000
serverName = "10.90.2.154"
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Enter the message ").encode()
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddr = clientSocket.recvfrom(1024)
print(modifiedMessage.decode())
clientSocket.close()
