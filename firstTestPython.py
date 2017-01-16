# import urllib.request as request
# import urllib.parse as parse
# import string
# print("""
# +++++++++++++++++++++++
#   学校：超神学院
#   专业：德玛班
#   姓名：德玛之力
#   version: python3.2
# +++++++++++++++++=++++
#      """)
# def baidu_tieba(url, begin_page, end_page):
#     for i in range(begin_page, end_page + 1):
#         sName = 'e:/test/'+str(i).zfill(5)+'.html'
#         print('正在下载第'+str(i)+'个页面, 并保存为'+sName)
#         m = request.urlopen(url+str(i)).read()
#         with open(sName,'wb') as file:
#             file.write(m)
#         file.close()
# if __name__ == "__main__":
#     url = "http://tieba.baidu.com/p/"
#     begin_page = 1
#     end_page = 3
#     baidu_tieba(url, begin_page, end_page)



# import urllib.request
# import socket
# import re
# import sys
# import os
#
# targetDir = r"e:\test"
#
#
# def destFile(path):
#     if not os.path.isdir(targetDir):
#         os.mkdir(targetDir)
#     pos = path.rindex('/')
#     t = os.path.join(targetDir, path[pos + 1:])  # 会以/作为分隔
#     return t
#
#
# if __name__ == "__main__":
#     hostname = "http://www.douban.com/"
#     req = urllib.request.Request(hostname)
#     webpage = urllib.request.urlopen(req)
#     contentBytes = webpage.read()
#     match = re.findall(r'(http:[^\s]*?(jpg|png|gif))',
#                        str(contentBytes))  # r'(http:[^\s]*?(jpg|png|gif))'中包含两层圆括号，故有两个分组，
#     # 上面会返回列表，括号中匹配的内容才会出现在列表中
#     for picname, picType in match:
#         print(picname)
#         print(picType)




# 百度贴吧美食图片
# #coding = utf-8
# import urllib.request
# import re
#
# def getHtml(url):
#     page = urllib.request.urlopen(url)
#     html = page.read()
#     return html
#
# def getImg(html):
#     reg = r'src="(.+?\.jpg)" size'
#     imgre = re.compile(reg)
#     html = html.decode('utf-8')
#     imglist = re.findall(imgre,html)
#     x= 0
#     for imgurl in imglist:
#         urllib.request.urlretrieve(imgurl,'photos/%s.jpg' % x)
#         x+=1
#
# html = getHtml("http://tieba.baidu.com/p/4253192113")
#
# getImg(html)


#网站文件写文件
# import urllib.request
# import http.cookiejar
#
#
# # head: dict of header
# def makeMyOpener(head={
#     'Connection': 'Keep-Alive',
#     'Accept': 'text/html, application/xhtml+xml, */*',
#     'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
# }):
#     cj = http.cookiejar.CookieJar()
#     opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#     header = []
#     for key, value in head.items():
#         elem = (key, value)
#         header.append(elem)
#     opener.addheaders = header
#     return opener
#
#
# oper = makeMyOpener()
# uop = oper.open('http://www.joofont.cn/', timeout=1000)
# data = uop.read()
# print(data.decode())
#
# def saveFile(data):
#     save_path = 'E:/test/temp.txt'
#     f_obj = open(save_path, 'wb') # wb 表示打开方式
#     f_obj.write(data)
#     f_obj.close()
#
# saveFile(data)



# -*- coding:utf-8 -*-
# import urllib
# import urllib.request
# import re
#
#
# # 处理页面标签类
# class Tool:
#     # 去除img标签,7位长空格
#     removeImg = re.compile('<img.*?>| {7}|')
#     # 删除超链接标签
#     removeAddr = re.compile('<a.*?>|</a>')
#     # 把换行的标签换为\n
#     replaceLine = re.compile('<tr>|<div>|</div>|</p>')
#     # 将表格制表<td>替换为\t
#     replaceTD = re.compile('<td>')
#     # 把段落开头换为\n加空两格
#     replacePara = re.compile('<p.*?>')
#     # 将换行符或双换行符替换为\n
#     replaceBR = re.compile('<br><br>|<br>')
#     # 将其余标签剔除
#     removeExtraTag = re.compile('<.*?>')
#
#     def replace(self, x):
#         x = re.sub(self.removeImg, "", x)
#         x = re.sub(self.removeAddr, "", x)
#         x = re.sub(self.replaceLine, "\n", x)
#         x = re.sub(self.replaceTD, "\t", x)
#         x = re.sub(self.replacePara, "\n    ", x)
#         x = re.sub(self.replaceBR, "\n", x)
#         x = re.sub(self.removeExtraTag, "", x)
#         # strip()将前后多余内容删除
#         return x.strip()
#
#
# # 百度贴吧爬虫类
# class BDTB:
#     # 初始化，传入基地址，是否只看楼主的参数
#     def __init__(self, baseUrl, seeLZ, floorTag):
#         # base链接地址
#         self.baseURL = baseUrl
#         # 是否只看楼主
#         self.seeLZ = '?see_lz=' + str(seeLZ)
#         # HTML标签剔除工具类对象
#         self.tool = Tool()
#         # 全局file变量，文件写入操作对象
#         self.file = None
#         # 楼层标号，初始为1
#         self.floor = 1
#         # 默认的标题，如果没有成功获取到标题的话则会用这个标题
#         self.defaultTitle = u"百度贴吧"
#         # 是否写入楼分隔符的标记
#         self.floorTag = floorTag
#
#     # 传入页码，获取该页帖子的代码
#     def getPage(self, pageNum):
#         try:
#             # 构建URL
#             url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
#             request = urllib.request.Request(url)
#             response = urllib.request.urlopen(request)
#             # 返回UTF-8格式编码内容
#             return response.read().decode('utf-8')
#
#     def getTitle(self, page):
#         # 得到标题的正则表达式
#         pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
#         result = re.search(pattern, page)
#         if result:
#             # 如果存在，则返回标题
#             return result.group(1).strip()
#         else:
#             return None
#
#     # 获取帖子一共有多少页
#     def getPageNum(self, page):
#         # 获取帖子页数的正则表达式
#         pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
#         result = re.search(pattern, page)
#         if result:
#             return result.group(1).strip()
#         else:
#             return None
#
#     # 获取每一层楼的内容,传入页面内容
#     def getContent(self, page):
#         # 匹配所有楼层的内容
#         pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
#         items = re.findall(pattern, page)
#         contents = []
#         for item in items:
#             # 将文本进行去除标签处理，同时在前后加入换行符
#             content = "\n" + self.tool.replace(item) + "\n"
#             contents.append(content.encode('utf-8'))
#         return contents
#
#     def setFileTitle(self, title):
#         # 如果标题不是为None，即成功获取到标题
#         if title is not None:
#             self.file = open(title + ".txt", "w+")
#         else:
#             self.file = open(self.defaultTitle + ".txt", "w+")
#
#     def writeData(self, contents):
#         # 向文件写入每一楼的信息
#         for item in contents:
#             if self.floorTag == '1':
#                 # 楼之间的分隔符
#                 floorLine = "\n" + str(
#                     self.floor) + u"-----------------------------------------------------------------------------------------\n"
#                 self.file.write(floorLine)
#             self.file.write(item)
#             self.floor += 1
#
#     def start(self):
#         indexPage = self.getPage(1)
#         pageNum = self.getPageNum(indexPage)
#         title = self.getTitle(indexPage)
#         self.setFileTitle(title)
#         if pageNum == None:
#             print
#             "URL已失效，请重试"
#             return
#         try:
#             print
#             "该帖子共有" + str(pageNum) + "页"
#             for i in range(1, int(pageNum) + 1):
#                 print
#                 "正在写入第" + str(i) + "页数据"
#                 page = self.getPage(i)
#                 contents = self.getContent(page)
#                 self.writeData(contents)
#         # 出现写入异常
#         finally:
#             print
#             "写入任务完成"
#
#
# print
# u"请输入帖子代号"
# baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
# seeLZ = raw_input("是否只获取楼主发言，是输入1，否输入0\n")
# floorTag = raw_input("是否写入楼层信息，是输入1，否输入0\n")
# bdtb = BDTB(baseURL, seeLZ, floorTag)
# bdtb.start()



# import urllib.request
#
# url = 'http://www.baidu.com/'
# req = urllib.request.Request(url, headers={
#     'Connection': 'Keep-Alive',
#     'Accept': 'text/html, application/xhtml+xml, */*',
#     'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
# })
# oper = urllib.request.urlopen(req)
# data = oper.read()
# print(data.decode())



#
# import gzip
# import re
# import http.cookiejar
# import urllib.request
# import urllib.parse
#
#
# def ungzip(data):
#     try:  # 尝试解压
#         print('正在解压.....')
#         data = gzip.decompress(data)
#         print('解压完毕!')
#     except:
#         print('未经压缩, 无需解压')
#     return data
#
#
# def getXSRF(data):
#     cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags=0)
#     strlist = cer.findall(data)
#     return strlist[0]
#
#
# def getOpener(head):
#     # deal with the Cookies
#     cj = http.cookiejar.CookieJar()
#     pro = urllib.request.HTTPCookieProcessor(cj)
#     opener = urllib.request.build_opener(pro)
#     header = []
#     for key, value in head.items():
#         elem = (key, value)
#         header.append(elem)
#     opener.addheaders = header
#     return opener
#
#
# header = {
#     'Connection': 'Keep-Alive',
#     'Accept': 'text/html, application/xhtml+xml, */*',
#     'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
#     'Accept-Encoding': 'gzip, deflate',
#     'Host': 'www.zhihu.com',
#     'DNT': '1'
# }
#
# url = 'http://www.zhihu.com/'
# opener = getOpener(header)
# op = opener.open(url)
# data = op.read()
# data = ungzip(data)  # 解压
# _xsrf = getXSRF(data.decode())
#
# url += 'login'
# id = '15197187787'
# password = 'youhebuke59421'
# postDict = {
#     '_xsrf': _xsrf,
#     'email': id,
#     'password': password,
#     'rememberme': 'y'
# }
# postData = urllib.parse.urlencode(postDict).encode()
# op = opener.open(url, postData)
# data = op.read()
# data = ungzip(data)
#
# print(data.decode())






#网站文件写文件
# import urllib.request
# import http.cookiejar
#
#
# # head: dict of header
# def makeMyOpener(head={
#     'Connection': 'Keep-Alive',
#     'Accept': 'text/html, application/xhtml+xml, */*',
#     'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
# }):
#     cj = http.cookiejar.CookieJar()
#     opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#     header = []
#     for key, value in head.items():
#         elem = (key, value)
#         header.append(elem)
#     opener.addheaders = header
#     return opener
#
#
# oper = makeMyOpener()
# uop = oper.open('https://www.zhihu.com/lives/', timeout=1000)
# data = uop.read()
# print(data.decode())
#
# def saveFile(data):
#     save_path = 'E:/test/temp.txt'
#     f_obj = open(save_path, 'wb') # wb 表示打开方式
#     f_obj.write(data)
#     f_obj.close()
#
# saveFile(data)



# coding=utf-8
# import urllib.request
# import random
#
#
# def getContent(url, headers):
#     """
#     此函数用于抓取返回403禁止访问的网页
#     """
#     random_header = random.choice(headers)
#
#     """
#     对于Request中的第二个参数headers，它是字典型参数，所以在传入时
#     也可以直接将个字典传入，字典中就是下面元组的键值对应
#     """
#     req = urllib.request.Request(url)
#     req.add_header("User-Agent", random_header)
#     req.add_header("GET", url)
#     req.add_header("Host", "blog.csdn.net")
#     req.add_header("Referer", "http://www.csdn.net/")
#
#     content = urllib.request.urlopen(req).read()
#     return content
#
#
# url = "http://blog.csdn.net/beliefer/article/details/51251757"
# # 这里面的my_headers中的内容由于是个人主机的信息，所以我就用句号省略了一些，在使用时可以将自己主机的User-Agent放进去
# my_headers = ["Mozilla/5.0 (Windows NT 6.3; Win64; x64) 。。。 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"]
# print(getContent(url, my_headers))



# import urllib.request
#
# url = "https://api.zhihu.com/lives/ongoing?purchasable=0&limit=10&offset=10"
# headers = ('Accept','*/*' Accept:*/*
# Accept-Encoding:gzip, deflate, sdch
# Accept-Language:zh-CN,zh;q=0.8
# Access-Control-Request-Headers:accept, authorization, x-api-version
# Access-Control-Request-Method:GET
# Connection:keep-alive
# Host:api.zhihu.com
# Origin:https://www.zhihu.com
# Referer:https://www.zhihu.com/lives/
# User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36)
#
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
# data = opener.open(url).read()
#
# print(data)


# # 首先获得Iterator对象:
# it = iter([1, 2, 3, 4, 5])
# # 循环:
# while True:
#     try:
#         # 获得下一个值:
#         x = next(it)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         break

#coding = utf-8
# import PIL.Image
#
# im = PIL.Image.open('photos/0.jpg')
# print(im.format, im.size, im.mode)
#
# im.thumbnail((200, 100))
# im.save('thumb.jpg', 'JPEG')


import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)