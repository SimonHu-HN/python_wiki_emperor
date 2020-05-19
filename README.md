## 爬虫维基百科中国皇帝系谱图

[![Build with python3.5](https://img.shields.io/badge/build%20with-python%203.5-green.svg)](https://www.python.org/downloads/release/python-350/)
[![Build Status](https://travis-ci.com/SimonHu-HN/wiki_emperor.svg?branch=master)](https://travis-ci.com/SimonHu-HN/wiki_emperor)


---

### 介绍：

---

![2](https://raw.githubusercontent.com/SimonHu-HN/GoPic_Private/master/img/2.gif)

个人爬虫练手系列，主要内容是针对维基上的[中国君主世系图](https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%9B%BD%E5%90%9B%E4%B8%BB%E4%B8%96%E7%B3%BB%E5%9B%BE)进行爬取，按照维基百科的分类方法，将各个系谱图按照分类爬取下来，并且同样也根据它的分类生成相应的markdown文件。

各位如果有热爱历史的，但是对爬虫方面不太熟悉的可以借鉴一下我的这个爬取工程，按照使用说明进行使用，就可以在自己的电脑里生成一整套较为完整的中国皇帝系谱图，方便各位查阅历史人物与了解文化传承。（另外我对生成的md文件中的各个点击链接做了优化，可以直接跳转到维基百科的官方页面，方便使用者了解感兴趣人物的详细资料。

新手操作，练手之用。如有建议，欢迎留言。

### 需求：

---

```
BeautifulSoup 
requests
collections
re
urllib
# pysocks （if you need socks proxy)
lxml 

$ pip install ...
```

### 文件结构

---

```
wiki_emperor/
├── config.py  //配置文件
├── detail.py  //主要功能
├── emperor.py //主要功能
├── Main.py //入口
├── Main_simple.py //方便IDE环境的入口
├── requirements.txt //pip install -r  requirements.txt
└── test.py

```

### 使用：

---

```
$ cd wiki_emperor
$ python Main.py
$ python Main.py -t -s # for elasped time/ silence mode
$ python Main.py -h # for help
```

```
#Notice：由于是在wiki百科上爬取东西，你应该需要用一下自己的代理，在config.py中的proxies选项里将地址换成自己的服务器地址，切记不要直接就开始跑程序了

#file config.py


"""
    use your own proxy server (support socks)
    'http': 'socks5://xxxx:5555',
    'https': 'socks5://xxxx:5555'
    -------
    'http': '127.0.0.1:5556',
    'https': '127.0.0.1:5556'

"""

```

生成后的markdown文件用一些常用的阅读器即可达到很好的阅览效果（[typora](https://www.typora.io/)，或者[marktext](https://github.com/marktext/marktext/releases)）

### 生成内容：

---

生成文件列表：

![image-20200519195624827](https://raw.githubusercontent.com/SimonHu-HN/GoPic_Private/master/img/image-20200519195624827.png)

文件内部样式预览：

![image-20200519195711665](https://raw.githubusercontent.com/SimonHu-HN/GoPic_Private/master/img/image-20200519195711665.png)

### DIY：

---

默认生成的图是很朴素的，如果你想更好的满足自己的眼睛，就去自己设计一下style吧。css by yourself。
