import random
#rangint函数
a=random.randint(1,10)
print(a) #生成的随机数：1<=n<=10
b=random.randint(4,4)
print(b) #结果永远是4
#c=random.randint(51,50)
#print(c) #该语句是错误的，下限必须小于上限
#练习
'''a=input('one')
b=input('two')
c=input('three')
max_num = a
if a<b:
    max_num=b
if max_num<c:
    max_num=c
print(max_num)'''
'''#九九乘法表
for i in range(1,10):
    for j in range(1,10):
        if j<=i:
         print('{}*{}={}'.format(j,i,j*i),end='\t')
    print()'''
#python定义函数
'''
def 函数名称（参数1，参数2，参数3）：
    （缩进）函数体
    函数体里面的内容函数外面看不到
    外面能看到的（函数名，参数值（输入），返回值（输出））
    return 返回值
'''
def add(x):
    # x 是参数；输入；吃东西
    y = x+1
    # return 返回；拉东西
    return y
y=add(2) # x=2
print(y)
def ceshi(o,u):
    p=u+1
    return {'a':p,'b':o}
print(ceshi(6,9))
#print：将某一个值打印（输出）到屏幕上面
#return：函数定义体里面拉出来的东西
'''函数：存储一段可以重复执行的程序
#1.程序的使用更加简洁
#2.可以重复使用
#3.代码具有可读性， 一读函数和注释我就知道这段代码的作用'''
my_list =[12,3]
b=my_list.append('hello')#函数定义的时候没有return：返回值；默认返回None(ctrl+鼠标左键，查看函数的定义)
c=my_list.pop(1)#函数定义的时候有return：返回值
print(b)
print(c)
'''函数定义的参数和实际传入的参数个数要相等，而且顺序要相等
#函数定义的参数：形式参数，x，y，z
#函数调用的参数：实际参数，实际的值，1,2,3
#TODO:函数体里面的内容只有当函数被调用的时候才会执行'''
'''def definition_name(params1,params2): #形式参数
    #函数体
    #函数体里的内容在外部无法查看
    return vaule '''
def dalao(name):
    new_name='DALAO'+name
    return new_name
    #函数体里面函数遇到return就会终止，不会再往下面运行。
    print('王贺选是个大佬')
    print('大家要向他学习')
new = dalao('连长')
print(new)
'''return 注意:
def a(height):
    if height > 185:
        return '帅'
    print('丑')
    if height < 34:
     return '矮'
    print('高')
    return '普通人'
a(190)
a(173)'''
#位置参数：形式参数和实际参数要根据位置(顺序)一一赋值
#函数的定义和函数的调用，参数要一一对应
#形式参数要赋值-->实际参数
#形式参数和实际参数是一个萝卜一个坑
def dalao(name,money,food='榴莲'):
    print('王贺选{}，拿到了一个{}'.format(name,money))
    print('{}喜欢吃{}'.format(name,food))
    return
dalao('真棒','A+','wa')
#关键字参数：把实际参数赋值给形式参数
#关键字参数的好处：1.换顺序 2.可以部分作为关键字参数，部分作为位置参数 注：关键字参数必须放在位置参数的后面
#dalao(money='B+','真棒',food='good')
dalao('真棒',money='B+',food='good')
#默认参数：作用在于可以少传参数
#当函数调用的时候有默认参数，那么在调用的时候，这个默认参数可以不传实际参数，使用默认参数作为实际参数
#food='榴莲'
dalao('王贺选','随便',food='榴莲')
#函数在定义的时候可以复杂，在调用的时候要简单（好记，少传参数）
#默认参数也必须要放在位置参数的后面
#默认参数和关键字参数的区别：默认参数是对于形参，函数定义的时候；关键字参数对函数调用
#不定长参数： 我不知道需要定义多少参数
def sum_total(a,b,*args):
    #*args 表示剩下的多余的参数，可以以任意字母来定义：*a，*b
    #在函数定义里面，你可以用*args去接收多余的位置参数
    #在函数定义里面，args是元祖
    print(args)
    total=0
    c=total+a+b
    for i in args:
        c +=i
    return c
print(sum_total(1,2,3,4))
#在函数的调用中，也可以用*vaule(余下来的实际参数)
#可以是列表，也可以是元祖。  注：序列类型，脱了衣服都一样
rest={3,3,3}
#解包-->脱衣服
print(sum_total(1,2,*rest))
#关键字不定长参数  **kwargs
def ceshi(c,d,*args,**kwargs):
    #**kwargs 表示接收多余的关键字参数
    #函数体里面kwargs是字典的形式接收多余的关键字参数
    print(args)
    print(kwargs)
other_info={'姓名':'王贺选','外貌':'真帅'}
ceshi(3,4,5,6,age=18,**other_info)
#函数的相互调用
def a():
    name ='王贺选'
    waimao='帅了'
    b(name,waimao)
def c(name,sex):
    print('{}最喜欢吃{}'.format(name,sex))
    return
def b(name,waimao,sex='雪糕'):
    print('{}真的太{}'.format(name,waimao))
    c(name,sex)
    return #注：return返回/不返回值，跟print打印没关系
a()
#1.当所有的函数没有被调用之前，函数的定义顺序没有关系
#2，一单某一个函数被调用，那么函数体如果调用了其他的函数，那么这个其他的函数必须在调用之前
#3.函数体内定义的变量-->局部变量，只能在函数体里面生效
# #函数体外面的变量-->全局变量，我能不能在函数体里面去使用？可以
name = '王贺选'
def dalao():
    name='andy'
    print('{} is dalao'.format(name))
dalao()
#函数的参数是局部变量
#id()查看某个值或者变量在内存当中的地址

#全局变量和局部变量的修改
#局部变量能在函数体当中被修改吗? 可以
#局部变量能在函数体外面被修改吗? 不可以
#全局变量能在局部变量中函数体里面被修改吗? 可以，需要用到global
name = '王大锤'
def dalao():
    name='王大锤'
    name='wanghexuan'
    print('{}is dalao'.format(name))
dalao()

#不能获取局部变量，更不用说修改了
name = '王小锤'
def dalao():
    name='王大锤'
    print('{}is dalao'.format(name))
dalao()

name='贺选'
def dalao():
    global name
    name=name+'真帅'
    print('{} is shuaige'.format(name))
print(dalao())
print(name)
#global 全局变量声明，但是现阶段不建议使用golbal
#global 造成数据紊乱
#内置函数：python自己内部放置的函数，python自己定义，不需要我们去定义的函数
#print(),input(),len(),max(),type(),range(),min(),id(),sorted(),enumerate(),eval(),sum(),round(),zip()
#print(help(range))
#模块导入
#什么是模块，module 就是一个python文件，一个模块里面会有很多的函数，类
#包，package 就是一个python文件的文件夹，会有一个或多个模块 注：包含一个__init__.py模块的文件夹
#标准库，第三方库：实现特定功能的代码集合，可以是一个模块，也可以是一个包，多个包
#模块导入的作用
#improt 的关键字