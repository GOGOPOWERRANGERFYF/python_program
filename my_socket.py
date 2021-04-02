# tcp/ip协议
# tcp
# udp
# http hypertext transport protocol
# TLS transport layer security 传输层安全协议
# SSL securce sockets layer 安全套接字层

# API application programming interface 应用程序接口
# socket是我们进行网络编程最基本的API,由系统提供,不同的系统有区别
# 其中windows平台的区别最大

# tcp/ip五层模型
#   应用层
# (socket api)
#   传输层
#   网络层
#   数据链路层
#   物理层

# 导入socket库
import socket

# 服务器端
def main():
    # TCP/IP 
    # transmission control protocol/internet protocol
    # 传输控制协议/网络协议
    # SOCK_STREAM
    # IP(网络协议):控制数据如何从源头到目的地,即"路由". 
    # AF_INET   ipv4
    # AF_INET6  ipv6
    #
    # UDP
    # (gram:克)
    # user datagram control protocol
    # 用户数据报协议/网络协议
    # SOCK_DGRAM
    #
    # AF_INET address family(地址族) _ inet(使用ipv4进行通信)
    # AF_INET6 使用ipv6进行通信
    # SOCK_STREAM 提供面向连接的稳定数据传输,即TCP协议
    # socket类,my_socket为socket类socket函数的实例
    # 建立一个socket类对象my_socket
    # socket类的socket方法(函数)
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    # socket函数创建连接
    # tcp连接创建的是双向通信,双方都可以同时给对方发数据,谁先发谁后发,怎么协调,
    # 要根据具体协议来决定
    # http协议规定客户端先发请求给服务器,服务器收到后才发数据给客户端

    # 服务器进程首先要绑定一个端口来监听其他客户端的请求/连接
    # 小于1024的端口必须有管理员权限才能绑定
    # bind 捆绑
    # 实参传入一个元组tuple = ()
    # 127.0.0.1为本机地址,或使用localhost
    my_socket.bind(('127.0.0.1', 9999))
    # 一个socket通过:客户端地址,客户端端口,服务器地址,服务器端口
    #                来唯一确定一个socket

    # 调用listen()方法来监听端口,传入实参指定等待连接的最大数量
    my_socket.listen(10)

    # 等待浏览器/客户端访问
    while True:
        # python特有语法,accept()返回两个结果
        # 用两个变量接收两个返回值...
        # 我了个去...还能这样...你厉害...你是爷...你是我大哥...
        # accept 接收
        # receive 收到
        fyf_connect, fyf_address = my_socket.accept()
        # 对象.recv(1024)   接收的1024个字节
        print(fyf_connect.recv(1024))
        print("web app address:port", fyf_address)

        # 给浏览器/客户端返回数据
        # 根据http协议规定:
        # 返回给浏览器/客户端的报文头
        # http状态码(status code): 200表示请求成功
        fyf_connect.send(b'HTTP/1.1 200 OK\r\n\
            Content-Type:text/html; charset=utf-8\r\n\r\n')
        # 返回给浏览器/客户端的内容
        # b byte字节
        # 单引号和双引号在python中并无区别,都可以用来表示一个字符串
        #fyf_connect.send(b"This is fyf connection!")
        fyf_connect.send("<h1>This is fyf connection!</h1>".encode("utf-8"))
        fyf_connect.send("<p><time>9:00</time></p>".encode("utf-8"))

        # 关闭和浏览器/客户端创建的连接
        fyf_connect.close()

# __name__为python内置属性,变量
# 直接运行本py文件时,__name__为"__main__"
# 被导入时,__name__为模块名
if __name__ == "__main__":
    main()

# WSGI (web server gateway interface)是一种规范
# 它定义了使用python编写的web app与web server(socket服务端)之间的接口格式
# 实现web app与web server间的解耦

# 我们可以直接使用现成的实现WSGI的模块
# 例如: wsgiref,uwsgi,werkzeug