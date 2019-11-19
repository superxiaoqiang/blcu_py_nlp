# Week11 -- Python 高级编程（四） 

> ### 课前预习
* 安装好mysql服务端（[xampp](https://www.apachefriends.org/download.html)安装好后自带）；在其中创建一个数据库，并在其中创建一个数据表；
* 下载[mongodb安装包](https://www.mongodb.com/download-center/community)(可以下载zip包，免安装)，启动mongod服务和客户端；测试使用命令行mongo客户端一些命令
* 安装MySQLdb、pymongo、sqlalchemy

> ### 课堂任务
<b><i>Previously On Week10 </i></b>
 * <i>selenium webdriver调用浏览器 [&para;](https://www.jianshu.com/p/0e7fc1b6b5cc)</i>
 * <i>面向对象编程、继承、多重继承</i>


#### 爬虫之网络编程（四）
* 网页中加入jquery的代码
```
javascript: var oHead = document.getElementsByTagName('HEAD').item(0); var oScript= document.createElement("script"); oScript.type = "text/javascript"; oScript.src="https://libs.baidu.com/jquery/2.0.0/jquery.min.js"; oHead.appendChild( oScript);alert('jquery%E6%B3%A8%E5%85%A5%E5%AE%8C%E6%88%90');
```
* [可可英语双语新闻](http://www.kekenet.com/read/news/)下载器
  + 导航
  + 分类列表
  + 文章页
* 可可英语双语新闻抽取器
  + 导航
  + 分类列表
  + 文章页
```
class ProxyPool():
    def __init__(self):
        # 初始化读取proxy站点配置文件

        # 初始化读取proxy池存储位置（文件、数据库、NoSQL...)

        # 定时扫描proxy可用性、删除失效代理
        pass

    def 

class KKBaseDownloader():
    def __init__(self):
        # 初始化代理池对象
        self.proxyp = ProxyPool()
        # 初始化headers配置列表文件路径
        self.headers_cfg_pth=''
        # 初始化最小、最大暂停间隔
        self.interval_min_max = (5,30)
        pass
    
    def gen_headers(self):
        pass

    def get_a_proxy(self):
        pass

class KKNavDl(KKBaseDownloader):
    def __init__(self):
        pass

class KKBaseExtractor():
    def __init__(self):
        pass

class KKNavExt(KKBaseExtractor):
    def __init__(self):
        pass
    

```

##### 练习1
> 使用requests库、pyquery库下载、抽取  [可可英语双语新闻](http://www.kekenet.com/read/news/) 科技分类下的文章列表第1页和其中的所有文章信息（包括元数据）；
> 将上述抽取的文章数据，以json字符串格式存入文件中。要求存入文件的json字符串是由每篇文章作为一个字典构成的列表转化而来。

#### Python 数据持久化（一）
[pymysql](https://blog.csdn.net/zuiziyoudexiao/article/details/86744910)
[pymongo](https://www.cnblogs.com/pywjh/p/9494329.html)
[sqlalchemy](https://www.cnblogs.com/sss4/p/9771916.html)
##### 操作关系型数据库 -- pymysql为例
* 常见的关系型数据库
* MySQL数据库基本操作之CRUD
* 使用pymsql进行数据库读操作 R
* 使用pymsql进行数据库写操作 CUD

>读数据库的相关操作语句
> * use schema_name;
> * select 语句
>写数据库的相关操作语句 -- 写数据库时需要有commit语句 原子化
> * CREATE 语句
> * UPDATE 语句
> * DELETE 语句

读数据库示例
```
import pymsql


```
写数据库示例
```
import pymsql


```
##### 练习2
> 将练习1抽取的文章数据，以json字符串格式存入文件后。读取文件内容，将每一条记录插入事先创建好的mysql数据库中的数据表里。

##### 操作NoSQL -- 以pymongo为例
* NoSQL数据库简介
* mongo的命令行操作
* 使用pymongo操作mongodb的简单示例 -- 以存储

```
from pymongo import MongoClient

```