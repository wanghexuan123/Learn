'''
方法：类里面的函数就叫方法，表示类或者对象的行为；
函数和方法：

方法和属性的关系：
属性：特征，名词
方法：行为，动作，动词
方法和方法之间的相互调用：和普通函数差不多，前面要加前缀，
带有self参数的方法叫做实例方法，(self可以修改，占位子的，但是强烈不建议修改)
没有self的方法：1.静态方法：self，就是表示刚刚好放在类下的普通的函数，只是为了方便管理我们的代码，静态方法的调用：self.方法  obi.方法 类名.方法
'''

class Dalao:
    favor='python'
    def __init__(self,name):
        self.name=name
    @staticmethod
    def eat(food):
        print("大佬喜欢吃{}".format())
        return "大佬喜欢吃{}".format()
    def offer(self,money,food):
        print("恭喜{}拿到{}的offer".format(slef.name,money))
        food=self.eat(food)
    @classmethod
    def code(cls):
        print("我喜欢的编程语言是{}".format(Dalao.favor))
'''
定义一个手机类，具有打电话和录音的功能，打电话的时候可以录音，也可以不录音
class Phone:
   def __repr__(self):
   返回对象打印出来的效果，名字固定用法
     return self.model
'''
'''类的继承
1.功能机，智能手机
是否 phone 里面所有的属性和方法 smartphone都可以使用
pyone >>> smartphone  phone 是父亲
如何继承
class 类名(父类名)：
  pass
继承以后，子类可以使用父类的所有属性和方法
如果父类和子类具有相同的方法和属性，子类会使用自己的方法和属性，重写
’‘’  
class Phone:
  def call(self)
    print('正在打电话')
  def send_msg(self)
    print('正在发短信')
class SmartPhone:
  #def call(self)
   # print('正在打电话')
  #def send_msg(self)
   # print('正在发短信')
  def caputure_video(self):
    print('正在视频')
smart = SmartPhone
smart.call()
多重继承：子类可以同时继承多个父类，这些父类所有的特性(属性，方法)子类都可以使用
用法：
class 子类名(父类1，父类2，父类3):
  pass
类名： 类名():  类名(object):
所有的类都是继承自object类的
所有的类都是object的子类
如果所有的父类都具有同样的一个方法，继承顺序的问题：1.找自己 2，根据代码当中继承的父类的先后顺序查找
菱形问题钻石问题>>>广度优先，深度优先  C3算法 ; 查找顺序-- print(__mro__)
超继承>>> super()就是表示调用父类的call()方法
debug>>>调试：1.最简单的方式 print();缺陷print(a) 调试完还要删除 
2.出完问题，先print() 百度
3.打断点，优先使用的调试
如何使用debug模式：
1.小虫子的标记，断点配合起来使用
2.断点：程序运行到红点的地方，会暂停
step into：进入对应的代码

getattr:获取属性(动态获取某个属性的函数);获取属性，获取属性如果不存在，会报错
getattr(对象或者类名，属性名称，当没有此属性的时候，需要提供的默认值)
类名，类属性; 类名，实例属性>>>是错误的

setattr:设置属性(动态获取某个属性的函数)----字典
setattr(对象或者类名，属性名称，赋值的新值)
不管属性存不存在，都会赋值给新值
#有时候我们提前不知道属性名称是什么，是从别的地方拿过来的
#测试用例：Excel ，method:get，
---
接口基础：什么是接口
1,前后端构成的桥梁
2,数据通道
我们所谓的接口概念：web api
API:应用程序可编程接口 application programing interface
硬件接口：两个不同的东西连接的桥梁，不同的事物就可以进行数据通信；例句：usb，耳机口，水龙头
软件接口：用户界面 UI，user interface(用户接口)
http://api.github.com/login  是接口
run函数  是接口，可以被访问的函数
def run():
    return'hello'
接口：
from flask import Flask
app = Flask(__name__)
@app.route("/login") #接口地址，@装饰器
def login():
    return "我很帅"
#login()
#/login地址 和 login函数 绑定在一起
#访问  /login 地址的时候，函数会被调用
---
什么是网络请求？
print("网路请求")

1.在设备上输入URL地址，发送请求参数
设备，浏览器，postman，jmeter，手机，电视，python，客户端(user client)
主动发送的都是客户端。
2.服务器：接受并响应请求。 被动接收，不能主动发送。
HTTP请求：
1.请求首行。请求的概要信息。
2.请求头
3.请求体
面试题：你会的请求方法
GET,POST,PUT,DELETE,OPTION,HEAD
域名地址 / IP
域名地址：好记。
IP-->HTTP：TCP/IP
IP地址：门牌号，邮编号：精确的找到我想到的地方
域名和ip有对应关系吗？
DNS 解析
get和post的区别？
请求参数在url里面，请求参数在body里面，
请求头：
User-Aent 用户代理，客户端是什么，用什么代表你
content-type:请求数据格式
HTTP:无状态
cookie：让无状态有状态。存在浏览器中
请求响应：
1.响应首行
2.响应头：conten-type 返回数据的格式。set-cookie name=wanghexuan
3.响应体
响应状态码：2XX 成功类，行为被成功地接受，理解和采纳 3XX 重定向类，为了完成请求，必须进一步执行的动作
4XX 客户端错误类，请求包含语法错误或者请求无法实现
500 服务端内部错误。最常见的原因是服务器内部挂了
cookie，session和token的区别？
cookie：让服务器记住你，存储在浏览器
session：在服务器记住用户信息状态的，验证。服务器验证
token：令牌，跨平台。只要他有这个令牌，不管他是什么身份，手机，浏览器，电视
保存在客户端本地，local_storage
输入url后的过程？
域名解析，DNS解析-->IP地址(分层级)；发起TCP连接的三次握手，建立连接；建立TCP连接后发起http请求；服务端响应http请求，返回响应报文；浏览器页面渲染，展示；断开TCP
连接，四次挥手。
三次握手，四次挥手？
第一次握手：建立连接时，客户端向服务端发送请求报文(SYN)，“我想建立连接”
第二次握手：服务器收到请求后，如同意连接，则向客户端发送确认报文(SYN/ACK)“同意建立”
第三次握手：客户端收到服务器的确认后，再次向服务器发送确认报文，完成连接(ACK)
三次握手主要是为了防止已经失效的请求报文字段发送给服务器，浪费资源。
第一次挥手：客户端向分手，发送消息(FIN)给服务器
第二次挥手：服务器通知客户端已经接受的挥手请求，返回确认消息(ACK),但还没做好分手准备
第三次挥手：服务器已经做好分手准备，通知客户端(FIN)
第四次挥手：客户端发送消息给服务端(ACK)，确认分手，服务器关闭选择







'''
