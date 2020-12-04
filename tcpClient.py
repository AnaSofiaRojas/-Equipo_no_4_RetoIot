#comunicacion entre Arduino y la computadora
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#sock.SOCK_DGRAM
s.connect(("104.244.42.1", 80))
s.send(b'GET / HTTP/1.1\r\n\r\n')
data=s.recv(1024)
print(data)
s.close()