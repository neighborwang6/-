
# -
杂乱的笔记
2.1编程的过程和规范
例：一个python的代码片段
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

"""  2.2良好的编程习惯  """
#看：阅读优秀的代码，学习别人的代码
#问：http://github.com/seajs/seajs/issues/545
#练：亲自动手写代码，实践，实践，再实践。






                                 
                                 
                                 
                                 
                                 
