#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/22 19:21
# @Author  : Cui jun
# @Site    : 
# @File    : baidu_pobu_image_spider.py
# @Software: PyCharm

import urllib2
import re
import requests

baiduUrl='https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C4%D0%C8%CB&fr=ala&ori_query=%E7%94%B7%E4%BA%BA&ala=0&alatpl=sp&pos=0&hs=2&xthttps=111111'
headers = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding':'gzip, deflate, sdch, br',
    'accept-language':'zh-CN,zh;q=0.8',
    'cookie':'BDqhfp=%25C4%25D0%25C8%25CB%26%26NaN-1undefined%26%260%26%261; BAIDUID=68E1BD01162ADFAF510B00027318DBFE:FG=1; BIDUPSID=68E1BD01162ADFAF510B00027318DBFE; PSTM=1484882658; BDRCVFR[UskT0xdbq16]=mk3SLVN4HKm; PSINO=2; H_PS_PSSID=1462_21125_17001; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=ala; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm',
    'referer':'https://www.baidu.com/link?url=_saU5yp6iVax1gpplU9DYevSDN-uk757ZETZvw2-wmhNzQeZMdPbe_wVXjugiw1yBpdEQoiz5lJSM9ASkIsvLdmalsJ0am0dNCw0OdARszh0YQ0lg0rpYCYtjTP3dpTV1sz4yH9U443lc_IZ7RxuaWZG1lZgaXXI_AzgFMGSOq82uDLNP1lDahjVinI0dE8m4kyxZnkGrZZfmyV56zX6G5hgiXwAtkK8N40kgO_gF1QsJkwsSD6rheaGqebFi7_8&click_t=1485082893271&s_info=1647_696&wd=&eqid=df50f95800013688000000025884910b',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}
buf=requests.get(baiduUrl, headers=headers, verify=False).content

listurl=re.findall(r'src=.+\.jpg',buf)
listurl=re.findall(r'http:.+\.jpg',buf)

print listurl

i=0
for url in listurl:
     f=open(r"images"+'/images'+str(i)+'.jpg','wb')
     headerss = {
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         'Accept-Encoding': 'gzip, deflate, sdch',
         'Accept-Language': 'zh-CN,zh;q=0.8',
         'Connection': 'keep-alive',
         'Upgrade-Insecure-Requests': '1',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
     }
     reqImages = requests.get(url, headers=headerss, verify=False).content
     buf = req=urllib2.urlopen(reqImages).read()
     f.write(buf)
     i+=1