import socket
import threading

host = '127.0.0.1'  # Server's IP address
port = 12345        # Server's port

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Function to receive messages from the server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Handle exceptions such as disconnection
            print('An error occurred.')
            client.close()
            break

# Function to send messages to the server
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

# Get nickname from user
nickname = input("Enter your nickname: ")

# Start threads for receiving and sending messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()