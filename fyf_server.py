import socket

# tcp/ip协议
# 创建一个socket对象
fyf_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
fyf_socket.bind(('127.0.0.1', 8800))
fyf_socket.listen(100)

while True:
    # http协议
    # 返回一个socket连接(对象), 客户端地址
    http_connect, address = fyf_socket.accept()
    # 服务器接收到的请求报文 对象的recv(1024)方法读取请求报文
    print(http_connect.recv(1024), '\n', address, '\n')
    # 响应报文
    #http_connect.send(b'HTTP/1.1 200 OK\r\n\Content-Type:text/html; charset=utf-8\r\n\r\n')
    http_connect.send('HTTP/1.1 200 OK\r\n\Content-Type:text/html; charset=utf-8\r\n\r\n'.encode('utf-8'))
    http_connect.send("<h1>Hello, This is fyf website!</h1>".encode('utf-8'))
    http_connect.close()

