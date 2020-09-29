import socket
localIP     = ""
localPort   = 12000
bufferSize  = 1024
otherPort=12001
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#UDPServerSocket1 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
#UDPServerSocket1.bind((localIP, otherPort))
print("UDP server up and listening")
# Listen for incoming datagrams
while(True):
	try:
		bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
		equation = bytesAddressPair[0]
		address = bytesAddressPair[1]
		if equation == "Q" or equation == "q" or equation == "Quit" or equation == "quit" or equation == "quit()":
			bytesToSend = str.encode("Quit")
			UDPServerSocket.sendto(bytesToSend,(localIP,12001))
			UDPServerSocket.close()
			#UDPServerSocket.sendto(bytesToSend,(localIP,12000))
			break
		else:
			print("You gave me the equation:", equation.decode())
			result = eval(equation)
			bytesToSend = str.encode(str(result))
			UDPServerSocket.sendto(bytesToSend,(localIP,12001))
			#UDPServerSocket.sendto(bytesToSend,(localIP,12000))
	except (ZeroDivisionError):
			bytesToSend = str.encode("Zero Error")
			UDPServerSocket.sendto(bytesToSend,(localIP,12001))
			#UDPServerSocket.sendto(bytesToSend,(localIP,12000))
	except (ArithmeticError):
			bytesToSend = str.encode("Math Error")
			UDPServerSocket.sendto(bytesToSend,(localIP,12001))
			#UDPServerSocket.sendto(bytesToSend,(localIP,12000))
	except (SyntaxError):
			bytesToSend = str.encode("Syntax Error")
			UDPServerSocket.sendto(bytesToSend,(localIP,12001))
			#UDPServerSocket.sendto(bytesToSend,(localIP,12000))
	except (NameError):
			bytesToSend = str.encode("Name Error")
			UDPServerSocket.sendto(bytesToSend,(localIP,12001))
			#UDPServerSocket.sendto(bytesToSend,(localIP,12000))
		

  
               
