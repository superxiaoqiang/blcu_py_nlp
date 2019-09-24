# Week4 -- Python 基础编程（三）

> ### 课前预习
* 完成week2，3中课堂任务中的练习（建议2020日历打印问题不要使用系统内置calendar库，自己使用列表、字典、循环和打印函数的技巧完成。）
* 预习翻阅[参考书电子](https://python.swaroopch.com/modules.html)中python模块相关的内容

> ### 课堂任务
<b><i>Previously On Week3</i></b> [虫洞](week3_Python_Basics_2.md)
<b><i>Code Review</i></b>

#### 模块与包


##### 模块 module
模块的介绍:模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法.
```
#!/usr/bin/python3
# 文件名: using_sys.py
 
import sys
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
 
print('\n\nPython 路径为：', sys.path, '\n')
```
##### import语句
```
import os
import sys
import time,json
import numpy as np  # 别名
```
##### from ... import语句
```
from math import pi
from math import sin, cos
from pyquery import PyQuery
from pyquery import PyQuery as pq
from numpy import array
from random import randint
```
##### from ... import *语句
```
from math import *
from json import *
```


##### 包的概念与使用 package
包的介绍，包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况。

假设你想设计一套统一处理声音文件和数据的模块（或者称之为一个"包"）。
现存很多种不同的音频文件格式（基本上都是通过后缀名区分的，例如： .wav，:file:.aiff，:file:.au，），所以你需要有一组不断增加的模块，用来在不同的格式之间转换。
并且针对这些音频数据，还有很多不同的操作（比如混音，添加回声，增加均衡器功能，创建人造立体声效果），所以你还需要一组怎么也写不完的模块来处理这些操作。
这里给出了一种可能的包结构（在分层的文件系统中）:

>##### 举例
```
sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```
<b>使用示例</b>
> import sound.effects.echo
from sound.effects import echo
echo.echofilter
from sound.effects.echo import echofilter


<b>练习一</b>
```
1. 尝试使用各种包与模块的引用方式去引用系统中已经安装的模块，并调用其中的函数
```


>### 课后作业
```
1. 模块的练习
使用如下包与模块结构，计算几种常见平面和3D图形的面积、表面积与体积， 并在main函数中依次调用上述定义的面积与体积计算函数，函数名自拟。

geometry/                      顶层包
      __init__.py              初始化 geometry 包
      area/                    计算面积的子包
            __init__.py
            square.py          正方形
            rectangle.py       长方形
            circle.py          圆形
            triangles.py       三角形
      surface_area/            计算表面积的子包
            __init__.py
            cube.py            立方体
            cuboid.py          长方体
            sphere.py          球体
            cylinder.py        圆柱体
      volume/                  计算体积的子包
            __init__.py
            cube.py
            cuboid.py
            sphere.py
            cylinder.py
main.py                        主程序脚本    
```

>### 源码阅读任务
* 任务要求(六选三)
  + 文字阅读报告
  + 上台报告
* 阅读项目列表 [参考：教你阅读Python开源项目代码](https://blog.csdn.net/xiaoxianerqq/article/details/79296708)
  + [stanfordcorenlp](https://github.com/Lynten/stanford-corenlp)
  + [SimpleLM](https://github.com/AdolfVonKleist/SimpleLM)
  + [abcNLP](https://github.com/wuliang/abcNLP)
  + [zhihu_spider](https://github.com/LiuRoy/zhihu_spider)
  + [jieba](https://github.com/fxsjy/jieba)
  + [snownlp](https://github.com/isnowfy/snownlp)
>### 小组项目一
* 小组项目要求说明
  + 项目分工说明
  + 项目说明 README.md或者Word说明文档
  + 源码与演示
  + 编码规范
* 小组项目题目
  + 题一：读取[压缩包 books.zip](projects/books.zip)中的文本文件，将每个文件的中文和英语分别抽取出来，并分别统计每个文件中不同中文词汇与不同英文单词出现的次数，将统计结果保存到csv文件中，每个txt文件对应一个csv文件结果。
  【提示】推荐使用snownlp，字符串，字典，文件读写相关库。
<br/>  
  + 题二： 抓取[房天下](https://newhouse.fang.com/house/s/)网页中北京各区新房楼盘的价格，并将每个区的各楼盘的信息保存下来到csv文件中，每个区一个csv文件。
  【提示】推荐使用requests, requests-html，字典，文件读写相关库。

<b><i>Next Week</i></b> -- I/O, 异常处理, 复习，练习课