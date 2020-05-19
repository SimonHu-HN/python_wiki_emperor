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

    if len(sys.argv) == 1:
        get_links()
        detail.generate_md_to_separate(url_lists, dic_category)
    elif len(sys.argv) > 3:
        print('incorrect usage (too many arguments)')
        sys.exit()
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-t':
            start = time.time()
            get_links()
            detail.generate_md_to_separate(url_lists, dic_category)
            end = time.time()
            print('elapsed time' + str(end - start))
        elif sys.argv[1] == '-s':
            get_links()
            detail.generate_md_to_separate_q(url_lists, dic_category)
        elif sys.argv[1] == '-h':
            print('***************Help menu***************')
            print('-t: to show elapsed time')
            print('-s: silence method: disable the progress bar')
            print('do not use arg concatenation')
            sys.exit()
        else:
            print('wrong usage, try type -h for help')
            sys.exit()
    elif len(sys.argv) == 3:
        mul_command = ''.join(sys.argv[1:])
        if len(mul_command) == 4:
            if mul_command.find('-t') != -1 and mul_command.find('-s') != -1:
                print('start')
                start = time.time()
                get_links()
                detail.generate_md_to_separate_q(url_lists, dic_category)
                end = time.time()
                print('elapsed time' + str(end - start))
            else:
                print('wrong usage, try type -h for help')
        else:
            print('wrong usage, try type -h for help')

    # pool = Pool(processes=8)
    # # pool.map(get_all_urllinks, category_url.split())
    # #
    # pool.map(detail.generate_md, url_lists)
