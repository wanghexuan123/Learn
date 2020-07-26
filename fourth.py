'''def a(*args):
    b=1
    for c in args:
        b*=float(args)
        return b % 20
print(a(nums_list))'''
#模块名称：模块名称是一个标识符
#标识符命名规则：
'''1.数字，下划线，字母，不能以数字开头，不能用关键字命名
2.模块名称命名一般是使用下划线的形式命名，驼峰
3.模块名称不能和python内置的模块名称重合
random，内置模块，那么我们命名自己的模块的时候，就不要使用random
包：python3 新版本，不带__init__.py 同样可以作为包使用(包带有__init__.py文件的文件夹)'''
#模块导入
#from 模块名称 import 类名，函数名，变量名   适用于项目根目录/内置模块
from time import time
from random import random
print(time())
#print(randint(1,99))
#from（项目根目录开始） 包名.包名.包名.模块名 import 类名，函数名，变量名    适用于我们自己定义的
#from（项目根目录开始） 包名.包名 import 模块名
#使用的时候，模块名，函数名
'''如果出现了重名的函数，那么要使用别名；函数名称很长，要使用别名
公式为：from 模块名称 import 类名，函数名，变量名 as alias_name'''
#import 只能是模块名(as 别名) 内置函数
#调用 模块名.函数名（）
#import 包名.包名.模块名
'''
__file__ :这个模块的路径

__name__:如果当前模块是用来作为程序运行的脚本文件，（入口文件）
__main__:表示运行python文件的模块名
如果不是程序运行的脚本文件，是作为模块导入其他地方的
包名，模块名
'''
if __name__ == '__main__':
    pass
#当py文件被作为脚本(入口)执行的时候，if下面的代码会执行
#如果py文件是被导入其他的模块 if下面的代码不会执行
#from 包.模块 import * （通配符，所有的）---导入非常混乱，很容易造成名称冲突，所有强烈不建议使用
'''如果是直接用别人已经写好的模块或者是包，可以直接导入
如果不是python内置的：放到项目下面，作为一个包或者模块导入'''
#os模块是别人写好的，python内置的
#主要处理系统相关的
#os.path 处理系统路径相关的
import os
#pwd 显示当前文件路径；你在哪里运行的python指令，这个路径就是当前文件路径；每次都会变，取决于你在哪里运行的python
#print(os.getcwd())
#如果我们想每次得到的都一样，要用绝对路径
#print(os.path.abspath(__file__))
#获取文件的文件夹名称
#print(os.path.dirname(os.path.abspath(__file__)))
#路径拼接
a=print(os.path.dirname(os.path.abspath(__file__)))
#print(os.path.join(a,'wang.txt'))
'''创建文件夹
data_path=os.path.join(a,'data')
os.mkdir(data_path)
#是否是一个文件夹
print(os.path.isdir(data_path))
#是否是一个文件
print(os.path.isfile(a))
#路径是否真的存在
print(os.path.exists(data_path))'''
'''如何读取文件：
1.打开文件，内置函数open（）
open（path/文件名称，mode=‘r’，encoding：编码规则）
#根据指定的编码格式读取
#编码是根据一定的规则将计算机内部的机器字节转化成人能看懂的字符串
#编码：string-->byte
#解码：byte-->string
mode：‘r’，读取；'w',写入，当已经存在这个文件的时候，原来文件的内容会被覆盖；‘a’，追加
‘b’，binar，二进制，图片，视频
‘t’，文字模式
2.读取
3.关闭文件,一定要关闭文件（数据不对，或者写入内容不生效，文件无法再次打开）'''

a = os.path.dirname(os.path.abspath(__file__))
b = os.path.join(a,'wanghexuan.txt')
f = open(b,encoding='utf-8')
print(f.read())
f.close()
#读取文件
#写入
'''f=open(b)
f.write('真帅')
f.close()'''
dir_name = os.path.dirname(os.path.abspath(__file__))
wanghexuan = os.path.join(dir_name,'wanghexuan.txt')
f=open(wanghexuan,encoding='utf-8')
#readline()只会读取一行
'''while True:
    line=f.readline()
    if not line:
        break
    print(line)'''
#readlines()
a=f.readlines()
for i in a:
    print(i,end='')
#异常：程序无法按照预计结果开始走
#一旦程序报错了，程序将停止运行，
'''
try:
    我要执行的肯恶搞出现错误的代码
    当没有出现情况，那么try就会执行
    一旦出现错误，立即跳到except里面
except：异常类型(默认就是所有的类型，语法错误除外) as e
     e：错误信息
     出现异常以后要运行的代码
'''
a=input('请输入数字1：')
b=input('请输入数字2：')
try:
    print('hello')
    print(a*b)
    print('world')
except Exception as e:
    print('这里有一个bug',e)

try:
    print('hello')
    print(a*b)
    print('world')
except IndexError:
    print('index error')
except TypeError:
    print('bug')
#错误类型
#1.NameError
#print(abc)
#2.IndexError
#rint(['a','b'][100])
'''
为什么不直接使用默认的捕获
不方便定位问题
不确定是什么原因造成的异常
一般不使用默认的，而是会加入异常类型
'''
