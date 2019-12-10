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
汉语分词是中文自然语言处理的基础，词性标注、数词、命名实体（人名、地名、机构名、专业术语等）识别、未登录词识别、
<b>汉语分词示例</b>
```
# snownlp
from snownlp import SnowNLP
text = "在尼比鲁星球探查期间，企业号舰长柯克为营救史波克采取了胆大妄为的举动，几乎危及全舰队员的生命，他也为此付出代价。"

# jieba



# stanfordcorenlp


```

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

<b>汉语分词举例</b>
```
from snownlp import SnowNLP
text = "在尼比鲁星球探查期间，企业号舰长柯克为营救史波克采取了胆大妄为的举动，几乎危及全舰队员的生命，他也为此付出代价。"

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

```

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
  + 制作简单的本地化领域的问答系统