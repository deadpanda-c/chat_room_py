from socket import socket

def define_the_pseudo():
    print(s.recv(1024).decode())
    pseudo = input("")
    s.send(pseudo.encode())

HOST = "127.0.0.1"
PORT = 4444
try:
    s = socket()
    s.connect((HOST, PORT))
    define_the_pseudo()
    input()
except:
    print("Hummmm, it seems it's broken :(")
    exit(84)