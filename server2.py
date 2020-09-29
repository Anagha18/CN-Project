import socket
localIP     = ""
localPort   = 12001
bufferSize  = 1024
#otherPort=12001
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#UDPServerSocket1 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
#UDPServerSocket1.bind((localIP, otherPort))
print("UDP server up and listening")
# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode()
    address = bytesAddressPair[1]
    if(message=="Q"):
    	UDPServerSocket.close()
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    print(clientMsg)
    # Sending a reply to client
    #UDPServerSocket.sendto(bytesToSend, (localIP, 12001))
   # UDPServerSocket1.sendto(bytesToSend, address)

