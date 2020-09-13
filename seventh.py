"""
模块导入
内置模块：python 自己内部写好的模块
自己写的模块；
别人写的魔模块：第三方

requests 仓库，安装
pip install requests
#导入 requests
#import requests
#访问一个url 接口地址，发送一个get请求
#url='http://api.github.com'
#res= request.get(url)
#print(res.text) #<Respinse [200]>
#如何发送 header 请求头
headers ={"token":"123","username":"wanghexuan"}
#如何传递参数，位置参数，或者关键字参数params， 通过？也就是querystring，查询字符串的形式传递
data={"username":"wanghexuan","pwd":"123456"}
#发送post请求(同get请求)
传递参数也可以通过表单形式，json格式 注：content-type 只能有一种形式
response：
获取响应文本，得到的数据类型，string
print(res.text)
获取 进制形式
print(res.content)#方便接收图片之类的
获取 json格式，不是json的响应数据，就会报错，try：except
json 得到的是字典数据类型
print(res.json())
注册接口：
url='接口地址'
header={"x-Lemonban-Media-Type":"lemonban.v1"}
data={"mobile_phone":"88888888888","pwd":"12345678"}
#一定要天机headers 关键字参数，不能以位置参数传递
#因为放到了可变长参数里面
#content-type 不需要添加，为什么？json关键字参数就是便是 content-type =json
#data 关键字参数就是表示：表单格式
#params 参数就是变 query string
登录接口：
#token放在什么地方？可以放到请求体当中吗？根据接口文档，都可以(只是一种协议，开发人员和你之间定义的协议)
#cookie 可以放到请求体当中吗？ HTTP协议



"""
