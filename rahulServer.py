import socket
import threading

port = 8980

s = socket.socket()
print("Socket successfully created")
s.bind(('', port))
print("Socket binded to", port, "port")

def handle_client(conn, addr):
    while True:
        response = conn.recv(1024).decode('UTF-8')
        print('Client:', response)

        if (response.lower() == 'exit'):
            reply = "Good Bye!!!"
            print("Server:", reply)
        else:
            reply = input('Server: ')

        conn.send(reply.encode('UTF-8'))
        # conn.close()

        if (response.lower() == 'exit'):
            break

def start():
    s.listen(5)
    print("Socket is listening")
    conn, addr = s.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print('Server is listening... ')
start()
