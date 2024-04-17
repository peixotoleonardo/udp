import io
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    message = input('Input lowercase sentence: ')
    
    client.sendto(message.encode('utf-8'), ('127.0.0.1', 12_000))
    
    response, _ = client.recvfrom(2048)

print(response)
