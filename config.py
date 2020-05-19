# -*- coding:utf-8 -*-
"""
@author:SimonHu
@file:config.py
@time:2020/5/19 14:11
formatting shift+f
run alt+x
debug alt+d
"""

# copy from the browser (date May/19 2020)
headers = {
    'authority': 'zh.wikipedia.org',
    'method': 'GET',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip,deflate,br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'cache-control': 'no-cache',
    'cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1994293536.0080583;TBLkisOn=0;WMF-Last-Access=18-May-2020;WMF-Last-Access-Global=18-May-2020;GeoIP=HK:HCW:Central:22.29:114.15:v4;zhwikimwuser-sessionId=a22c66adcc6d47cec44d',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https://zh.wikipedia.org/zh-hans/%E4%B8%AD%E5%9C%8B%E5%90%9B%E4%B8%BB%E4%B8%96%E7%B3%BB%E5%9C%96%E5%88%97%E8%A1%A8',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0(WindowsNT6.3;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/81.0.4044.138Safari/537.36',
}

"""
    use your own proxy server (support socks)
    'http': 'socks5://xxxx:5555',
    'https': 'socks5://xxxx:5555'
    -------
    'http': '127.0.0.1:5556',
    'https': '127.0.0.1:5556'

"""

proxies = {

}

file_type = '.md'
