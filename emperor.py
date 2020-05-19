# -*- coding:utf-8 -*-
"""
@author:SimonHu
@file:emperor.py
@time:2020/5/18 12:20
formatting shift+f
run alt+x
debug alt+d
"""
import re
import urllib

import requests
from bs4 import BeautifulSoup
import collections
import os
from config import proxies, headers

# scrawl from comprehensive page to generate the url_lists (each link of dynasty)
url_lists = []

# comprehensive page link of Chinese dynasties and emperors
url = 'https://zh.wikipedia.org/zh-hans/%E4%B8%AD%E5%9C%8B%E5%90%9B%E4%B8%BB%E4%B8%96%E7%B3%BB%E5%9C%96%E5%88%97%E8%A1%A8'

dic_category = collections.OrderedDict()


# You can comment up any line if you want
# For example, there exist two method to record the full link collection of each dynasty:
# 1. append to url_lists (If you start this project via Main.py, you shouldn't comment the line #58
# 2. local storage, you can check the weblist.txt on your disk to see the detailed link of each dynasty (line #59)

def get_links():
    with open('weblist.txt', 'w+', newline='', encoding="utf-8") as f:
        result = requests.get(
            url,
            proxies=proxies,
            headers=headers)
        soup = BeautifulSoup(result.content.decode('utf-8'), 'lxml')
        lists = soup.find_all('a', text=re.compile('^(?!/Template:)(.)*世系图$'))

        # fix the the problem of url misleading
        for item in lists[:100]:  # 100 is the # of links in url, maybe one day you will change it

            """
            NOTICE:
            change path to 'zh-hk' can solve the display problem of uncommon chinese
            also you can remove the '.replace[...]' if you feel familiar with traditional Chinese
            """
            fix = str('https://zh.wikipedia.org' + item.get('href')).replace('/wiki', '/zh-hk')
            url_lists.append(fix)
            f.write(fix + '\n')

        # cooperate the function of separate markdown file
        category = soup.select('h3 .mw-headline')
        category_fix = []

        # split the five Dynasties and Ten Kingdoms period into two categories
        for item in category:
            if item.get_text() == '五代十国':
                category_fix.append('五代')
                category_fix.append('十国')
            else:
                category_fix.append(item.get_text())

        # create the dict that includes the k (category name) and v (# of link in this category)
        for item in range(1, len(category_fix) + 1):
            select_sentence = '.mw-parser-output > ul:nth-of-type({}) > li a'.format(item)
            num = len(soup.select(select_sentence))
            dic_category[category_fix[item - 1]] = num
