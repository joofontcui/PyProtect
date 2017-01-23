#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/22 16:35
# @Author  : Cui jun
# @Site    : 
# @File    : mooc_image_spider.py
# @Software: PyCharm

import urllib2
import re
req=urllib2.urlopen('http://www.imooc.com/course/list')
buf=req.read()

listurl=re.findall(r'src=.+\.jpg',buf)
listurl=re.findall(r'http:.+\.jpg',buf)

print listurl

i=0
for url in listurl:
     f=open(r"images"+'/image'+str(i)+'.jpg','wb')
     req=urllib2.urlopen(url)
     buf=req.read()
     f.write(buf)
     i+=1