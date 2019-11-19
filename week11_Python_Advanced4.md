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
import requests
import random
import time
from pyquery import PyQuery as pq

class ProxyPool():
    def __init__(self):
        # 初始化读取proxy站点配置文件

        # 初始化读取proxy池存储位置（文件、数据库、NoSQL...)

        # 定时扫描proxy可用性、删除失效代理
        pass

    def check_a_proxy(self):
        pass

class KKBaseDownloader():
    def __init__(self):
        # 初始化代理池对象
        self.proxyp = ProxyPool()
        # 初始化headers配置列表文件路径
        self.headers_cfg_pth=''
        # 初始化最小、最大暂停间隔
        self.interval_min_max = (5,30)
        pass
    
    def gen_an_ua(self):
        self.ua_list = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0"]

        return random.choice(self.ua_list)

    def get_a_proxy(self):
        proxys = [

        ]
        idx = random.randint(1,len(proxys))
        return proxys[idx]

class KKNavDl(KKBaseDownloader):
    def __init__(self,init_url):
        super(KKNavDl,self).__init__()
        self.url_tgt = init_url

    def fetch_html(self):
        ua = self.gen_an_ua()
        headers = {'User-Agent':ua}
        # _proxy = self.get_a_proxy()
        # r = requests.get(self.url_tgt,proxies=_proxy)
        r = requests.get(self.url_tgt,headers=headers)
        if r.status_code==200:
            if r.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(r.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r.apparent_encoding
            encode_content = r.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            return encode_content
        else:
            return ''

class KKBaseExtractor():
    def __init__(self,html='<html></html>'):
        self.doc = pq(html)

class KKNavExt(KKBaseExtractor):
    def __init__(self,html):
        super(KKNavExt,self).__init__(html)

    def parse(self):
        lis = self.doc('.navtab>ul>li')
        nav_links = []
        for i in range(3,len(lis)):
            pq_li = pq(lis[i])
            nav_links.append((pq_li.text(),pq_li.find('a').attr('href')))
        return nav_links

def main()
    navDl = KKNavDl(init_url='http://www.kekenet.com/read/news/')
    html = navDl.fetch_html()
    navExt = KKNavExt(html)
    nav_links = navExt.parse()
    for lnk in nav_links:
        print(lnk)
    
```

##### 练习1
> 使用requests库、pyquery库下载、抽取  [可可英语双语新闻](http://www.kekenet.com/read/news/) 科技分类下的文章列表第1页和其中的所有文章信息（包括元数据）；
> 将上述抽取的文章数据，以json字符串格式存入文件中。要求存入文件的json字符串是由每篇文章作为一个字典构成的列表转化而来。

#### Python 数据持久化（一）
[pymongo](https://www.cnblogs.com/pywjh/p/9494329.html)
[sqlalchemy](https://www.cnblogs.com/sss4/p/9771916.html)
相关库的安装
pip install pymysql pymongo sqlalchemy
##### 操作关系型数据库 -- pymysql为例
* 常见的关系型数据库 sqlite, MySQL(MariaDB), SqlServer, Oralce
* MySQL数据库基本操作之  CRUD
* 使用pymsql进行数据库读操作 R
* 使用pymsql进行数据库写操作 CUD

> <b>读数据库的相关操作语句</b>
* 首先导入示例数据库脚本 [kekenet.sql](examples/kekenet.sql)
* use schema_name;
* select 语句

<b><i>读数据库示例</i></b>

```
import pymysql
conn = pymysql.connet('localhost','moodle30','moodle30','kekenet',charset='utf-8')
conn = pymysql.connect('localhost','moodle30','moodle30','kekenet')
cur = conn.cur()
sql = 'set names utf8'
cur.execute(sql)

sql = 'select * from article'
cur.execute(sql)

dat = cur.fetchall()
print(dat)
```

> <b>写数据库的相关操作语句</b> -- 写数据库时需要有commit语句 原子化
 * INSERT 语句
 * UPDATE 语句 
 * DELETE 语句

<b><i>写数据库示例</i></b>

```
# 删除语句
sql ='delete from article where id = 3';
cur.execute(sql)
sql = 'select * from article'
cur.execute(sql)
data = cur.fetchall()
print('删除了一条数据:')
print(data)
# 提交，不然无法保存新建或者修改的数据
conn.commit()
# 关闭光标对象
cur.close()
# 关闭数据库连接
conn.close()

# 添加语句
sql = 'insert into article (id, title, editor, source, datetime, txt_en, txt_cn) values (3, "近一半的上班族因为压力太大而濒临崩溃", "Kelly", "chinadaily", "2019-10-12 07:00:00", "Nearly half of all employees are close to \"breaking point\" at work due to increased stress levels. A survey of 2,000 professionals found the average working adult feels stressed for almost a third of their working day.", "近一半的上班族因为压力增大而濒临崩溃。一项针对2000名职场人士的研究发现：工作日期间，每位上班族平均有三分之一的时间感到心力交瘁。")';
cur.execute(sql)
sql = 'select * from article'
cur.execute(sql)
data = cur.fetchall()
print('插入了一条数据:')
print(data)
print("\n")

# 更新语句
sql = 'update article set editor="Lily" where id=3';
cur.execute(sql)
sql = 'select * from article'
cur.execute(sql)
data = cur.fetchall()
print('插入了一条数据:')
print(data)
print("\n")
```



##### 练习2
> 将练习1抽取的文章数据，以json字符串格式存入文件后。读取文件内容，将每一条记录插入事先创建好的mysql数据库中的数据表里。

##### 操作NoSQL -- 以pymongo为例
* NoSQL数据库简介
* mongo的命令行操作 [&para;](https://www.jianshu.com/p/140cd046c748)
* 使用pymongo操作mongodb的简单示例 -- 以存储可可英语文章为例

```
import pymongo
client = pymongo.MongoClient('127.0.0.1',27017)
db=client['kekenet']
col=db['article']

dat=col.find_one()
print(dat)


a = {
    'title':'微软在日本试行4天工作制,工作效率暴增!',
    'txt_eng':'A growing number of smaller companies are adopting a four-day workweek. Now the results of a recent trial at Microsoft (MSFT) suggest it could work even for the biggest businesses.',
    'txt_cn':'越来越多中小公司开始采用四天工作制。如今微软近日的试验结果显示，就算在大企业也能见效。'
}
col.insert_one(a)

_as = [
    {
        'title':'你一开口,面试官就知道你是哪种人',
        'txt_eng':'Job candidates are judged on their social status just a few seconds after they start to speak, according to a new study.',
        'txt_cn':'一项新研究发现，求职者开口说话几秒钟后，面试官就已经对他们的社会地位做出了判断。'
    },
    {
        'title':'近一半的上班族因为压力太大而濒临崩溃',
        'txt_eng':'Nearly half of all employees are close to "breaking point" at work due to increased stress levels. A survey of 2,000 professionals found the average working adult feels stressed for almost a third of their working day.',
        'txt_cn':'近一半的上班族因为压力增大而濒临崩溃。一项针对2000名职场人士的研究发现：工作日期间，每位上班族平均有三分之一的时间感到心力交瘁。'
    }
]
col.insert_many(_as)

dat=col.find()
for d in dat:
    print(d)

col.update_one({'title':'这是填标题'}, {'$set':{'title':'标题'}})
col.find_one()

col.delete_one({'title':'标题'})
dat=col.find()
for d in dat:
    print(d)
```

> ### 课后作业
将从可可英语中爬取的各分栏下的文章存入mongodb中。（要求不只是爬取第一页，需要分析分页链接，并爬取尽可能多的列表页）