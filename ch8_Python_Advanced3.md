# Week10 -- Python 高级编程（三） 

> ### 课前预习
* 完成与自己电脑安装的chrome版本相对应的chromedriver版本的安装
* 使用selenium库(通过chromedriver)调用chrome并访问某个网页，保证此
* 预习分享的电子书中面向对象编程（类 Class）相关章节内容

> ### 课堂任务
<b><i>Previously On Week8,9 </i></b>
 * <i>浏览器调试、[jQuery教程](https://www.runoob.com/jquery/jquery-tutorial.html)</i>
 * <i>selenium webdriver调用浏览顺 [&para;](https://www.jianshu.com/p/0e7fc1b6b5cc)</i>


#### 爬虫之网络编程（三）
* 网页中加入jquery的代码
```
javascript: var oHead = document.getElementsByTagName('HEAD').item(0); var oScript= document.createElement("script"); oScript.type = "text/javascript"; oScript.src="https://libs.baidu.com/jquery/2.0.0/jquery.min.js"; oHead.appendChild( oScript);alert('jquery%E6%B3%A8%E5%85%A5%E5%AE%8C%E6%88%90');
```
* jquery css选择器示例
* selenium webdriver调用浏览器访问www.blcu.edu.cn, www.bing.com 网站并检索内容
  + 访问blcu主页并抓取北语新闻
  + 访问bing并检索关键词，获取检索结果列表和分页列表
```
from selenium import webdriver
from pyquery import PyQuery as pq


dr = webdriver.Chrome()
dr.get("www.blcu.edu.cn")

s = dr.page_source
doc = pq(s)
doc('.zcontent').text()
dr.get('http://cn.bing.com')
dr.find_element_by_id('sb_form_q').send_keys('Sun')
dr.find_element_by_id('sb_form_go').click()
dr.find_element_by_id('sb_form_go').click()
s=dr.page_source
lst = doc1('#b_results li')
pq(lst[0]).find('h2').text()
pq(lst[0]).find('.b_algo').text()
pq(lst[0]).find('.b_caption').text()
dr.get('http://www.baidu.com')

```

##### 练习
> 使用selenium webdriver调用chrome, 访问www.baidu.com，并用程序控制在检索框输入自己的姓名，抽取搜索结果列表的内容和分页的链接列表。

#### Python 面向对象编程（一）
##### 面向对象编程基础 
* 类的定义 [&para;](https://superxiaoqiang.github.io/blcu_py_nlp/python_notes/08-object-oriented-programming/08.04-writing-classes)
* 类的继承与super函数 [&para;](https://superxiaoqiang.github.io/blcu_py_nlp/python_notes/08-object-oriented-programming/08.08-inheritance.html)
* 多重继承 [&para;](https://superxiaoqiang.github.io/blcu_py_nlp/python_notes/08.13-multiple-inheritance.html)
>super(CurrentClassName, instance)
>
>返回该类实例对应的父类对象。

```
class Leaf(object):
    def __init__(self, color="green"):
        self.color = color
    def fall(self):
        print "Splat!"

class MapleLeaf(Leaf):
    def change_color(self):
        if self.color == "green":
            self.color = "red"
    def fall(self):
        self.change_color()
        super(MapleLeaf, self).fall()
```
这里，我们先改变树叶的颜色，然后再找到这个实例对应的父类，并调用父类的 fall() 方法：

```
mleaf = MapleLeaf()

print mleaf.color
mleaf.fall()
print mleaf.color
```

##### 面向对象编程实例 -- 以爬虫与文本处理为例
* 案例分析：抓取可可英语网站的分栏目文章，并分别进行文本分析：抽取命名实体、表义词汇（动词、名词、形容词等）,并进行统计
* 通过编写一系列类，来处理以上问题比如：Downloader(若干）, Extractor(若干）, Analyzer(若干），Scheduler
* 在后续小节中逐步完善这些类，引入多进程、定时任务、数据存储（MySQL与MongoDB)
