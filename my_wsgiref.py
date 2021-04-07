# WSGI web server gateway interface 
# 
# web应用 
# web框架
# web服务 
# socket(套接字)
# 
# wsgiref模块功能: 
#   按照http协议解析请求数据(报文)
#   按照http协议封装响应数据(报文)
#   本质就是处理字节串
#   例如:将请求报文解析后赋值给一个字典dict={"path":"/xxx/xx",...,......}

# wsgiref包的simple_server模块
# make_server函数
from wsgiref.simple_server import make_server

# 第一个形参接收http请求报文,一个字典
# 第二个形参接收一个函数(封装响应报文的函数)
def WebApp(http_request, http_response):
#def WebApp(environ, start_response):
    http_response('200 OK', [('Content-Type', 'text/html')])
    #start_response('200 OK', [('Content-Type', 'text/html')])
    # 函数返回一个列表list
    return ["<h1>Welcome to my web site!</h1>".encode('utf-8'), "<h1>go on</h1>".encode('utf-8')]

http_server = make_server('127.0.0.1', 8000, WebApp)
print('server start... port:8000')
http_server.serve_forever()
