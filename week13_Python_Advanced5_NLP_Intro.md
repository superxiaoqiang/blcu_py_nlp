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
  + [多线程](https://www.runoob.com/python/python-multithreading.html)
  + [多进程](https://www.jianshu.com/p/a69dec87e646)
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
> 使用多进程的方法扩展上述程序，来对下载的文章进行文本抽取。

#### 自然语言处理入门（一）

##### 什么是自然语言处理 （Natural Lanuage Processing)
* 自然语言处理是计算机科学与语言学中关注于计算机与人类语言间转换的领域
* 自然语言处理是计算机科学领域与人工智能领域中的一个重要方向
* NLP要研制表示语言能力和语言应用的模型，建立计算框架来实现这样的语言模型，提出相应的方法来不断完善这样的模型，并根据语言模型设计各种实用系统，以及对这些系统的评测技术

> <b>自然语言处理研究的基本问题</b>
* 词法分析
* 句法分析
* 语义分析
* 词向量
* 文本分类
* 机器翻译
* 信息抽取
* 篇章分析
* 问答系统

<b>分词与语言模型介绍</b>
* 分词 [&para;](https://blog.csdn.net/sinat_26917383/article/details/77067515)
* NGram语言模型([参考](projects/NGrams.pdf))
在自然语言处理中的一个基本问题：给定一串字母，下一个最大可能性出现的字母是什么？
如何计算一段文本序列在某种语言下出现的概率？
<b>语言模型就是用于评估文本符合语言使用习惯程度的模型。</b>

全拼输入法的例子：
P(你现在干什么 | nixianzaiganshenme) > P(你西安在干什么|nixianzaiganshenme)

<b>N-gram模型是一种基于统计语言模型（Language Model，LM），语言模型是一个基于概率的判别模型，它的输入、是一句话（单词的顺序序列），输出是这句话的概率，即这些单词的联合概率（jointprobability）。</b>
N-gram本身也指一个由N个单词组成的集合，各单词具有先后顺序，且不要求单词之间互不相同。常用的有 Bi-gram (N=2) 和 Tri-gram (N=3)

```
from nltk.util import ngrams
a = "add domain with authentication for conference focus user".split(' ')
unigrams = ngrams(a,1)
for i in unigrams:
    print(i)
 
bigrams = ngrams(a,2)
for i in bigrams:
    print(i)

trigrams = ngrams(a,3)
for i in trigrams:
    print(i)
```

* <b>语言模型工具包</b>
    + SRILM - The SRI Language Modeling Toolkit
    + CMUCLMTK   CMU Language Modeling Toolkit 
    + IRSTLM -  The IRST Language Modeling Toolkit
    + KenLM Language Model Toolkit
    + mitlm    MIT Language Modeling Toolit
    + RNNLM Toolkit  (Neural network based lanuage modeling )


> <b>自然语言处理常用工具集[&para;](https://github.com/superxiaoqiang/Awesome-Chinese-NLP)</b>
 * nltk
 * snownlp
 * stanfordcorenlp
 * spaCy
 * FudanNLP
 * ltp

<b><i>使用示例</i></b>

```
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import nltk
# NLTK 分词
word_tokenize("this's a test")
# NLTK 分句
text = "this's a sent tokenize test. this is sent two. is this sent three? sent 4 is cool! Now it's your turn."
sent_tokenize_list = sent_tokenize(text)
print(sent_tokenize_list)

text = nltk.word_tokenize("Dive into NLTK: Part-of-speech tagging and POS Tagger")
nltk.pos_tag(text)

# 词干提取
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer

porter_stemmer = PorterStemmer()
lancaster_stemmer = LancasterStemmer()
porter_stemmer.stem('maximum')
lancaster_stemmer.stem('maximum')


wordnet_lemmatizer = WordNetLemmatizer()
wordnet_lemmatizer.lemmatize('dogs')
wordnet_lemmatizer.lemmatize('aardwolves')

wordnet_lemmatizer.lemmatize('is', pos='v')
wordnet_lemmatizer.lemmatize('are', pos='v')
```

##### 词法分析、句法分析
* <b>词法分析</b>
将句子转换成词序列并标记句子中的词的词性等。不同语言词法分析任务有所不同。
  + 英语
    - 用空格隔开，不需要分词
    - 用词的形态变化表示语法关系 
    - 英文词法分析（曲折变化）
      i. 词的识别、词形还原
      ii. 未登录词处理
      iii.词性标注

  + 汉语
    - 词与词紧密相边，没有明显分界标志
    - 词形变化少，靠词序或虚词来表示语法关系
    - 中文词法分析
      i. 分词
      ii.未登录词识别 
      iii.词性标注

```
from snownlp import SnowNLP
text = "在尼比鲁星球探查期间，企业号舰长柯克为营救史波克采取了胆大妄为的举动，几乎危及全舰队员的生命，他也为此付出代价。"
s = SnowNLP(text)
print(s.words)
print([t for t in s.tags])
```
* <b>句法分析</b>
确定句子包含的全部句法信息，并确定句子中各成分之间的关系。

```
from stanfordcorenlp import StanfordCoreNLP
from nltk.tree import ParentedTree as PT
from nltk.treeprettyprinter import TreePrettyPrinter

corenlp = StanfordCoreNLP('http://localhost',port=2002)
text="Once again, Coca-Cola, Nestlé, and PepsiCo are the world's worst plastic pollution contributors, according to a recent global audit."
tstr = corenlp.parse(text)
pt = PT.fromstring(tstr)
tstr_pretty = TreePrettyPrinter(pt).text()
print(tstr_pretty)
```
##### 练习2
> 对于练习1抽取的文章数据，使用用nltk、stanfordcorenlp、spaCy分别进行练习使用其词法分析和句法分析相关功能。（可参考其官方文档）

> ### 课后作业
分别统计[His_dark_meterials_full_en.zip](projects/His_dark_meterials_full_en.zip)和[The_three_body_problem_full.zip](projects/The_three_body_problem_full.zip) 中所有不同类型词汇的分布比例。比如对于前者，统计其中英文单词中名词、形容词、副词等等占所有词汇的百分比；对于后者，统计中文中各类词汇的占比。

> ### 个人作业
* 要求：
  + 自己独立完成，并在代码中标注详细的注释，另外需要撰写readme文件，说明思路和流程
  + 模块化编程
  + 使用面向对象编程
  + 使用多线程编程

* 说明：期末之前提交初稿代码，已经完成的函数模块可执行。
* 题目（N选1）：
  + 文本特征抽取 
  + 文本人物、动物关系分析
  + 文本分类分析（贝叶斯）
  + 文本句型分析（中、英文）
  + 
  + 