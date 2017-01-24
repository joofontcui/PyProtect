#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------- 
# @Time    : 2017/1/23 17:28
# @Author  : Cui jun
# @Site    : 
# @File    : douban_house_spider.py
# @Software: PyCharm
#---------------------------------------
import re
import requests
from bs4 import BeautifulSoup

#新建个excel文件&完善头部摘要
# file = xlwt.Workbook()
# table = file.add_sheet('douban house spider',cell_overwrite_ok=True)

#excel排版太乱，阅读起来蓝瘦，换成word试试,然而word模块下载不下来，改用txt
f = open(r'demo.txt', "w")

j = 0
url = "https://www.douban.com/group/zhufang/discussion?start=2" #+ j

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cookie':'bid=Q1PBAIS6jjs; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1485162019%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DSGIVTByAAyTO9_kxh3FnKpOgkIIelc-f6geDSdIsd8aZlmpRYG27XK8IrKBKoEb-%26wd%3D%26eqid%3Dc19282790001a5eb000000045885c61e%22%5D; ap=1; __utmt=1; _pk_id.100001.8cb4=e600a168b0ab079a.1485061031.3.1485163703.1485142191.; _pk_ses.100001.8cb4=*; __utma=30149280.722708358.1485061032.1485142191.1485162020.3; __utmb=30149280.334.2.1485163703651; __utmc=30149280; __utmz=30149280.1485162020.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    'Host': 'www.douban.com',
    'Referer':'https://www.douban.com/group/zhufang/discussion?start=50',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}
houseData = requests.get(url,headers=headers,verify=False).content.decode('utf8')
inHtml = re.findall(r'<a href="(.+?)" title=',houseData,re.I)

h = 1
# print inHtml #数据之一：豆瓣原链接
for i in inHtml:
    indata = requests.get(i,headers=headers,verify=False).content
    print 'i = '+i
    soup = BeautifulSoup(indata)
    inTitle = soup.head.title.string
    print inTitle   #数据之二：房屋标题
    f.write('------------------------------------------------------------'+inTitle.encode('utf8')+'------------------------------------------------------------\n')  # 房屋标题
    f.write(i+'\n')  # 豆瓣原链接
    # onText = soup.select('div[class=topic-content] p')
    onText = soup.select('.topic-content > p')
    try:
        for oonText in onText:
            H=2
            strNeed = ''
            for inText in oonText.strings:
                H+=1
                strNeed=strNeed+inText
            print strNeed  # 豆瓣原链接  # 详细信息
            f.write(strNeed.encode('utf8')+'\n')
        h+=1
        print '------------------'
        f.write('\n\n')
    except:
        print '抛出一个异常'

f.close()
print 'save success'