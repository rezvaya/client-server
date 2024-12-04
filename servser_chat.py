import socket
import threading

host = '0.0.0.0'  # Listen on all interfaces
port = 12345      # Choose a port number

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print(f'Server is listening on {host}:{port}')

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            # Remove clients that are disconnected
            clients.remove(client)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove the client and nickname if an error occurs
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            print(f'{nickname} has left the chat.')
            broadcast(f'{nickname} has left the chat.'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        # Request and receive nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of client is {nickname}')
        broadcast(f'{nickname} joined the chat.'.encode('ascii'))

        # Start handling thread for the client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()