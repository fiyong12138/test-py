#注释1
'''注释3'''
"""注释2"""

from tkinter import W


print("helloword!")

#input("\n\n 按下回车退出") #在输入前打印“”内字符 然后等待输入
#一行内写多个语句时 用；隔开
print("num",end="") #输出后不换行

if True:    #首字母大写才为真
    print ("true")
  #print("true")    同一个代码块的语句必须包含相同的缩进空格数
else:
    print("false")  

num=1+2+\
    3   #用\实现多行        变量没有类型    所存对象才有类型
num1=[1,2,4,     #但【】 {} （）可直接多行
      4,6,7]
a=b=c=1 #多个赋值

word='单引号和双引号没有区别'
words="""
    用来定义多行字符串
      """
print('this is a line\n')
print(r'this is a line\n')  #r让反斜杠不发生转义
print('-------------------list的用法-------------------')
list=[1,2,3,4,5,6]
print(word[2:])#输出第三个开始到最后  -1为倒数第二个
print(word*2+'123') #   * 输出2次 +连接字符串
print(list[2:3])#=print (list[2]) 但后者没有中括号  因为前者类型为list
print(word[::2])    #输出全部 步进2
print(word[-1::-2])     #倒序输出 步进2
num1[3]='a'   #修改列表
print(num1)
num1[1:4:2]='14'    #连续修改
print(num1)
""" 列表的内置方法
l=[]
添加方法：append、insert和extend
l.append((‘Jerry‘,5))
l.insert(2, ‘哈喽‘)
l.extend([‘Lily‘, False, (234, 567)])需要传入一个可遍历对象(list、tuple或字符串等)

删除方法：clear、pop和remove
l.clear() 清空列表
v1 = l.pop()  默认弹出最后一个
l.remove(‘haha‘) 参数为要删的对象

其他方法：cpoy、count、index、sort
v = l.copy() 浅拷贝
v = l.count(True)计算某个元素在列表中出现的次数
v = l.index(True,3,8) 从第3个到第8个查找True
l.sort()  同类型元素按ascii码值排序
l.sort(key = lambda x: x.lower()) 使用key来指定一个按照每个元素的小写字母进行排序
lambda  行内匿名简单函数
l_tuple = [(‘haha‘, 23), (‘yuyu‘, 15), (‘oiui‘, 32), (‘erer‘, 53)]

l_tuple.sort(key=lambda x: x[1], reverse=True)

print(l_tuple)

打印结果：

[(‘erer‘, 53), (‘oiui‘, 32), (‘haha‘, 23), (‘yuyu‘, 15)]
"""

#函数返回多个元素时一般为元组return a,b=return (a,b)，但可以手动指定返回类型return [a,b]
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )  #元组可以为空 且不能进行元素修改 
#tuple的元素不可改变，但它可以包含可变的对象，比如list列表
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
#string、list 和 tuple 都属于 sequence（序列）。

print('-----集合使用大括号 { } 或者 set() 函数---集合在Python内部通过哈希表实现，其本征无序-----')
a = set('abracadabra')
b = set('alacazam')
print(a)# 输出集合，集合是无重复元素的序列，重复的元素被自动去掉
# set可以进行集合运算  
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

print('-----列表有序---字典无序，用键来存取-------')
dict = {}
dict['one'] = "1 - 菜鸟教程"  
dict[2]     = "2 - 菜鸟工具"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'} 
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

dict={x: x**2 for x in (2, 4, 6)} #字典推导式 {2: 4, 4: 16, 6: 36}
for k,v in dict.items():  #直接输入 dict 的键值
    print(k,":",v)
"""
 dict(d)创建字典时，d只要全为(key,value)就可以
 dict_2 = dict({('a',1),('b',2),('c',3)})#元素为元组的集合
 dict_3 = dict([['a',1],['b',2],['c',3]])#元素为列表的列表
 dict_4 = dict((('a',1),('b',2),('c',3)))#元素为元组的元组

 字典因为其key唯一性，所以也不会出现相同元素
"""

print("--------------------Python3 数据类型转换-------------")
x=1+1.2 #x输出结果为2.2 隐式转换
y = int(2.8) # y 输出结果为 2 显式类型转换
z = int("3") # z 输出结果为 3













