# !coding=utf-8
#根据电商平台商品url爬取价格趋势
import csv

import requests
import os
import re
import json
import datetime
import time
import pandas as pd
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import win32api, win32con


def raw(text):  # 转化URL字符串

    escape_dict = {
        '/': '%252F',
        '?': '%253F',
        '=': '%253D',
        ':': '%253A',
        '&': '%26',

    }
    new_string = ''
    for char in text:
        try:
            new_string += escape_dict[char]
        except KeyError:
            new_string += char
    return new_string


def mmm(item, name):
    name = name + ".csv"
    item = raw(item)
    url = 'https://apapia.manmanbuy.com/ChromeWidgetServices/WidgetServices.ashx'
    s = requests.session()
    headers = {
        'Host': 'apapia.manmanbuy.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Proxy-Connection': 'close',
        'Cookie': 'ASP.NET_SessionId=uwhkmhd023ce0yx22jag2e0o; jjkcpnew111=cp46144734_1171363291_2017/11/25',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 mmbWebBrowse',
        'Content-Length': '457',
        'Accept-Encoding': 'gzip',
        'Connection': 'close',
    }
    postdata = 'c_devid=2C5039AF-99D0-4800-BC36-DEB3654D202C&username=&qs=true&c_engver=1.2.35&c_devtoken=&c_devmodel=iPhone%20SE&c_contype=wifi&' \
               't=1537348981671&c_win=w_320_h_568&p_url={}&' \
               'c_ostype=ios&jsoncallback=%3F&c_ctrl=w_search_trend0_f_content&methodName=getBiJiaInfo_wxsmall&c_devtype=phone&' \
               'jgzspic=no&c_operator=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&c_appver=2.9.0&bj=false&c_dp=2&c_osver=10.3.3'.format(
        item)
    s.headers.update(headers)
    req = s.get(url=url, data=postdata, verify=False).text

    print(req)
    try:
        js = json.loads(req)
        title = js['single']['title']  ##名称
    except Exception as e:
        print(e)
        # exit(mmm(item))
    ###数据清洗
    pic = js['single']['smallpic']  ##图片

    itemurl = js['single']['url']  ##商品链接
    good_list = {'商品名称': title,'商品图片': pic,"商品链接": itemurl}
    return good_list

if __name__ == '__main__':
    item = '/jdDetail.aspx?originalUrl=https://item.jd.com/100013406802.html&amp;skuid=100013406802&amp;proid=2324753211'  ##京东、淘宝、天猫等电商平台数据都可以获取
    mmm(item,"耳机1")