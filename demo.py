############################# СЕРВЕРНАЯ ЧАСТЬ
import socket

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Биндим сокет к адресу и порту
server_socket.bind(('0.0.0.0', 12345))

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
