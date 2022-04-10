

# un serveur qui va mettre en relation les deux clients
# deux clients qui peuvent communiquer ensemble

from socket import socket

def define_the_pseudo(client):
    client.send("[*] Enter your pseudo here: ".encode())
    return client.recv(1024).decode()


HOST = "127.0.0.1"
PORT = 4444
NAME_CLIENT_ONE = ""
NAME_CLIENT_TWO = ""

s = socket()
try:
    s.bind((HOST, PORT))
    s.listen(2)
    client_one, adr_one = s.accept()
    NAME_CLIENT_ONE = define_the_pseudo(client_one)
    print("the pseudo of the client one is: {}".format(NAME_CLIENT_ONE))
    client_two, adr_two = s.accept()
    NAME_CLIENT_TWO = define_the_pseudo(client_two)
    print("the pseudo of the client two is: {}".format(NAME_CLIENT_TWO))
    input()
except:
    print("Roses are red, violets are blue, this code is broken, like my life without you")
    exit(84)
