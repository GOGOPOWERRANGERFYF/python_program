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

# 第一个形参接收http请求报文,请求报文(字节串)已经解析并且封装在一个字典里
# 
# 第二个形参接收一个函数(封装响应报文的函数)
#def WebApp(environ, start_response):
def WebApp(http_request, http_response):
    #浏览器发送了两次请求:1.URI标识的资源
    #                   2.favicon.ico (浏览器标签的图标)
    #print(http_request)
    url_path = http_request.get('PATH_INFO')
    print(type(http_request), url_path)

    # 封装响应报文的：状态行,响应头
    http_response('200 OK', [('Content-Type', 'text/html')])
    #start_response('200 OK', [('Content-Type', 'text/html')])

    # 补充一个知识点:
    # 如果浏览器缓存里面有favicon.ico的话就不会再发ico的请求报文
    if url_path == '/favicon.ico':
        with open('./icons/favicon.ico', 'rb') as file_object:
            response_body = file_object.read()
    else:
        response_body = b'<h1>Welcome to my web site!</h1><h1>go on</h1>'

    # 封装响应正文
    # 函数返回一个列表list
    return [response_body]

# 实例化一个make_server对象
# 实现功能: 封装socket,socket对象
http_server = make_server('127.0.0.1', 8000, WebApp)

print('server start... port:8000')

#        socket连接对象
# 实现功能: connect.accpet() 监听连接...
http_server.serve_forever()
