import socket

PORT = 12_000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind(('', PORT))
    print("server listen on port %d" % PORT)
    
    while True:
        message, clientAddress = server.recvfrom(2048)
        server.sendto(message.upper(), clientAddress)
    