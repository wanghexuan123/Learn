'''1.os：主要用到查找现在文件的绝对路径
现在的项目的名称：hipython，根据现在的文件路径获取项目根目录路径？
绝对路径：每次都要从最开始的地方查找 D:\Program Files\PyCharm Community Edition 2020.1.2\PycharmProjects\hiPython\xuexi.demo\demo_1.py
相对路径：依据现有的路径进行查找 D:\Program Files\PyCharm Community Edition 2020.1.2\PycharmProjects\hiPython'''
import os
demo_1=os.path.dirname(os.path.abspath(__file__))
print(demo_1)
#找到dir_name的文件夹
root_path=os.path.dirname(demo_1)
print(root_path)
#判断文件是否存在，如果存在你就创建
'''if not os.path.exists(dir_name):
    os.mkdir(dir_name)'''
'''2.文件读写
f=open(file_path,mode='r',encoding='utf-8')
f.read()  #读取文件，根据光标读取内容. seek()
f.readlines()  #列表.
f.close() #关闭文件 
既想读取又想写入  #w+ 先写后读'''
file_path=os.path.join(demo_1,'wanghexuan.txt')
f=open(file_path,'w+',encoding='utf-8')
f.write('wangheshi is 帅哥')
f.close()
f=open(file_path,'r',encoding='utf-8')
print('读取',f.read())
f.close()
3.异常处理
try：
    执行
except Exception as e： #Exception 通用；具体：TypeError，NameError
    print(a)
    #下面抛出的异常，我要告诉程序，报一个错误，终止这个程序
    raise NameError
except TypeError as c: #捕获多个异常，继续添加except
    print(c)
finally：
    #无论你有没有报错，程序是否正常执行，都会执行的语句
# with open(file_path,'w+',encoding='utf-8') as f:  #自动帮忙关闭
    f.write('langlang')
'''
方法：类里面的函数就叫方法
函数和方法

方法和属性的关系：
属性：特征，名词
方法：行为，动作，动词

方法和方法之间的相互调用
带有self参数的方法叫做实例方法
self 可以修改，占位子的，但是强烈不建议修改-->规范

没有self的方法：
1.静态方法：self.
就是表示刚刚好放在类下面的普通函数
只是为了方便管理我们的代码
静态方法的调用：self.方法 obj.方法
类名.方法

类方法：
cls.-->类本身，类自己
类方法的调用，类.方法名  实例.方法名

类方法：主要用来做备用的构造函数
实例方法：用的最多
静态方法：有提示的时候
'''
class Dalao:
    favor='python'
    def __init__(self,name):
        self.name=name
    @staticmethod
    def eat(food):
        print('大佬喜欢吃{}'.format(food))
        return '大佬喜欢吃{}'.format(food)
    def offer(self,money,food):
        print('恭喜{}拿到{}的offer'.format(self.name,money))
        food = self.eat(food)
        print(food)
    @classmethod
    def code(self):
        print('我喜欢的编程语言是{}'.format(Dalao.favor))


dalao = Dalao('wanghexuan')
dalao.offer()
'''总结：
什么是方法：类下面的函数，表示类或者对象的行为；

方法和方法之间如何调用-->和普通函数差不多，前面要加前缀，

静态，实例，类方法'''

1.什么是类？
具有相同特征的某一些事物的种类，集合

类的定义：
class 类名（）
    类的内容
    类体

类名表示：
-类名也是标识符
-字母，数据，下划线，且不能以数字开头
-不能是关键字
-大驼峰式命名：BigBoss，小驼峰命名(别的语言当中)：bigBoss
-APILanglang Apilanglang

2.什么是对象
对象就是类当中的一个成员。TODO：如何表示某一个成员
#类定义
class BigBoss：
   pass
#类的使用，类的实例化，对象化，类的初始化
#可以使用整个
print(BigBoss)
#使用类当中的一个成员。 TODO：对象，实例，东西，object
print(BigBoss())

#类的属性：包括类属性和实例属性
类属性：类集体的属性

类属性：所有成员都具备的特征
类里面表示的变量，就是属性
类属性又称为类变量

类属性的获取：
1.类名.属性名

类属性的修改：类名，属性名=新的属性值

实例属性，实例变量：表示类成员自己独有的特征，并不会是每个类成员都具备的

如何去定义一个具体的对象：
具体的对象的定义，会在类的下面定义固定的函数名称：__init__()
初始化对象的时候：类名(参数1，参数2，参数3)
初始化对象定义的时候：__init__(self，参数1，参数2，参数3)
总结：具体对象使用的时候实际上是调用__init__函数
__init__函数 返回值只能是none，不能是其他事-->规定

如何表示实例属性：
实例属性的定义：在__init__里面：self.属性名=属性值
实例属性的使用：实例名称(不是类名) .属性名
实例属性的修改：实例名称.属性名=new 属性值

self：是在类的定义当中，表示实例自己。我自己

class a:
    #属性
    code_level='goog'
    hair='thin'
    def __init__(self,name,food):
        print(name)
        print(food)
        #return None
    #定义具体的对象，初始化函数，初始化方法
    def hello_word(self):
        #实例方法
        print('哇哇哇哇')
        return '正常'
    pass
#获取类属性“
print(a.hair)
print(a.code_level)

a.code_level='wo'
print(a.code_level)

#print(hair)
#初始化对象，实例化对象，对象生出来
#baby=a('wao','cao')
#print('code_level',baby.code_level)
