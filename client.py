import socket
serverAddressPort   = ("", 12000)
bufferSize          = 1024
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
#msgFromServer = UDPClientSocket.recvfrom(bufferSize)
#msg = "Message from Server {}".format(msgFromServer[0])
#UDPClientSocket.sendto(bytesToSend, serverAddressPort)


#print(msg)
#bytesToSend=input('Enter sentence')

while(True):
		equ=input("Please give me your equation (Ex: 2+2) or Q to quit: ")
		if(equ=="Q"):
			break
		bytesToSend = str.encode(equ) 
		UDPClientSocket.sendto(bytesToSend, serverAddressPort)
		'''result = UDPClientSocket.recvfrom(bufferSize)
		if result == "Quit":
			print("Closing client connection, goodbye")
			break
		elif result == "ZeroDiv":
			print("You can't divide by 0, try again")
		elif result == "MathError":
			print("There is an error with your math, try again")
		elif result == "SyntaxError":
			print("There is a syntax error, please try again")
		elif result == "NameError":
			print("You did not enter an equation, try again")
		else:
			print("The answer is:", result)'''
  	

