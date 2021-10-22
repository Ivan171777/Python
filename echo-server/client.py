import socket
#создаем сокет
sock = socket.socket()
sock.connect(('localhost', 1777))
#подключаемся к сокету
while True:
#в цикле обрабатываем запрос клиента и если он вводит выход, останавливаем цикл
    a = input()
    if a == 'exit':
        break
    b = bytes(a, encoding='utf-8')

    sock.send(b)
#отправка данных на сервер (по 1024 байта)
    data = sock.recv(1024)
#выводим данные
    print (data)

sock.close()
