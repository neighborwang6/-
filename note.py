
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
                        
                        
                        
                        
                        
                        
                                 
                                 
                                 
                                 
                                 
