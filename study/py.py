import urllib.request
import json


url = "https://api.zhihu.com/lives/ongoing?purchasable=0&limit=10&offset=20"
header1 = ('Access-Control-Allow-Credentials','true')
header2 = ('Access-Control-Allow-Headers','Authorization,Content-Type,X-API-Version')
header3 = ('Access-Control-Allow-Methods','GET,PATCH,PUT,POST,DELETE,OPTIONS')
header4 = ('Access-Control-Allow-Origin','https://www.zhihu.com')
header5 = ('Connection','keep-alive')
header6 = ('Content-Encoding','gzip')
header7 = ('Content-Type','application/json; charset=utf-8')
header8 = ('Date','Mon, 16 Jan 2017 02:46:19 GMT')
header9 = ('Etag','W/"c89639c6f2ca82bfed4166947cd76a63b3319022"')
header10 = ('Server','ZWS')
header11 = ('Transfer-Encoding','chunked')
header12 = ('Vary','Accept-Encoding')
header13 = ('X-Req-ID','9F17262587C2ED3')
header14 = ('X-Req-LB','Tc=0,Tr=280,F=main,B=api,bq=0,bc=22,S=ng-platform03,sq=0,sc=8,si=10.3.9.30,sp=80,ci=218.11.4.5,cp=46808,ts=--')
header15 = ('X-Req-SSL:proto=TLSv1.2,sni=,cipher=ECDHE-RSA-AES256-GCM-SHA384')


opener = urllib.request.build_opener()
opener.addheaders = [header1]
opener.addheaders = [header2]
opener.addheaders = [header3]
opener.addheaders = [header4]
opener.addheaders = [header5]
opener.addheaders = [header6]
opener.addheaders = [header7]
opener.addheaders = [header8]
data = opener.open(url).read()
# d = dict(data)
# json.dumps(d)

#
# r = requests.post(url, postdata)
#
# resp = urllib.request.urlopen(url)
# content = resp.read()
# if(content):
#     print(content)


print(data)
# def saveFile(data):
#     save_path = 'E:/python_test/temp.html'
#     f_obj = open(save_path, 'wb') # wb 表示打开方式
#     f_obj.write(data)
#     f_obj.close()
#
# saveFile(data)

