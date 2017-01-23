#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------- 
# @Time    : 2017/1/22 20:08
# @Author  : Cui jun
# @Site    : 
# @File    : baidu_searchForImage.py
# @Software: PyCharm
#---------------------------------------

'''
    抓取百度图片xx词条瀑布图中，前yy条
'''
import json
import os
import socket
import urllib
import requests

#全局超时：5s
socket.setdefaulttimeout(5.0)

#用户交互
xx = raw_input("输入你要检索的字段,例如->男人装:") #输入你要检索的字段,例如：男人装
zz = urllib.quote(xx)
print zz
yy = input("输入你要下载的图片总数，例如->1000:") #输入你要下载的图片总数，例如：1000
print yy

for j in range(0, yy, 30):
    #解析url，拼装动态接口，获取数据，转成json
    jj = str(j)
    print type(jj)
    baiduUrl = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result" \
               "&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&s=&se=&tab=&width=&height=&face=0&istype=2" \
               "&qc=&nc=1&fr=&rn=30&gsm=96&1485087644325=&pn="+jj+"&queryWord="+zz+"&word="+zz
    print baiduUrl
    headers = {
        'accept':'text/plain, */*; q=0.01',
        'accept-encoding':'gzip, deflate, sdch, br',
        'accept-language':'zh-CN,zh;q=0.8',
        'cookie':'closedowntip=1; BDIMGISLOGIN=0; BDqhfp=%E7%94%B7%E4%BA%BA%26%260-10-1undefined%26%262973%26%266; '
                 'BAIDUID=68E1BD01162ADFAF510B00027318DBFE:FG=1; BIDUPSID=68E1BD01162ADFAF510B00027318DBFE; PSTM=1484882658; '
                 'H_PS_PSSID=; locale=zh; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; '
                 'BDRCVFR[CLK3Lyfkr9D]=mk3SLVN4HKm; indexPageSugList=%5B%22%E7%94%B7%E4%BA%BA%22%5D; cleanHistoryStatus=0; userFrom=null',
        'referer':'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&fm=detail&lm=-1&st=-1&sf=2&fmq=1485082988520_R_D&fm=detail&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&word=%E7%94%B7%E4%BA%BA',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'x-requested-with':'XMLHttpRequest',
    }
    buf=requests.get(baiduUrl, headers=headers, verify=False).content
    to_json = json.loads(buf)
    print to_json

    #打开或新建文件，用来放置抓取的图片
    filepath=os.getcwd()+'\imagesForBaidu'
    if os.path.exists(filepath) is False:
        os.mkdir(filepath)

    #主要逻辑：百度瀑布图接口数据不固定，原图应该在replaceUrl里，如果没有->直接拿百度的缩略图，如果有判断里面有几个值，尽量取第二个（最新的）
    '''示例
        "replaceUrl": [
                {
                    "ObjURL": "http://img2.imgtn.bdimg.com/it/u=2310040820,4200770776&fm=214&gp=0.jpg",
                    "FromURL": "http://tu.pcpop.com/all-655385.htm"
                },
                {
                    "ObjURL": "http://img5.pcpop.com/articleimages/picshow/120x90/20110425/2011042522334710762.jpg",
                    "FromURL": "http://tu.pcpop.com/pic-655385-14.htm"
                }
            ],
    '''
    x = 1
    for i in to_json['data']:
        if len(i) == 0:
            print '空值,抛弃'
        else:
            temp = filepath + '\%s.jpg' % int(x+j)
            print u'正在下载第%s张图片' % int(x+j)
            if 'replaceUrl' not in i:
                print i["thumbURL"]
                urllib.urlretrieve(i["thumbURL"].strip(), temp)
            else:
                try:
                    if len(i["replaceUrl"]) == 2:
                        print i["replaceUrl"][1]['ObjURL']
                        urllib.urlretrieve(i["replaceUrl"][1]['ObjURL'].strip(), temp)
                    elif len(i["replaceUrl"]) == 1:
                        print i["replaceUrl"][0]['ObjURL']
                        urllib.urlretrieve(i["replaceUrl"][0]['ObjURL'].strip(), temp)
                    elif len(i["replaceUrl"]) == 0:
                        urllib.urlretrieve(i["thumbURL"].strip(), temp)
                    else:
                        print '空值,抛弃';
                except:
                    print '抛出一个异常'
            x += 1

print u'图片下载完毕，保存路径为'+filepath