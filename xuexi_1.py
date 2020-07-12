#two
#列表，字典
#列表作用：存储多个数据，获取单个元素，可读性不强
wanghexuan=["王贺选",18,'男','英雄联盟','王者荣耀']
#获取不记得位置，列表劣势：列表没有标志--key
print(wanghexuan[3])
#字典作用：储多个数据，获取单个元素，有标记--key：value
#表示方法：{key1:vaule1,key2:vaule2}
wanghexuan1={'name':"王贺选",'age':'18','sex':'男'}
print(wanghexuan1['name'])
#key唯一
wanghexuan2={'name':'王贺选','age':'18','name':'大帅哥'}
print(wanghexuan2['name'])
print(wanghexuan2)
#获取长度
print(len(wanghexuan2))
#字典是无序的数据类型，list是有序的
#print(wanghexuan2[2])
#字典是可变类型，增删改
#添加字典元素
wanghexuan2['tianjia']=['哇哦','偶偶']
print(wanghexuan2)
#1.字典里面的双引号与单引号没有区别，自动使用单引号
#2.使用元素修改和元素添加的方式是一样的
#当key值不存在的时候，就是添加元素；当key值存在的时候，修改会覆盖之前的值
wanghexuan2['star']=['大哥']
print(wanghexuan2)
wanghexuan2['star']=['小弟']
print(wanghexuan2)
#随机删除，没有参数的
#wanghexuan2.popitem()
#print(wanghexuan2)
#删除指定的key
wanghexuan2.pop('age')
print(wanghexuan2)
#其他的方法，清除
#wanghexuan2.clear()
#print(wanghexuan2)
#获取所有的字典，把key和value以元祖的形式展示，用来存储数据
print(wanghexuan2.items())
#获取所有的key值
print(wanghexuan2.keys())
#获取所有的value值
print(wanghexuan2.values())
#总结1.无序的，可变的类型 2.key，唯一，不可变类型，value，随意 3.增删改，列表 4.items(),keys(),vaules()
#remove 为什么返回None，pop返回删除的值？ return
#元祖
dalaos=['贺选','男','完美','绝对的']
print(type(dalaos))
#元祖形式，和列表非常相似，元祖用()，列表示[]
dalaos1=('贺选','男','完美','绝对的')
print(type(dalaos1))
#获取某一个元素，索引，和列表一样
print(dalaos1[0])
#获取多个--切片
#元祖不可变，和字符串类似，只能重新赋值
#元祖里面有列表--元祖的不可变是相对的，不是说里面所有的内容都完全不能变；只要看索引前面是不是一个可变的类型
tuple=('王贺选','ceshi',['哇哦','偶偶','嘿嘿'])
#tuple[2]=['新列表']
#print(tuple)
tuple[2][0]='哈哈'
print(tuple)
tuple1=('王贺选','ceshi',{'哇哦':'偶偶'})
#tuple1[2]索引前面是元祖，代表修改的是元祖的元素，不可以
#tuple1[2]='嘻嘻'
#print(tuple1)
#tuple1[2]是字典，可变类型，可以直接修改
tuple1[2]['哇哦']='嘻嘻'
print(tuple1)
#tuple2是列表，可以改变
tuple2=['王贺选','ceshi',('哇哦','偶偶')]
tuple2[2]='hello'
print(tuple2)
#tuple2[2]元祖，不可变
#tuple2[2][0]='youxi'
#print(tuple2)
#存在空元祖
a=()
print(type(a))
#TODO:坑：1个元素的元祖表示，不是一个元祖，而是去掉括号以后的原始数据类型
a1=(1)
print(type(a1))
#如果想表示一个元素的元祖，记得务必在元素后面加一个逗号，
a3=(1,)
print(type(a3))
print(len(a3))
#元祖解包
b,c,d=('wang','he','xuan')
print(b)
print(c)
print(d)
#集合不是键值对；集合是无序的；通过不能索引能获取到；重复的元素直接去掉，集合目前我们使用的最多的功能就是去重
aa={'微微','笑笑','可可','笑笑'}
print(aa)
print(len(aa))
#去重
aa1=list(set({'微微','笑笑','可可','笑笑'}))
print(aa1)
#数据运算
#算数运算：加减乘除
b=1
c=2
print(c-b)
print(c+b)
print(c*b)
#除法运算，python版本有关系，算完以后的数据是float类型
print(type(c/b))
#整除
print(5//3)
#取余--模运算 %
print(8%5)
#幂运算--**
print(2**4)
#在算术运算有一个坑：浮点数运算，不能精确
print(0.1+0.1)
print(0.1+0.2)
from decimal import Decimal
#Decimal能够维持很高的精度；函数里接受的要是字符串形式，不要写成数字形式
print(100.1-0.2)
print(Decimal('100.1')-Decimal('0.2'))
#赋值运算 =
wang = '王'
#+= -= *= /=
wang += 'ceshi'
print(wang)
#类似省略形式
wang=wang+'ceshi'
print(wang)
#比较运算 大于>，小于<，等于=，不等于!=，大于等于>=，小于等于<=
#比较运算等于符号是2个=，得到的结果是布尔值
print(1==3-2)
print(4!='4')
#逻辑运算and not or,得到的结果也是布尔值
#and 并且 同时为真
print(1==1 and 2==2)
print(1==1 and 2==3)
#or 或者 只要有一个为真，就是真
print(1==1 or 2==3)
#not 非，取反的；加括号提高优先级
print(not ((1==1) or (2==3)))
#成员运算 in, not in
#字符串，列表，字典，元祖
print('wang'in'wanghexuan')
print(3 not in [1,2,3])
#字典的in是判断key值，不是vaule
print('wang'in{'name':'wang','age':'12'}.values())
#运算 if...elif...else...
#python 遇到冒号要缩进
aaa=1
print(type(aaa))
#if（条件表达式）：
    #条件语句
#elif（另外的条件）：
if (type(aaa)==int):
    print('我真帅')
elif type(aaa)==float:
    print('哇哦')
# 剩下所有的情况
else:
    print('heihei')
#pass 冒号后语句块里不想执行任何东西
if aaa==1:
    pass
else:
    print('hello')
print('end')
#for 循环执行某一段程序
#循环播放，遍历
songs=['稻香','听妈妈的话','周杰伦','霍元甲']
#songs[0]
#songs[1]
for song in songs:
    #song = songs[0]
    print('正在播放:{}'.format(song))
    #index + 1
#字符遍历
name = "wang he xuan"
for i in name:
    print(i,end='/')
#字典遍历
name = {'namee':'111','sex':'222'}
# 字典默认是获取keys
for ii in name:
    print(ii)
#获取所有的values
for iii in name.values():
    print(iii)
#获取全部的值
a,b=('1','2')
for u,o in name.items():
    print(u)
    print(o)
#while（重点）
#打印无限次的’我喜欢你‘
#while（条件表达式）
wanghexuan_accept=0
while (wanghexuan_accept<10000):
    print('我喜欢迪丽热巴')
    print(wanghexuan_accept)
    wanghexuan_accept+=1
print('已经爱我了')

dilireba_a=0
while True:
    print('我喜欢迪丽热巴')
    dilireba_a+=1
    if dilireba_a ==99:
        print('迪丽热巴拒绝了')
        print(dilireba_a)
        #break以后，循环关系劈裂，退出循环
        break
print('伤心欲绝')

my_list=[('大海','海鸥'),('大陆','老虎')]
for name in my_list:
    #print(name)
    for haha in name:
        print(haha)











