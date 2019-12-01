# Week13 -- Python 高级编程（五）与自然语言处理（一） 

> ### 课前预习
* 自行百科进程与线程的知识
* 安装配置stanfordcorenlp库，并配置使用Stanford CoreNLP。[参考](https://www.jianshu.com/p/002157665bfd)
* 自学练习[NLTK cookbook](http://www.52nlp.cn/tag/nltk-cookbook)中Part I-V
  + [Part I: Getting Started with NLTK](https://textminingonline.com/dive-into-nltk-part-i-getting-started-with-nltk)
  + [Part II: Sentence Tokenize and Word Tokenize](http://textminingonline.com/dive-into-nltk-part-ii-sentence-tokenize-and-word-tokenize)
  + [Part III: Part-Of-Speech Tagging and POS Tagger](http://textminingonline.com/dive-into-nltk-part-iii-part-of-speech-tagging-and-pos-tagger)
  + [Part IV: Stemming and Lemmatization](http://textminingonline.com/dive-into-nltk-part-iv-stemming-and-lemmatization)
  + [Part V: Using Stanford Text Analysis Tools in Python](http://textminingonline.com/dive-into-nltk-part-v-using-stanford-text-analysis-tools-in-python)

> ### 课堂任务
<b><i>Previously On Week10 </i></b>
 * <i>爬虫之网络编程（四）</i>
 * <i>数据持久化</i>


#### 多进程、多线程处理 -- 以爬虫为例子
* 网页中加入jquery的代码
```
javascript: var oHead = document.getElementsByTagName('HEAD').item(0); var oScript= document.createElement("script"); oScript.type = "text/javascript"; oScript.src="https://libs.baidu.com/jquery/2.0.0/jquery.min.js"; oHead.appendChild( oScript);alert('jquery%E6%B3%A8%E5%85%A5%E5%AE%8C%E6%88%90');
```
* [可可英语双语新闻](http://www.kekenet.com/read/news/)下载器与抽取器，工作同步进行
  + 进程与线程的知识
  + 多进程
  + 多线程
  + 共享队列
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
        self.ua_list = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
            ]
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
> 使用

#### 自然语言处理入门（一）

##### 什么是自然语言处理 （Natural Lanuage Processing)
* 问题
* 问题
* 问题
* 问题

> <b>自然语言处理研究的基本问题</b>
* 问题
* 问题
* 问题

<b>分词与语言模型介绍</b>

```



```

> <b>自然语言处理常用工具集</b>
 * nltk
 * snownlp
 * stanfordcorenlp
 * spaCy
 * FudanNLP
 * ltp

<b><i>使用示例</i></b>

```



```



##### 练习2
> 将练习1抽取的文章数据

##### 词法分析、句法分析
* 词法分析
* 句法分析


```



```

> ### 课后作业
将从可可英语中爬取的各分栏下的文章存入mongodb中。

> ### 个人作业
* 要求：
* 说明：