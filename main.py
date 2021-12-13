import socket
import threading
import os

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
CONN = []
ADDRESS = []
THREAD = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clear = lambda: os.system('cls')
def handle_client_poll(conn, addr):
    poll_code = '1001'
    snd_msg = poll_code
    conn.send(snd_msg.encode(FORMAT))
    rcv_msg = conn.recv(HEADER).decode(FORMAT)

    if rcv_msg == '1':
        rcv_msg = conn.recv(HEADER).decode(FORMAT)
        print('Message from {}\n> {}'.format(addr[1], rcv_msg))
    else:
        print('{} does not want to send message'.format(addr[1]))

    '''    
    connected = True
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        if msg == "quit":
            connected = False
        print(f"[{addr}] {msg}")
        temp = "hello world"
        conn.send(temp.encode(FORMAT))
    '''

def handle_client_select(conn, addr):
    poll_code = '1002'
    snd_msg = poll_code
    conn.send(snd_msg.encode(FORMAT))
    temp = input('Server Message for client: {}'.format(addr[1]))
    conn.send(temp.encode(FORMAT))

def poll():
    threads = []
    print('Inside Poll function: ')
    print('size of CONN is: ', len(CONN))
    for i in range(0,len(ADDRESS)):
        print('Sending message to {}'.format(ADDRESS[i][1]))
        thread = threading.Thread(target = handle_client_poll, args = (CONN[i], ADDRESS[i]))
        thread.start()
        threads.append(thread)
    for i in range(0, len(ADDRESS)):
        threads[i].join()


def select():
    threads = []
    print('Inside Select function: ')
    print('size of CONN is: ', len(CONN))
    for i in range(0,len(ADDRESS)):
        print('Sending message to {}'.format(ADDRESS[i][1]))
        thread = threading.Thread(target = handle_client_select, args = (CONN[i], ADDRESS[i]))
        thread.start()
        threads.append(thread)
    for i in range(0, len(ADDRESS)):
        threads[i].join()

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def menu():
    print('1. Poll\n2. Select\n3. None')
    flag = True
    while(flag):
        flush_input()
        temp = input('Enter your choice: ')
        if(temp >= '1' and temp <= '3'):
            flag = False
        else:
            print('invalid input, try again')

    if (temp == '1'):
        poll()
    elif (temp == '2'):
        select()
    else:
        print('none selected')
        
def start():
    server.listen()
    while True:
        print(f"[LISTENING] Server is listening on {SERVER}")
        conn, addr = server.accept()
        CONN.append(conn)
        ADDRESS.append(addr)
        print('New connection at port: ', addr[1])
        flush_input()
        menu()
        print('Here is the end line ')
            #thread = threading.Thread(target=handle_client, args=(conn, addr))
            #THREAD.append(thread)
            #thread.start()


print("[STARTING] server is starting...")
start()
