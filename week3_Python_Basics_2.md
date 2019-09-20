# Week3 -- Python 基础编程（二）

> ### 课前预习
* 完成week1中课堂任务中的练习一
* 完成week1中课堂任务中的练习二（选做）
* 预习翻阅[参考书电子](README.md#ref-books)中python函数相关的内容

> ### 课堂任务
Previously On Week2 [虫洞](week2_Python_Basics.md#week2)
#### 常用python内置函数
<table valign="top">
<tr><td><a href="python3-func-number-abs.html" target="_blank" rel="noopener noreferrer">abs()</a></td>
<td><a href="/python/python-func-dict.html" target="_blank" rel="noopener noreferrer">dict()</a></td>
<td><a href="/python/python-func-help.html" target="_blank" rel="noopener noreferrer">help()</a></td>
<td><a href="python3-func-number-min.html" target="_blank" rel="noopener noreferrer">min()</a></td>
<td><a href="/python/python-func-setattr.html" target="_blank" rel="noopener noreferrer">setattr()</a></td>
</tr>
<tr><td><a href="/python/python-func-all.html" target="_blank" rel="noopener noreferrer">all()</a></td>
<td><a href="/python/python-func-dir.html" target="_blank" rel="noopener noreferrer">dir()</a></td>
<td><a href="/python3/python3-func-hex.html" target="_blank" rel="noopener noreferrer">hex()</a></td>
<td><a href="/python/python-func-next.html" target="_blank" rel="noopener noreferrer">next()</a></td>
<td><a href="/python/python-func-slice.html" target="_blank" rel="noopener noreferrer">slice()</a></td>
</tr>
<tr><td><a href="/python/python-func-any.html" target="_blank" rel="noopener noreferrer">any()</a></td>
<td><a href="/python3/python3-func-divmod.html" target="_blank" rel="noopener noreferrer">divmod()</a></td>
<td><a href="/python/python-func-id.html" target="_blank" rel="noopener noreferrer">id()</a></td>
<td>object()</td>
<td><a href="/python3/python3-func-sorted.html" target="_blank" rel="noopener noreferrer">sorted()</a></td>
</tr>
<tr><td><a href="/python3/python3-func-ascii.html" target="_blank" rel="noopener noreferrer">ascii()</a></td>
<td><a href="/python3/python3-func-enumerate.html" target="_blank" rel="noopener noreferrer">enumerate()</a></td>
<td><a href="/python/python3-func-input.html" target="_blank" rel="noopener noreferrer">input()</a></td>
<td><a href="/python/python-func-oct.html" target="_blank" rel="noopener noreferrer">oct()</a></td>
<td><a href="/python/python-func-staticmethod.html" target="_blank" rel="noopener noreferrer">staticmethod()</a></td>
</tr>
<tr><td><a href="/python/python-func-bin.html" target="_blank" rel="noopener noreferrer">bin()</a></td>
<td><a href="/python/python-func-eval.html" target="_blank" rel="noopener noreferrer">eval()</a></td>
<td><a href="/python/python-func-int.html" target="_blank" rel="noopener noreferrer">int()</a></td>
<td><a href="/python3/python3-func-open.html" target="_blank" rel="noopener noreferrer">open()</a></td>
<td><a href="/python/python-func-str.html" target="_blank" rel="noopener noreferrer">str()</a></td>
</tr>
<tr><td><a href="/python/python-func-bool.html" target="_blank" rel="noopener noreferrer">bool()</a></td>
<td><a href="/python3/python3-func-exec.html" target="_blank" rel="noopener noreferrer">exec()</a></td>
<td><a href="/python/python-func-isinstance.html" target="_blank" rel="noopener noreferrer">isinstance()</a></td>
<td><a href="/python3/python3-func-ord.html" target="_blank" rel="noopener noreferrer">ord()</a></td>
<td><a href="/python/python-func-sum.html" target="_blank" rel="noopener noreferrer">sum()</a></td>
</tr>
<tr><td><a href="/python/python-func-bytearray.html" target="_blank" rel="noopener noreferrer">bytearray()</a></td>
<td><a href="/python3/python3-func-filter.html" target="_blank" rel="noopener noreferrer">filter()</a></td>
<td><a href="/python/python-func-issubclass.html" target="_blank" rel="noopener noreferrer">issubclass()</a></td>
<td><a href="/python3/python3-func-number-pow.html" target="_blank" rel="noopener noreferrer">pow()</a></td>
<td><a href="/python/python-func-super.html" target="_blank" rel="noopener noreferrer">super()</a></td>
</tr>
<tr><td><a href="/python3/python3-func-bytes.html" target="_blank" rel="noopener noreferrer">bytes()</a></td>
<td><a href="/python/python-func-float.html" target="_blank" rel="noopener noreferrer">float()</a></td>
<td><a href="/python/python-func-iter.html" target="_blank" rel="noopener noreferrer">iter()</a></td>
<td><a href="/python/python-func-print.html" target="_blank" rel="noopener noreferrer">print()</a></td>
<td><a href="/python3/python3-func-tuple.html" target="_blank" rel="noopener noreferrer">tuple()</a></td>
</tr>
<tr><td><a href="/python/python-func-callable.html" target="_blank" rel="noopener noreferrer">callable()</a></td>
<td><a href="/python/att-string-format.html" target="_blank" rel="noopener noreferrer">format()</a></td>
<td><a href="/python3/python3-string-len.html" target="_blank" rel="noopener noreferrer">len()</a></td>
<td><a href="/python/python-func-property.html" target="_blank" rel="noopener noreferrer">property()</a></td>
<td><a href="/python/python-func-type.html" target="_blank" rel="noopener noreferrer">type()</a></td>
</tr>
<tr><td><a href="/python3/python3-func-chr.html" target="_blank" rel="noopener noreferrer">chr()</a></td>
<td><a href="/python/python-func-frozenset.html" target="_blank" rel="noopener noreferrer">frozenset()</a></td>
<td><a href="/python3/python3-att-list-list.html" target="_blank" rel="noopener noreferrer">list()</a></td>
<td><a href="/python3/python3-func-range.html" target="_blank" rel="noopener noreferrer">range()</a></td>
<td><a href="/python/python-func-vars.html" target="_blank" rel="noopener noreferrer">vars()</a></td>
</tr>
<tr><td><a href="/python/python-func-classmethod.html" target="_blank" rel="noopener noreferrer">classmethod()</a></td>
<td><a href="/python/python-func-getattr.html" target="_blank" rel="noopener noreferrer">getattr()</a></td>
<td><a href="/python/python-func-locals.html" target="_blank" rel="noopener noreferrer">locals()</a></td>
<td><a href="/python/python-func-repr.html" target="_blank" rel="noopener noreferrer">repr()</a></td>
<td><a href="/python3/python3-func-zip.html" target="_blank" rel="noopener noreferrer">zip()</a></td>
</tr>
<tr><td><a href="/python/python-func-compile.html" target="_blank" rel="noopener noreferrer">compile()</a></td>
<td><a href="/python/python-func-globals.html" target="_blank" rel="noopener noreferrer">globals()</a></td>
<td><a href="/python/python-func-map.html" target="_blank" rel="noopener noreferrer">map()</a></td>
<td><a href="/python3/python3-func-reversed.html" target="_blank" rel="noopener noreferrer">reversed()</a></td>
<td><a href="/python/python-func-__import__.html" target="_blank" rel="noopener noreferrer">__import__()</a></td>
</tr>
<tr><td><a href="/python/python-func-complex.html" target="_blank" rel="noopener noreferrer">complex()</a></td>
<td><a href="/python/python-func-hasattr.html" target="_blank" rel="noopener noreferrer">hasattr()</a></td>
<td><a href="/python3/python3-func-number-max.html" target="_blank" rel="noopener noreferrer">max()</a></td>
<td><a href="/python3/python3-func-number-round.html" target="_blank" rel="noopener noreferrer">round()</a></td>
<td>&nbsp;</td>
</tr>
<tr><td><a href="/python/python-func-delattr.html" target="_blank" rel="noopener noreferrer">delattr()</a></td>
<td><a href="/python/python-func-hash.html" target="_blank" rel="noopener noreferrer">hash()</a></td>
<td><a href="/python/python-func-memoryview.html" target="_blank" rel="noopener noreferrer">memoryview()</a></td>
<td><a href="/python/python-func-set.html" target="_blank" rel="noopener noreferrer">set()</a></td>
<td>&nbsp;</td>
</tr>
</table>

#### 函数的定义
你可以定义一个由自己想要功能的函数，以下是简单的规则：
* 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
* 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
* 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
*  函数内容以冒号起始，并且缩进。
* return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
>##### 语法
Python 定义函数使用 def 关键字，一般格式如下：

```
def 函数名(参数列表):
    函数体
```

默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。
>##### 举例
* 计算圆柱的体积 volume(r,h)

#### 函数参数与返回值
以下是调用函数时可使用的正式参数类型：

* 必需参数
* 关键字参数
* 默认参数
* 不定长参数：元组式*、字典式**
```
##### 举例
# 关键字参数示例
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )


# 元组可变参数示例
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )


# 字典可变参数示例
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)

```

<b>练习一</b>
```
1. 打印九九乘法表
```

#### 函数的调用与参数传递
##### 可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

* 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
* 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
```
#  传不可变对象实例
def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print( b ) # 结果是 2


# 传可变对象实例
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)
```   

### 匿名函数Lambda
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

* lambda 只是一个表达式，函数体比 def 简单很多。
* lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
* lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
* 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
##### 语法
lambda 函数的语法只包含一个语句，如下：

>lambda [arg1 [,arg2,.....argn]]:expression

示例
```
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))
```

> ### 课后作业
```
    1. 生成并打印2020年的日历，要求以类似如下格式打印：
     2019

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                   1  2  3
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       4  5  6  7  8  9 10
14 15 16 17 18 19 20      11 12 13 14 15 16 17      11 12 13 14 15 16 17
21 22 23 24 25 26 27      18 19 20 21 22 23 24      18 19 20 21 22 23 24
28 29 30 31               25 26 27 28               25 26 27 28 29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7             1  2  3  4  5                      1  2
 8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
29 30                     27 28 29 30 31            24 25 26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                         1
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                         1
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                    30 31
```
