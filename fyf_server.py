import socket

# tcp/ip协议
# 创建一个socket(对象)
# TCP/IP协议    transmission control protocol/internet protocol
# TCP socket(对象)  SOCK_STREAM 流格式套接字
# UDP socket(对象)  SOCK_DGRAM  数据报格式套接字
fyf_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
fyf_socket.bind(('127.0.0.1', 8800))
fyf_socket.listen(100)

# 循环的测试条件一直为真,所以一直执行循环体
while True:
    # 个人心得:
    #   本质就是socket连接,只不过是根据http协议来通信,仅为个人理解,不保证正确性
    #   http协议要通过socket实现应用
    # http协议
    # 返回一个socket连接(对象), 客户端地址
    http_connect, address = fyf_socket.accept()
    # 服务器接收到的请求报文 对象的recv(1024)方法读取请求报文
    print(http_connect.recv(1024), '\n', address, '\n')
    # 响应报文
    # b'byte string' 字节串
    #http_connect.send(b'HTTP/1.1 200 OK\r\n\Content-Type:text/html; charset=utf-8\r\n\r\n')
    http_connect.send('HTTP/1.1 200 OK\r\n\Content-Type:text/html; charset=utf-8\r\n\r\n'.encode('utf-8'))
    #http_connect.send(b"<h1>Hello, This is fyf website!</h1>")
    http_connect.send("<h1>Hello, This is fyf website!</h1>".encode('utf-8'))
    http_connect.close()

