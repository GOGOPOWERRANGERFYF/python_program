'''
TCP/IP协议栈是一系列网络协议的总和

应用层                                                 |HTTP数据|
(HTTP FTP SMTP)         

操作系统提供socket API

传输层                                          |TCP首部|HTTP数据|
(TCP UDP)

网络层                                   |IP首部|TCP首部|HTTP数据|
(IP ARP 路由器)

数据链路层                     |以太网首部|IP首部|TCP首部|HTTP数据|
(以太网 网桥)

物理层
电信号传输(光纤 双绞线 无线电波)

《计算机网络教程 自顶向下方法》 1.2.2 TCP/IP协议簇 更容易理解
目前我个人不严谨不成熟的理解:
    socket编程(用python实现)
    个人设置 IP协议版本 TCP/UDP:流格式报文(SOCK_STREAM)/用户数据报报文(SOCK_DGRAM)
    数据链路层以下的(包含数据链路层)不需要我们自己设置
'''
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
# 根据已经创建的socket对象,这里创建的是TCP连接
# socket对象的accept()方法返回的是TCP连接对象和客户端地址端口
while True:
    # 个人心得:
    #   本质就是socket连接,只不过是根据http协议来通信,仅为个人理解,不保证正确性
    #   http协议要通过socket实现应用
    # http协议
    # 返回一个socket连接(对象), 客户端地址
    http_connect, address = fyf_socket.accept()
    # 服务器接收到的请求报文 对象的recv(1024)方法读取请求报文
    # 1024byte 1kb
    print(http_connect.recv(1024), '\n', address, '\n')
    # 响应报文
    # b'byte string' 字节串
    #http_connect.send(b'HTTP/1.1 200 OK\r\n\Content-Type:text/html; charset=utf-8\r\n\r\n')
    http_connect.send('HTTP/1.1 200 OK\r\n\Content-Type:text/html; charset=utf-8\r\n\r\n'.encode('utf-8'))
    #http_connect.send(b"<h1>Hello, This is fyf website!</h1>")
    http_connect.send("<h1>Hello, This is fyf website!</h1>".encode('utf-8'))
    http_connect.close()
