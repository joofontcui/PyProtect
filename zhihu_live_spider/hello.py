# !/usr/bin/python
# -*- coding:utf-8 -*-
import datetime
import requests
import json
import xlwt

file = xlwt.Workbook()
table = file.add_sheet('zhihu live')
table.write(0,0,('课程名称').decode('utf8'))
table.write(0,1,('讲师知乎昵称').decode('utf8'))
table.write(0,2,('课程描述').decode('utf8'))
table.write(0,3,('价钱￥').decode('utf8'))
table.write(0,4,('开始时间').decode('utf8'))
table.write(0,5,('关注人数').decode('utf8'))
table.write(0,6,('讲师联系地址').decode('utf8'))


for j in range(0,190,10):
    url = "https://api.zhihu.com/lives/ongoing?purchasable=0&limit=10&offset=%d" % j
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
        print to_json['data'][i]
        print to_json['data'][i]['subject']

        # 将队列写入excel
        table.write((j + i + 1), 0, to_json['data'][i]['subject'])  #live title
        table.write((j + i + 1), 1, to_json['data'][i]['speaker']['member']['name'])    #class name
        table.write((j + i + 1), 2, to_json['data'][i]['outline'])    # descripition
        table.write((j + i + 1), 3, to_json['data'][i]['fee']['amount']/100 + to_json['data'][i]['fee']['amount']%100)  # class money
        table.write((j + i + 1), 4, str(datetime.datetime.utcfromtimestamp(to_json['data'][i]['starts_at'])))   #starts_at
        table.write((j + i + 1), 5, to_json['data'][i]['liked_num'])   #liked_num
        table.write((j + i + 1), 6, to_json['data'][i]['speaker']['member']['url'])    #teacher index url

file.save('demo.xls')