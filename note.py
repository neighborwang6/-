
# -
Python的学习笔记

"""
2.1编程的过程和规范
例：一个python的代码片段
"""
def main()
  """
      主函数，返回0表示成功
  """
  try：
          with open('cat.pic','rb')as fin:
              if fin.seek(0,2)!=400*400*3: #判断文件长度是否满足要求
          print("输入文件cat.pic不符合要求")
                  return -1
              fin.seek(0)
              try:
                  try:
                      with open('cat.pic','wb')as fout:
                  #下面是图像转换的算法实现。彩色图像到灰色图像的转换主要利用
                  #RGB色彩空间到YUV色彩空间的变换公式来取得灰度值Y，公式是
                  #Y=0.299R+0.578G+0.1148B
                  for i in range(400):
                                 for j in range (400):
                                 b=ord(fin.read(1))
                                 g=ord(fin.read(1))
                                 r=ord(fin.read(1))
                                 y=(299*r+587*g+114*b)/1000
                                 fout.write(char(y))
                    except IOError as e:
                        print("打开文件cat2.pic时错误")
                        return -1
        except IOError as e:
            print("打开文件cat.pic时错误")
            return -1
        return 0
      
#Python 编程规范：语句
print("Hello,world!");    #不要在行尾加分号

for i in range(n):
  result+=i
#不要使用制表符（tab）进行缩进，千万不要混用tab与空格，应使用4个空格进行缩进

class book_shelf:    #类的命名应该为驼峰风格且首字母应该大写，这里应该是BookShelf
  pass

bookShelf=BookShelf()    #变量名应该是下划线风格，这里应该是bool_shelf


f=open('output.txt','w')    #使用文件时候应注意显示地调用close(),或使用with
                            #with open('output.txt','w')as if:
                            #pass

if n>5:print(n)    #每一行只写一条语句，该换行就换行，一定不要吝啬换行
  else:n=6

#import语句应该遵循的原则：
#import次序：先import Python 内置模块，在import第三方模块，最后import自己开发项目中的其他模块；这几种模块中用空行分割开来。
#一条import语句import一个模块。
#当从模块中import多个对象且超过一行时（一般建议一行不超过80个字符），使用如下断行法（py2.5以上版本）：
from module import(obg1,obj2,obj3,obj4,obj5,obj6)
#不要使用from module import* 导入模块的所有内容，除非是import常量定义模块或其他你确保不会出现命名空间冲突的模块。

#Python还有很多灵活的用法，使用时应注意删繁就简。
#Python的列表推导简洁方便，但仅应在简单的情况下使用
[s['name']for s in students if s['age']>18]#正确
[(x,y)for x in range(m)for y in range(n) if x**2+y**2>=4]#错误
#Python的条件表达式是if语句的简短语法规则，但同样仅应在简单的情况下使用
return s['name']if s['age']>18 else s['nickname']#正确
return s['name']if s['age']>18 else s['nickname']if s['age']>14 else 'anonymous'#错误
#Python还有一些很“酷”的特性，但奇淫技巧的代码会难以开发调试维护

"""
请参考Google Python Style Guide: 
http://google.github.io/styleguide/pyguide.html
以及Python之禅道（The Zen of Python）
打开Python交互式解释器并输入import this即可查看
"""
import this

"""
****************************************2.2良好的编程习惯****************************************
"""
#看：阅读优秀的代码，学习别人的代码
#问：http://github.com/seajs/seajs/issues/545
#练：亲自动手写代码，实践，实践，再实践。
"""
Python 的模块化设计主要包括函数，类，模块，包四种类型
每个py文件就是一个模块，其中还可以导入其他的模块，一些模块还可以作为启动程序独立运行

"""
#案例：生命游戏

#地图模块
#逻辑模块
#⏲模块

#python程序的异常处理
try:
  do_something()
except KeyboardInterrupt:
  exit (0)
except IOError as e:
  print("IO failed:",e)
  
  
#Ctrl+C的方式终止程序

""" Python代码分析工具 """
#Pylint功能：检查代码是否符合PEP8规范，检查代码中是否存在常见的错误和违反最佳实践http://pylint-messages.wikidoc.com.all-messages检查重复的代码
#Pylint的安装与使用
#Pylint安装：pip install-U pylint #安装最新版的Pylint#
#Pylint使用：pylint[options]module_or_package_or_file#对模块/包/文件运行pylin
                   #options:
                          #--rcfile=<file>指定检查的配置文件
                          #--ignore=<file>不进行检查的文件列表
                          #--disable=<msg ids>关闭某种类型的检查
                          #-f  <format>报告类型，如html
""" 
例：凯撒密码的加密和解密
"""
#coding=utf-8

import string

shift=3
choice = input("would you like to encode or decode?")
word = (input("Please enter text"))
letters = string.ascii_letters+string.punctuation+string.digits
encoded ="
if choice =="encode":
  for letter in world:
    if letter=='':
      encoded=encoded+''
    else:
      x=letters.index(letter)+shift
      encoded+encoded+letters[x]
if choice=="decode":
  for letter in word:
    if letter=='':
      encoded=edcoded+''
    else:
      x=letters.index(letter)-shift
      encoded=encoded+letters[x]
      
print(encoded)

"""  
****************************************2.4代码的静态检查****************************************
"""
#code Review


"""
****************************************2.5代码的性能分析****************************************
"""

#效率
#代码性能优化
#数据结构、算法
#实践效率、空间效率

#改进算法，选择合适的数据结构
#良好的算法对性能起到关键作用，因此性能改进的重要点是对算法改进
#算法的时间复杂性的排序依次是O(1)->O(lg n)->O(n^2)->O(n^k)->O(k^n)->O(n!)
#对成员的查找访问等操作，字典（dictionary）要比（list）更快
#集合（set）的并、交、差的操作比列表（list）的迭代要快
#循环优化的基本原则：尽量减少循环过程中的计算量，在多重循环的时候，尽量将内层的计算提到上一层。
#字符串的优化：Python的字符串对象是不可改变的。字符串连接的使用尽量使用join()而不是+。当对字符串可以使用正则表达式或者内置函数处理时，选择内置函数。
#使用列表解析和生成器表达式：列表解析要比在循环中构建一个新的list更为高效，因此可以利用这一特性来提高程序的效率。

"""
****************************************2.6结对编程实践****************************************
"""

#结对编程就是两名程序员在同一台电脑前结对编写解决同一问题的代码。例如领航员和驾驶员、长机和僚机、驾驶和副驾驶。
    #口渴指数是核实伙伴交流程度的一个考核标准
    #领航员需要给驾驶员一点时间
    #主动参与
    #坚持代码标准、流程规范
#并不是所有的项目都需要结对编程
    #最大限度发挥领航的价值
    #与个人性格有关
#实例：生命游戏
    #cell_maprange
  CELL_DEAD = 0
  CELL_ALIVE = 1
  
  @staticmethod
  def chenck_integer(n,min=None,max=None):
    if not isinstance(n,int) or not isinstance(min,int) or not isinstance(max,int):
      rsise TypeError("Type.Error:int")
    if min and n < min:
      raise RangeError("Range error:min")
    if max and n > max:
      raise RangeError("Range error:max")

#构造函数     
def __init__(self,rows,cols):
    """Inits GameMap with row and column count.
    Validate all the parameters: integer,range[1,???]
    """
    GameMap.check_integer(row,1)
    GameMap.check_integer(cols,1)
    self.size = (rows,cols)
    self.size = (rows,cols)

def get_neighbor_count_map()
def set_map()
def print_map()
  """
  
  """
  
    
    
    
