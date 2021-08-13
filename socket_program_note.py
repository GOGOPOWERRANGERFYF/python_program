import re
# website 网站
# site 地点
# application 应用
# url uniform resource locator 统一资源定位符
# division 分开,分隔,除法等...    div划分(计算机)

# header + body

# regular 规则的,有规律的,经常做的
# regular expression 正则表达式,计算机科学的一个概念 
# 正则表达式通常被用来检索,替换那些符合规则(模式)的文本
# 例如:seq和grep两个工具
# 正则表达式 ^开头 $结尾
print('string character\n')
# reverse v 颠倒,使完全相反,撤销
#         n 反面
#         adj 反面的;相反的
print(r'string character\n')
# 加r后字符串中的转移序列\n被反转成为字面意思
# (?P<name>) 分组匹配?p<组名> pattern 
string_a = 'AAAaaa123'
re1 = re.search(r'[0-9]{3}', string_a)
print(re1)

# def func(a, b) 位置参数   
# def func(*a)  可变参数
# def func(**a) 关键字参数,
#   a=1按照关键字传入
#   否则无法传入
#   的参数被封装成dict字典{a1:1}
def func1(**a):
    print(a)
func1(a=1)
func1(b=1)
# 命名关键字参数
def func(*, a, b):
    print(a, '+', b)
func(a=1, b=2)


# pattern 模式,方式,范例
# url pattern url规则

# wsgi web server gateway interface 
#     python 编写web server和web app的接口规范

# b'abc123' 字节串
# 'abc123' 字符串
# http协议
# 请求协议(客户端-->服务端,浏览器-->服务器)
#   请求格式(报文):
#       请求行: 方法(get/post) URI(统一资源标识符/xxx/xx) 协议版本(HTTP/1.1)       
#       请求头:请求首部字段
#       内容实体/请求正文
#   请求行/r/n请求头/r/n请求头/r/n/r/n请求正文(报文本质:字节串,当然,字节串和字符串之间可以转换)
#
#   报文预览(文本):
#       请求行
#       请求头
#       请求头
#
#       请求体/请求正文
#
#   注意:GET请求没有请求体,POST有
#        GET方法提交数据时,位于请求首行URI后:以?分割URI(URL),参数之间以&相连
#        请求首行:(方法GET)(URl:/xx/xx?提交的数据:参数&参数)(协议版本HTTP/1.1)/r/n请求头/r/n请求头/r/n/r/n请求体
#        GET方法提交的数据大小有限制(因为浏览器对URL有长度限制)
#        POST方法提交的数据放请求体
#        POST方法提交的数据大小没有限制
#   补充知识:URL是URI的子集
#           URI:统一资源标识符,例如 每个人的身份证号 
#           URL:统一资源定位符,例如 地址协议://xx省/xx市/xx区/xx街道xx号/某某人
#           URI资源的唯一编号
#           URL以地址来确定资源,用定位的方法实现URI
#
# 响应协议
#   响应格式(报文)
#       状态行
#       响应头:响应首部字段
#       响应体/响应正文
# 状态行/r/n响应头/r/n/r/n响应正文
# 协议版本 状态码 状态码的原因短语/r/n首部字段/r/n/r/n响应正文
# HTTP/1.1 200 ok/r/nContent-Type:text/html/r/n/r/n<h1>标题</h1>

# 从socket到wsgiref
# socket核心:
#   通过调用系统socket
#   1. 创建socket
#   2. 监听socket连接
#   3. 创建socket连接(服务端:被动接收连接)
# wsgiref核心:
#   编写业务代码主要处理:
#   1. 接收已解析请求报文
#   2. 封装和发送响应报文


# 流程: 创建虚拟环境-->创建工程-->创建应用

# python虚拟环境
# debian: sudo apt install python3-venv
# venv在3.8以上版本中
# 可直接通过命令创建虚拟环境
# python3 -m venv 文件夹名称
# 
# 激活
# source 文件夹名称/bin/activate
# virtualenv 的一个最大的缺点就是,
# 每次开启虚拟环境之前要去虚拟环境所在目录下的
#  bin 目录下 source 一下 activate......
# 
#  停用激活:
#      deactivate
#      或直接删除文件夹
# 
#      python3 -m IPython

# shell:< python3
# shell:< import django
# shell:< django-VERSION

# 执行模块的命令
# python3 manage.py runserver


# 第一步: 创建工程/项目:
#     django-admin startproject 工程名/文件夹
#         manage.py 管理程序的文件. 启动和结束等,工程管理脚本
#         settings.py 配置文件
#         urls.py 路由系统 url和其处理函数的对应关系
#         wsgi.py 指定框架的wsgi
#     一个项目(project):
#     app
#     app
#     app
#     ...
#     至少包含一个app
# 
# 第二步: 创建app
#     在工程根目录下创建app
#     django-admin startapp app/文件夹
#     /migrations 数据库相关
#     __init__.py 包
#     admin.py    数据库后台
#     apps.py     把app和项目关联起来的文件
#     models.py   模型:数据库操作
#     tests.py    单元测试
#     views.py    视图:业务逻辑代码
# 
# urlpatterns 网址格式
#     浏览器/客户端 ---> urls.py ---> app/views.py
#         |____________<_____________<__| 返回给客户端
# 
# django下一次客户端请求:        
#     1.匹配路由  路由分发器查找用户请求的url --> 与url绑定的视图函数
#         a.找到业务/视图函数,调用
#         b.找不到,返回404
#     2.业务函数,执行业务逻辑
#     3.返回数据给浏览器/客户端
# 
# 代码编写:
#     1.在urls.py编写路由
#     2.在app的views.py编写业务函数
#         2.1编写业务代码
#         2.2通过直接操作HttpResponse类返回数据给浏览器/客户端
#     3. python3 manage.py runserver 0.0.0.0:8000
# 
# method:
# get 从后端取数据
# post 前端提交数据(post提交账户和密码是非明文的)
# 
# 一般的框架: MVC modle view controller (模型,视图,控制器)
# 1.modle 一般对应数据库操作
# 2.view 业务逻辑处理+数据展示
# 3.controller

# django框架: MTV(modle view templates)
# 1.modle     构建和操纵web应用的数据
# 2.view      负责处理用户的请求并返回响应
# 3.templates 渲染向用户呈现的信息(数据展示)
# 
#                              urls.py                       提取>     提取>
# 用户/浏览器--(输入访问URL)-->URL控制器---------->在views.py<-->modles<-->数据库
#      |                       根据URL对应的视图函数  |      <返回     <返回
#      +--<<<-----template-----<<<-(要展示的数据)-----+
#                 (html文件)        数据库读取的

# 路由系统:
# 1.静态路由
# 2.动态路由

# csrf cross-site request forgery 跨站请求伪造
# 一种web攻击方式(详细的有需要再搜索了解)