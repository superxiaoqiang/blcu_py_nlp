# Week6 -- Python 基础编程（四）

> ### 课前预习
* 完成week2，3, 4中课堂任务中的练习（建议2020日历打印问题不要使用系统内置calendar库，自己使用列表、字典、循环和打印函数的技巧完成。）
* 完成week2，3, 4中课后作业中的练习
* 预习翻阅[参考书电子中IO](https://python.swaroopch.com/io.html)和[异常处理](https://python.swaroopch.com/exceptions.html)相关的章节内容

> ### 课堂任务
<b><i>Previously On Week2~4</i></b> [虫洞](week3_Python_Basics_2.md)

<b><i>Code Review</i></b>
* <b><i>Example1：打印乘法表 [&para;](examples/week6/Week3_practice.py)</i></b>
* <b><i>Example2 打印日历1[&para;](examples/week6/calendar.py)</i></b>
* <b><i>Example3 打印日历2[&para;](examples/week6/2020日历.py)</i></b>
* <b><i>Example4 geometry[&para;](examples/week6/week4_hw)</i></b>

#### IO与异常处理

##### IO
* 标准输入输出
  + input
  + print
* 文件读写[&para;](https://www.runoob.com/python/python-files-io.html)
  + 文本文件
  + 二进制文件


##### json与pickle
* json
* pickle

><b>练习一</b>
> 1.读取[压缩包 books.zip](projects/books.zip)中解压缩后的文本文件，以文件名为键，文件中文本的长度为值，组成一个字典；
> 2. 将上述字典以json字符串的形式存入文本文件中；
> 3. 将上述字典以pickle二进制形式存入文件中；
    

* 命令行调用传参
  + sys.argv
  + argparse[扩展]
  + optparse[扩展]


##### logging
* 日志操作库[扩展]
* 时间、日期的处理[扩展]



##### 异常处理
* try...except

>### 课后作业
> 1. 同样是读取练习一中的压缩包book.zip中解压缩后的文件，这次在命令行下传递参数，参数为需要读取的文件的文件名；
> 2. 根据 命令行下传递的 文件名读取文件；读取文件时使用异常处理的方法来解决不存在文件的异常情况（比如命令行输入了一个文件名，而引文件并不存在）
> 3. 分别将读取的文件中的中文和英文分离开来，另存为两个文件；比如文件a.txt中既包含中文，也包含英文，将所有中文部分抽取出来，保存为a_CN.txt，将所有英文抽取出来 ，保存为a_EN.txt；以次类推。
