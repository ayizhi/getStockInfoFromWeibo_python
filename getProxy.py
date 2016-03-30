# !/usr/bin/python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getProxy():
	arr = []
	f = open('/Users/zhangyizhi/GitHub/getStockInfoFromWeibo/data/proxy.txt'
,'r')
	while True:
		line = f.readline()
		if line:
			proxy = line.strip()
			arr.append(proxy)
		else:
			break
	return arr

	
