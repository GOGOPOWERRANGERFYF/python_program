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
# 