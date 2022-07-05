#导入整个模块
import sys
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python的路径为',sys.path)
#模块具体函数导入写法   from time import *  导入全部函数 接下来直接调用 sleep（1）
from sys import path
print('第二次打印路径',path)


import os
#i=os.system("cls") #清屏命令

