# !/usr/bin/python
# -*- coding:utf-8 -*-

'''抓取网址：https://www.zhihu.com/lives/'''


import urllib2
import re
import requests
import json
import xlwt
from bs4 import BeautifulSoup

#新建个excel文件&完善头部摘要
file = xlwt.Workbook()
table = file.add_sheet('zhihu live')
table.write(0,0,('知乎live名').decode('utf8'))
table.write(0,1,('大V知乎昵称').decode('utf8'))
table.write(0,2,('大V关注人数').decode('utf8'))
table.write(0,3,('知乎live关注人数').decode('utf8'))
table.write(0,4,('大V主页').decode('utf8'))


for j in range(0,170,10):
    url = "https://api.zhihu.com/lives/ongoing?purchasable=1&limit=10&offset=%d" % j
    headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'x-api-version': '3.0.43',
                'Referer': 'https://www.zhihu.com/lives/',
                'Origin': 'https://www.zhihu.com',
                'Host': 'api.zhihu.com',
                'Cookie': 'q_c1=e28b6fe2563e44ada5433489beecf04b|1484565618000|1484565618000; d_c0="ACBC9hLUKQuPTnh9V2jf-UhSN-MT69TsS28=|1484565618"; l_cap_id="MDI1OWIzY2I0YmM1NDNhOGI4N2JmYmZiODNiZGQ2OTA=|1484737865|686bbe37b0165f837b0fee6084a2543ff55d0f04"; cap_id="NTVlNGZlMTJhZGI1NGYyMzg3OGY5OWYyMGMwMGQ3Njg=|1484737865|1d33205ca1725f76a32bfbfd6788bb5e1d7e2892"; _zap=6e9d1286-727c-497e-b0d2-27e0532959dc; r_cap_id="YWFlYzhkN2E1YjM4NDFiYTkyNGIxNjBlMDQ2NWI1Njg=|1484737865|32d93713ceea0bc23854813510c2c15a87db57ea"; login="Y2FkNjJiYTljY2ViNGRiNzhmMDQ4ZDk0NDhkMDc5YmY=|1484737876|97ca602cb6f4413c3182dcab554d7aa99fb4ac90"; aliyungf_tc=AQAAAGBffC0kAQ4A8EZ+e0r5Ikcp4sSE; z_c0=Mi4wQUNBQTFrNmJ3Z29BSUVMMkV0UXBDeGNBQUFCaEFsVk5WTnFtV0FEeTFKZERjRDkyVEhURHJ2TkM1ZlFDOWk4a2xB|1484797825|6c4354b9c4559dfb898e808c0962848a2e775ec9; __utma=155987696.1532979897.1484797824.1484797824.1484797824.1; __utmb=155987696.0.10.1484797824; __utmc=155987696; __utmz=155987696.1484797824.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
            }
    data = requests.get(url, headers=headers, verify=False).content
    to_json = json.loads(data)

    #遍历list，拿到10条内容
    for i in range(0,10,1):
        # print to_json['data'][i]
        # print to_json['data'][i]['subject']
        # print to_json['data'][i]['speaker']['member']['id']

        #获取大V的主页信息，取出其关注人数
        urlIndex = "https://www.zhihu.com/people/" + to_json['data'][i]['speaker']['member']['url_token'] + "/answers"
        # print urlIndex
        headers = {
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8',
            'Accept - Encoding': ' gzip, deflate, sdch, br',
            'Accept - Language': ' zh - CN, zh;q = 0.8',
            'Host': ' www.zhihu.com',
            'Upgrade - Insecure - Requests': ' 1',
            'User - Agent': ' Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 55.0.2883.87Safari / 537.36',
            'Cookie': 'd_c0="AEDCGIe0LguPTi7G67NWtCGQImpBxI6nDus=|1484892893"; q_c1=d56df23070b342749c2fb6b512429f2b|1484892893000|1484892893000; r_cap_id="NzExNzI2YjQ1Nzc5NDhkYzg3Y2M5ODFkOWZlMDk0ZjU=|1484910486|21cecf0c0b9c7b194816c0ff709f40b18f3e82a3"; l_cap_id="NjJlNTIwZjM3ZGU2NDU0NzkxZDVmMDJmODlmZjI3MWE=|1484911422|0a479ccfa4ce4aeda2d8242406180b1ad8d6510b"; cap_id="YTRjNTQzYjQyOGRiNDNmOGE0YjdiYzQwYWUxMmRkN2M=|1484911422|b7f8e35604e26ef980e8400dccc3a5c6abc8c985"; _zap=82631030-9ce0-40f8-8541-d4f97fb0180d; login="ZTE3MmNiZmUxNWMwNDYxNDhiOTg2YTI4YzAxODI0NjI=|1484911427|1d3c5675b82ec33918cfb177c5c25bec55ed9e25"; aliyungf_tc=AQAAAExrWjp/zggA70Z+e8qT8AIM71/S; _xsrf=9fbb1fee8235280d47d43d1661580fb5; __utma=155987696.1764165997.1485056278.1485056278.1485056278.1; __utmc=155987696; __utmz=155987696.1485055245.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); z_c0=Mi4wQUNBQTFrNmJ3Z29BUU1JWWg3UXVDeGNBQUFCaEFsVk5RNENwV0FDV2tYNXZ4Uzl5c0sydzZodktNVHVRTnY0aWdB|1485064953|976e95d687258b76680bb7d5370d4a93ee48c4b1',
        }
        data = None
        req = urllib2.Request(urlIndex, data, headers)
        response = urllib2.urlopen(req)
        htmlIndex = response.read()
        focusPeople = re.findall(r'<div class="NumberBoard-name">关注者</div><div class="NumberBoard-value">(.+?)</div>', htmlIndex, re.I)
        # print focusPeople

        #这块代码是用来测试：不带头cookie信息访问会返回空数据
        soup = BeautifulSoup(htmlIndex)
        if soup.select('.NumberBoard-value').__len__() == 0:
            print urlIndex,htmlIndex

        # print urlIndex, soup.select('.NumberBoard-value')  #<div class="NumberBoard-name">关注者</div><div class="NumberBoard-value">

        # 将队列写入excel
        table.write((j + i + 1), 0, to_json['data'][i]['subject'])  #live title
        table.write((j + i + 1), 1, to_json['data'][i]['speaker']['member']['name'])    #V name
        table.write((j + i + 1), 2, focusPeople)  #V focus
        table.write((j + i + 1), 3, to_json['data'][i]['liked_num'])   #live focus
        table.write((j + i + 1), 4, urlIndex)    #V index url

file.save('demo.xls')