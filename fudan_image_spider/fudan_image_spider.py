#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------- 
# @Time    : 2017/3/7 13:03
# @Author  : Cui jun
# @Site    : 
# @File    : fudan_image_spider.py
# @Software: PyCharm
#---------------------------------------
import os
import urllib
import urllib2

for i in range(569,706,1):
    try:
        url = "http://www.fudan.edu.cn/files/slider/1920/%d.jpg" %i
        f = open(r"images" + '/images' + str(i) + '.jpg', 'wb')
        # temp = filepath + '\%s.jpg' % int(i)
        print url
        buf = req = urllib2.urlopen(url).read()
        f.write(buf)
    except:
        print "抛出一个异常"
