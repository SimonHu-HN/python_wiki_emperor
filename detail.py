# -*- coding:utf-8 -*-
"""
@author:SimonHu
@file:detail.py
@time:2020/5/18 13:24
formatting shift+f
run alt+x
debug alt+d
"""
import re
import urllib

import requests
from bs4 import BeautifulSoup
from config import proxies, headers, file_type


def is_chinese(string):
    """
    check whether the string includes the Chinese
    param: string
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return True


def sharp_fix(url):
    """
    the sharp (#) will incur some troubles in url
    param: url

    """
    if url.find('#') >= 0:
        strs = url.split('#')
        if is_chinese(strs[1]):
            fix = urllib.parse.quote(strs[1])
            fix = strs[0] + '%23' + fix
            return fix
        return url
    return url


def markdown_layout(dynasty_name, map_content, f_write):
    """
    you can design your own layout of your output markdown file
    param:
    dynasty_name: the category name
    map_content: the map of emperor on the website
    f_write : file index

    """
    dynasty_name = str(dynasty_name).replace('#', '')
    f_write.write(
        '### ' + dynasty_name + '\n')  # Use H3 title to distinguish each dynasty
    for item in map_content:
        real_item = str(item).replace("/wiki", "https://zh.wikipedia.org/wiki")  # Important
        f_write.write(str(real_item))
    f_write.write('\n')
    f_write.write('---')  # Add dividing line to beautify the layout
    f_write.write('\n')


def get_map(url):
    """
    download the map content on website
    param: url

    """
    url_fix = sharp_fix(url)
    result = requests.get(url_fix, proxies=proxies, headers=headers)
    soup = BeautifulSoup(result.content.decode('utf-8'), 'lxml')
    dynasty_name = urllib.parse.unquote(url[30:])  # Get title
    dynasty_name = re.sub('[#/]', '', dynasty_name)  # remove extra char
    map_content = soup.find_all('div', class_="chart-container")
    if len(map_content) == 0:
        map_content = soup.find_all('table', class_="chart-container")
    return dynasty_name, map_content


def progress_bar(url_num, dynasty_name):
    """
    default output the progress bar and current task name, -s will kill this function
    param: url_num, url

    """
    print('\r' + '▇' * (url_num // 2) + ' ' + str(url_num + 1) + '%' + dynasty_name, end='')
    if url_num == 99:
        print('\r' + 'done success')


# with open('weblist.txt', 'r') as f_read:
#     for line in f_read.readlines():
#         url_lists.append(line.strip('\n'))

"""
# Method I : Output the result to signal file is tooooooooooooooooo source-consumed,
# Might be, you cannot view it on your local markdown editor.

"""
# def generate_md_to_one(url_lists):
#     with open('emperor_map.md', 'w+', encoding="utf-8") as f_write:
#         for url in url_lists:
#             print(url)
#             result = requests.get(url, proxies=proxies, headers=headers)
#             soup = BeautifulSoup(result.content.decode('utf-8'), 'lxml')
#             dynasty_name = soup.select('#firstHeading')[0].get_text()  # Get title
#             # print(dynasty_name)
#             map_content = soup.find_all('table', class_="chart-container")
#             # print(map_content)
#             f_write.write('### ' + dynasty_name + '\n')  # Use H3 title to distinguish each dynasty
#             for item in map_content:
#                 real_item = str(item).replace("/wiki", "https://zh.wikipedia.org/wiki")  # Important
#                 f_write.write(str(real_item))
#             f_write.write('\n')
#             f_write.write('---')  # Add dividing line to beautify the layout
#             f_write.write('\n')


"""
# Method II : distinguish them by the wiki's way

"""


def generate_md_to_separate(url_lists, dic_category):
    url_num = 0
    for name, num in dic_category.items():
        with open(name + '.md', 'w+', encoding="utf-8") as f_write:
            for i in range(num):
                dynasty_name, map_content = get_map(url_lists[url_num])

                markdown_layout(dynasty_name, map_content, f_write)

                progress_bar(url_num, dynasty_name)

                url_num = url_num + 1


# Method II : silence  method
def generate_md_to_separate_q(url_lists, dic_category):
    url_num = 0
    for name, num in dic_category.items():
        with open(name + file_type, 'w+', encoding="utf-8") as f_write:
            for i in range(num):
                dynasty_name, map_content = get_map(url_lists[url_num])

                markdown_layout(dynasty_name, map_content, f_write)

                url_num = url_num + 1
