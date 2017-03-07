#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------- 
# @Time    : 2017/2/27 17:21
# @Author  : Cui jun
# @Site    : 
# @File    : edu_class_data_spider.py
# @Software: PyCharm
#---------------------------------------
import json
import re
import requests

sum_all = 0

for j in range(1,1750,1):
    url = "https://ke.qq.com/cgi-bin/tool/get_bottom_agency?page=%d&count=8&bkn=&r=0.2847930943111394" %j

    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8',
        'cookie': '_pathcode=0.7114380376557266; iswebp=1; course_origin=[{"cid":54837,"ext":{"pagelocation":"index,8.1.5"}}]; _cookie_tdw_firstLand=; _cookie_tdw_firstForm=4; _cookie_tdw_userPath=j; _cookie_tdw_userPathCode=0.5759317517789353; _cookie_tdw_refer=weekedu.ke.qq.com; _cookie_tdw_from=; tdw_data={"ver4":"www.baidu.com","ver5":"","ver6":"","path":"a-0.7114380376557266","uin":null}; pgv_info=ssid=s4686790450; ts_last=ke.qq.com/; ts_refer=www.baidu.com/link; pgv_pvid=6089419024; ts_uid=2549275128',
        'referer': 'https://ke.qq.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = requests.get(url, headers=headers, verify=False).content
    dataOrg = json.loads(data)
    dataOrgList = dataOrg['result']['items']



    for i in dataOrgList:
        # print i['agency_domain']
        try:
            orgUrl = "https://"+i['agency_domain']
            orgHeaders = {

            }
            data = requests.get(orgUrl, headers=orgHeaders, verify=False).content
            inHtml1 = re.findall(r'<a href="javascript:;"><h2>课程(.+?)</h2>', data, re.I)
            keyNum = int(inHtml1[0].replace('(','').replace(')',''))
            sum_all += keyNum
            print sum_all
        except:
            print '抛出一个异常'

print "<----"
print j
print sum_all
print "---->"