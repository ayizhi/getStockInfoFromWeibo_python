# !/usr/bin/python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import urllib
import json
import re
# import simplejson
from lxml.html import etree
import lxml
import sqlite3 as sqlite
import getProxy


def getTodayCommand(cookieJar):
    f = open(
        r'/Users/zhangyizhi/GitHub/getStockInfoFromWeibo/data/weiboData.txt', 'w+')

    def getPage(pageNum, f, opener):
        url = 'http://weibo.cn/search/mblog?hideSearchFrame=&keyword=%E8%82%A1%E7%A5%A8&page=' + \
            str(pageNum) + '&vt=4'

        print url

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1',
                   'Referer': '', 'Content-Type': 'application/x-www-form-urlencoded'}
        req = urllib2.Request(url, '', headers)
        res = opener.open(req)

        info = res.read()
        info = lxml.html.fromstring(info)
        content = info.xpath('//div[@class = "c"][@id]')

       

        for i in range(len(content) - 1):
            lineDiv = content[i].xpath('./div')[0]
            timeDiv = content[i].xpath('./div')[-1]

            line = lineDiv.xpath('./span[@class = "ctt"]')
            line = line[0].xpath('string(.)')
            time = timeDiv.xpath('./span[@class = "ct"]')
            time = time[0].xpath('string(.)')

            f.writelines([line, '========', time])
            f.writelines('+++++++++++++')
            print line
            print time
            print '=========='
            print '=========='
            print '=========='

    proxyArr = getProxy.getProxy()
    cookie_support = urllib2.HTTPCookieProcessor(cookieJar)

    ipNum = 0
    pageNum = 1
    while pageNum < 100:
        ip = proxyArr[ipNum % len(proxyArr)]
        print 'ip:',ip
        print 'pageNum:',pageNum
      
        proxy_handler = urllib2.ProxyHandler({'HTTP': ip})
        opener = urllib2.build_opener(
            proxy_handler, cookie_support, urllib2.HTTPHandler)

        try:
        	getPage(pageNum, f, opener)
        	pageNum = pageNum + 1
        except:
            print '这个代理失效'

        ipNum = ipNum + 1


    f.close()
