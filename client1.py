import socket

HEADER = 64
PORT = 5050
NAME = 'client1'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))

while True:
    msg = client.recv(HEADER).decode(FORMAT)
    if(msg == '1001'):
        print('Do you have anything to send, press 1 for yes; 0 for no ')
        flag = True
        temp = ""
        while(flag):
            temp = input()
            if(temp == '1' or temp == '0'):
                flag = False
            else:
                print('Invalid input, try again')

        client.send(temp.encode(FORMAT))
        if(temp == '1'):
            temp = input('Enter your messaage: ')
            client_msg = temp.encode(FORMAT)
            client.send(client_msg)
    elif(msg == '1002'):
        print('Server sending the data')
        msg = client.recv(HEADER).decode(FORMAT)
        print(msg)
