############################# СЕРВЕРНАЯ ЧАСТЬ
import socket

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Биндим сокет к адресу и порту
server_socket.bind(('127.0.0.1', 12345))

# Слушаем соединения
server_socket.listen(5)
print("Сервер слушает...")

# Принимаем соединение
client_socket, addr = server_socket.accept()
print(f'Получено соединение от {addr}')

# Получаем данные от клиента
data = client_socket.recv(1024)
print(f'Получены данные: {data.decode()}')

# Отправляем ответ клиенту
client_socket.send(b'Hello, client!')

# Закрываем соединение
client_socket.close()
server_socket.close()

############################# КЛИЕНТСКАЯ часть
import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
client_socket.connect(('127.0.0.1', 12345))

# Отправляем данные серверу
client_socket.send(b'Hello, server')

# Получаем ответ от сервера
data = client_socket.recv(1024)
print(f'Получен ответ: {data.decode()}')

# Закрываем соединение
client_socket.close()