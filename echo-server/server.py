import socket
#создаем сокет
sock = socket.socket()
#назначаем номер порта
sock.bind(('',1777))
#прослушивание
sock.listen(1)

conn, addr = sock.accept()    
#принимаем подключение
while True:   
    data = conn.recv(1024)    
    if not data:
        break       
    conn.send(data.upper())
#получаем данные для клиента
#выходим из сокета    
sock.close()
