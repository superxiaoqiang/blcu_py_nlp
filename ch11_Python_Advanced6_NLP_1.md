# Week14 -- Python 高级编程 - 自然语言处理基础（一） 

> ### 课前预习
* 安装gensim 和 spaCy库，并参考官方文档进行基本练习
* 继续自学练习[NLTK cookbook](http://www.52nlp.cn/tag/nltk-cookbook)中Part I-V
  + [Part I: Getting Started with NLTK](https://textminingonline.com/dive-into-nltk-part-i-getting-started-with-nltk)
  + [Part II: Sentence Tokenize and Word Tokenize](http://textminingonline.com/dive-into-nltk-part-ii-sentence-tokenize-and-word-tokenize)
  + [Part III: Part-Of-Speech Tagging and POS Tagger](http://textminingonline.com/dive-into-nltk-part-iii-part-of-speech-tagging-and-pos-tagger)
  + [Part IV: Stemming and Lemmatization](http://textminingonline.com/dive-into-nltk-part-iv-stemming-and-lemmatization)
  + [Part V: Using Stanford Text Analysis Tools in Python](http://textminingonline.com/dive-into-nltk-part-v-using-stanford-text-analysis-tools-in-python)

> ### 课堂任务
<b><i>Previously On Week13 </i></b>
 * <i>多线程爬虫</i>
 * <i>自然语言处理入门</i>


#### 自然语言处理基础（一）

##### 什么是自然语言处理 （Natural Lanuage Processing)
* 自然语言处理是计算机科学与语言学中关注于计算机与人类语言间转换的领域
* 自然语言处理是计算机科学领域与人工智能领域中的一个重要方向
* NLP要研制表示语言能力和语言应用的模型，建立计算框架来实现这样的语言模型，提出相应的方法来不断完善这样的模型，并根据语言模型设计各种实用系统，以及对这些系统的评测技术

> <b>自然语言处理研究的问题和领域</b>
* 词法分析
* 句法分析
* 语义分析
* 词向量
* 文本分类
* 机器翻译
* 信息抽取
* 篇章分析
* 问答系统

#### <b>汉语分词与词法分析</b>
##### 汉语分词 [&para;](https://blog.csdn.net/sinat_26917383/article/details/77067515)
汉语分词是中文自然语言处理的基础，词性标注、命名实体（人名、地名、机构名、专业术语等）识别、未登录词识别、多词表达消歧、句法分析、语义分析、关键词提取、文本分类、机器翻译等深层自然语言处理任务的结果都依赖于分词的结果好坏。


##### 基本方法
* 基于词表的方法
  + 最大匹配法(MM)
    - 正向最大匹配法(MM)
    - 逆向最大匹配法(RMM)
    - 双向匹配法
  + 全切分+路径选择
* 序列标记方法

##### 最大匹配法
* 正向最大匹配法： 从左向右匹配词典
* 逆向最大匹配法： 从右向左匹配词典
* <b>例子</b>
输入: 企业要真正具有用工的自主权
MM: 企业/要/真正/具有/用工/的/自主/权
RMM: 企业/要/真正/具有/用工/的/自/主权

##### 全切分方法
* 依据词表，给出输入文本的所有可能的切分结果
* <b>例子</b>
输入:  提高人民生活水平
输出:  提/高/人/民/生/活/水/平
提高/人/民/生/活/水/平
提高/人民/生/活/水/平
提高/人民/生活/水/平
提高/人民/生活/水平
……
* 依据一定的原则选择一种结果作为最终切分结果。如：
  + 选择词数最少的切分结果(最短路径)
  + 选择概率最大的切分结果

##### 序列标注方法
* 把切分问题看作给句子中每个字加标记的过程。
* 四个标记：
(1) B 词首 (2) M 词中
(3) E 词尾 (4)单独成词 S
* <b>例如</b>
输入:提高人民的生活水平
提/B 高/E 人/B 民/E 的/S 生/B 活/E 水/B 平/E
* 设计一个给字序列标注标记序列的算法 -- 常见的算法有HMM （隐马尔可夫模型）

##### 自动切分的评价指标
* 准确率(precision)
  准确率（P）＝切分结果中正确分词数/切分结果中所有分词数*100%
* 召回率(recall)
  召回率（R）＝切分结果中正确分词数/标准答案中所有分词数*100%
* F-评价(F-measure  综合准确率和召回率的评价指标 )
  F-指标＝2PR/(P+R)

上述评价指标也是很多自然语言处理和机器学习任务的评价指标


<b>汉语分词示例</b>
```
text = "在尼比鲁星球探查期间，企业号舰长柯克为营救史波克采取了胆大妄为的举动，几乎危及全舰队员的生命，他也为此付出代价。"

# snownlp
from snownlp import SnowNLP
doc = SnowNLP(text)
doc.words

# jieba
import jieba
words = jieba.cut(text)
[w for w in words]

# stanfordcorenlp
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost',port=2002)
nlp.word_tokenize(text)

# 正确切分
# 在 尼比鲁星球 探查 期间 ，企业号 舰长 柯克 为 营救 史波克 采取 了 胆大妄为 的 举动 ， 几乎 危及 全舰 队员 的 生命 ， 他 也 为此 付出 代价 。
```
<b>练习一</b>
> 复习自动切分的评价指标的概念，分别计算一下上述几种工具对于text表示的中文的自动切分结果相对于正确切分结果的准确率、召回率和F值。可手动统计计算（需要有详细文字解释说明），也可以写程序计算。

> <b>自然语言处理常用工具集[&para;](https://github.com/superxiaoqiang/Awesome-Chinese-NLP)</b>
 * nltk
 * snownlp
 * stanfordcorenlp
 * spaCy
 * FudanNLP
 * ltp
##### 词法分析
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

###### 未登录词识别
+ 举例：
  * 中国人名：李素丽 老张 李四 王二麻子
  * 中国地名：定福庄 白沟 三义庙 韩村河 马甸
  * 翻译人名：乔治·布什 叶利钦 包法利夫人 酒井法子
  * 翻译地名：阿尔卑斯山 新奥尔良 约克郡
  * 机构名：方正公司 联想集团 国际卫生组织 外贸部
  * 商标字号：非常可乐 乐凯 波导 杉杉 同仁堂
  * 专业术语：万维网 主机板 模态逻辑 贝叶斯算法
  * 缩略语：三个代表 五讲四美 打假 扫黄打非 计生办
  * 新词语：卡拉OK 波波族 美刀 港刀
+ 未登录词识别困难
  * 未登录词没有明确边界
  * 许多未登录词的构成单元本身都可以独立成词
+ 通常，每一类未登录词都要构造专门的识别算法
  * 在序列标注法中，未登录词无需单独处理
+ 识别依据
  * 内部构成规律（用字规律）
  * 外部环境（上下文）

<b>汉语词法分析举例</b>
```
from snownlp import SnowNLP
from pprint import pprint
text = "2019年即将结束，与之相伴的是健康保健行业中一些有趣的新趋势。这是一个不断发展的领域，随着新技术和信息的广大普及，新出现的趋势受到了人们的关注。2019年，我们看到越来越多的人选择了新疗法，包括大麻二酚产品的增加，以及致力于改善健康的应用程序和技术的持续增长。"
s = SnowNLP(text)
tags = [t for t in s]
distr = {}
for t in tags:
    if not t[1] in distr.keys():
        distr[t[1]]=1
    else:
        distr[t[1]]+=1
pprint(distr)

```
<b>英语词法分析</b>
* 英语的分词tokenize

* 英语的词形变化
  + 名词单复数、所有格、专有名词 (United States, United Kingdom of Great Brita)
  + 代词的主格、宾格、所有格
  + 形容副词词比较级、最高级
  + 动词数、时态、语态、分词（过去分词、现在分词）
  + 其他

<b>词法分析举例</b>
```
import spacy
nlp = spacy.load('en_core_web_sm')
text="2019 is coming to a close, and with it, we've seen some interesting trends that come and go in the health and wellness industry. This is a constantly evolving area where areas of interest come and go with new trends appearing as new technology and information are made accessible to the broader public. In 2019, we saw an interesting shift toward new therapies, including an increase in CBD-based products, as well as a continued rise in the number of apps and technology to improve well-being and health."
doc = nlp(text)
# 分句
list(doc.sents)
# 词性标注
for w in list(doc.sents)[0]:print(w,w.tag_)
all_tags = {w.pos: w.pos_ for w in doc}
# 命名实体检测
[ (w,w.label_)  for w in doc.ents]
# 名词性短语
[np for np in doc.noun_chunks]
```
<b>练习二</b>
>计算上述例子中段落的词性分布（可以参考“汉语词法分析的示例”）


> ### 个人项目解析
* 文本特征
* 人物、动物关系紧密程序分析
* 文本分类
* 句型分析

> ### 小组项目
* 要求：
  + 小组合作完成，并在代码中标注详细的注释，另外需要撰写readme文件，说明思路和流程
  + 模块化编程
  + 使用面向对象编程
  + 使用多线程编程

* 说明：期末之前提交初稿代码，已经完成的函数模块可执行。
* 题目（N选1）：
  + 制作文本特征抽取系统完整版
  + 制作简单的本地化领域的问答系统，参考[ruyi.ai](http://ruyi.ai/official.html)