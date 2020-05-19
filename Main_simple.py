# -*- coding:utf-8 -*-
"""
@author:SimonHu
@file:Main.py
@time:2020/5/18 14:42
formatting shift+f
run alt+x
debug alt+d
"""
import time
from multiprocessing.pool import Pool

import detail
from emperor import url_lists, get_links, dic_category
import sys

if __name__ == '__main__':
     start = time.time()
     get_links()
     detail.generate_md_to_separate(url_lists, dic_category)
     end = time.time()
     print('elapsed time' + str(end - start))
