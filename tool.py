import types
import urllib.request
import json

duan = "--------------------------"  # 在控制台断行区别的


# 利用urllib2获取网络数据
def registerUrl():
        url = "http://www.baidu.com"
        data = urllib.request.urlopen(url).read()
        return data



def jsonFile(fileData):
    file = open("e:/test/temp.txt", "w")
    file.write(fileData)
    file.close()


# 解析从网络上获取的JSON数据
def praserJsonFile(jsonData):
    value = json.loads(jsonData)
    rootlist = value.keys()
    print (rootlist)
    print (duan)
    for rootkey in rootlist:
        print (rootkey)
    print (duan)
    subvalue = value[rootkey]
    print (subvalue)
    print (duan)
    for subkey in subvalue:
        print (subkey, subvalue[subkey])


if __name__ == "__main__":
    # xinput = raw_input()
    # x = 130
    # xvalue = cmp(x,xinput)
    # print xvalue
    # print x/100.0

    data = registerUrl()
    # jsonFile(data)

    praserJsonFile(data)