#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------- 
# @Time    : 2017/2/23 14:02
# @Author  : Cui jun
# @Site    : 
# @File    : class_data_spider.py
# @Software: PyCharm
#---------------------------------------
import urllib2

import re
from base64 import encode, decode

import requests
import xlwt

file = xlwt.Workbook()
table = file.add_sheet('class data')
table.write(0,1,('腾讯课堂成量').decode('utf8'))
table.write(0,2,('网易云课堂成量').decode('utf8'))
table.write(0,3,('百度传课课堂成量').decode('utf8'))

#拼装list
OrganizationList = ['高顿网校',
                    'CDA数据分析师',
                    '开课吧',
                    '51RGB在线教育',
                    '大立教育V',
                    'CGJOY在线课堂',
                    '小象学院',
                    '麦子学院V',
                    '优才教育',
                    '51CTO学院',
                    '为课教育机构',
                    '优达学城Udacity',
                    '名动漫CG教育',
                    'SIKASTONE',
                    '医学教育网官方平台',
                    '92爱知趣',
                    '战翼CG文化教育',
                    '三节课',
                    '91缔范学院',
                    '中华会计网校',
                    '建设工程教育网官方平台',
                    '百通世纪V',
                    '中大网校V',
                    '心教育平台视频中心',
                    '何氏教育',
                    '部落窝教育itblw',
                    '优路教育网',
                    'PMCAFF产品社区',
                    '优才学院',
                    '创汇教育',
                    '计蒜客',
                    '魔乐科技',
                    'IT修真院',
                    '搜狐TDC技术学院',
                    '爱尔信会计网校',
                    'Spss教程',
                    '搜狐快站',
                    '初心客厅心理疏导',
                    '活力网',
                    '小牛学堂',
                    '沃cg',
                    '诚筑说',
                    '3DMAX视频教程幽幽老师',
                    '可道教育',
                    '碧泉教育',
                    '知舟教育',
                    '古厄木小助手',
                    '一点空间学校',
                    'Classmeet社群',
                    '运营直升机兑吧',
                    '菜鸟家园',
                    '千锋教育',
                    '迪才恩网络培训学院']

i = 1
for organization in OrganizationList:
    print organization

    # 腾讯课堂抓取
    # organization = "51RGB"
    TencentUrl = "https://ke.qq.com/course/list/"+ organization
    TencentHeaders = {
        'Cookie': 'RK=9YNupwPres; tvfe_boss_uuid=a8110c4149a25ea2; o_cookie=824929588; pgv_pvi=8347678720; ptcz=47074a76e685bc3f73dfe6f9bccfa9f38d83c9ef36e0cc6b9a9b1b91c4863d01; pt2gguin=o0824929588; _pathcode=0.18326280486267454; iswebp=1; tdw_data={"ver4":"www.baidu.com","ver5":"","ver6":"","path":"a-0.18326280486267454","uin":824929588}; pgv_info=ssid=s8992450300; ts_last=ke.qq.com/; ts_refer=www.baidu.com/link; pgv_pvid=3313893376; ts_uid=1376665960',
    }

    houseData1 = requests.get(TencentUrl,headers=TencentHeaders,verify=False).content.decode('utf8')
    inHtml1 = re.findall(r'<span class="bold">(.+?)</span>',houseData1,re.I)

    print inHtml1[1]



    # 网易云课堂抓取
    # NetEasetUrl = "http://study.163.com/p/search/studycourse.json"
    # NetEasetUrl2 = "http://study.163.com/p/search/studycourse.json"
    # NetEaseHeaders = {
    #     # 'Accept': 'application/json',
    #     # 'Accept-Encoding': 'gzip, deflate',
    #     # 'Accept-Language': 'zh-CN,zh;q=0.8',
    #     # 'Content-Length': '96',
    #     # 'Content-Type': 'application/json',
    #     'Cookie': 'NTESSTUDYSI=aa4aba9281714ea7ba98dc4766628382; EDUWEBDEVICE=a52cffef0a584f70ae47d12de2177819; _ntes_nnid=360e2818bb2242f2b73b9a5a9a34064f,1487828039163; _ntes_nuid=360e2818bb2242f2b73b9a5a9a34064f; utm="eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly93d3cuYmFpZHUuY29tL2xpbms/dXJsPTNFRVBLZjJ4U1VpZjJwalRoTEhfUUh2dlBBOUdHVGMtemFBeFZHN1Jqekcmd2Q9JmVxaWQ9YmI0ODA1Y2IwMDAwZDBlYTAwMDAwMDAyNThhZTgyYTM="; __utma=129633230.785076093.1487828035.1487828035.1487831715.2; __utmb=129633230.63.8.1487832397334; __utmc=129633230; __utmz=129633230.1487831715.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    #     'edu-script-token': 'aa4aba9281714ea7ba98dc4766628382',
    #     'Host': 'study.163.com',
    #     'Origin': 'http://study.163.com',
    #     'Pragma': 'no-cache',
    #     'Referer': 'http://study.163.com/courses-search?keyword=51RGB',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    # }
    # # houseData3 = requests.get(NetEasetUrl,headers=NetEaseHeaders,verify=False).content.decode('utf8')
    # # inHtml3 = re.findall(r'<span class="mc-search-course-list_count j-result-count"></span>',houseData3,re.I)
    # inHtml3 = requests.get(NetEasetUrl2, headers=NetEaseHeaders, verify=False).content
    #
    # print inHtml3



    # 百度传课抓取
    BaiduUrl = "http://www.chuanke.com/course/_"+ organization +"_____.html"
    BaiduHeaders = {
        'Cookie': '_ck_uName=1487827772842239888434; BAIDUID=B93086B5D2CC0A221D302E8F58D0A8CA%3AFG%3D1; _uck_page=1487827775500051156; _uck_from=30000; statistics_first_referer=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DnK_Zxj-ZB4rBZMXbCPJdAyjsX1k-qheZ1qDszAGnF1kWxoVq9brjscfdozy4lGWF%26wd%3D%26eqid%3Db364f4f900019c270000000258ae7337; SchoolStorage=%7B%7D; SessionIDKey=2474280171%0924742801893ji24s; ck_refer=baidu; Hm_lvt_2be0d6083ea4207036d33a4d8be519db=1487827769,1487830893; Hm_lpvt_2be0d6083ea4207036d33a4d8be519db=1487830992',
    }

    houseData2 = requests.get(BaiduUrl,headers=BaiduHeaders,verify=False).content.decode('utf8')
    inHtml2 = re.findall(r'<em>(.+?)</em>',houseData2,re.I)

    print inHtml2[1]

    # table.write(i,0,organization.encode('utf8'))
    table.write(i,1,inHtml1[1])
    table.write(i,3,inHtml2[1])

    i=i+1

file.save('demo.xls')