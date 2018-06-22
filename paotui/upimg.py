#coding:utf-8
'''
author:微凉

修改头像，上传图片
解决思路：使用requests模块中的post方法，将参数进行拆分，拆分为普通参数data:values和图片参数files:files，
进行post的请求时不使用其他接口的urlib.request模块，使用requests中的post请求方法
具体使用步骤为requests.post（url=接口路径,data=其他参数,files=图片的路径）
files参数示意：
files = {
        'avatar':('a.jpg',open('C:\\Users\\Administrator\\Desktop\\u=224580600,1576965104&fm=27&gp=0.jpg','rb'),'image/jpeg')
             }
'''
import urllib.request
import urllib.parse
import jiami
import time
import json
import requests
def login():
    date = str(int(time.time()))
    username = "15930762890"
    password = "a123456"
    type = "2"
    data = date+","+username+","+password+","+type+","
    data1 = jiami.DesEncrypt(data)
    #print(data1)
    url = "http://192.168.1.181:8093/interface2/member/member.post.php"
    headers = {
        'User-Agent': 'okhttp/2.5.0'
    }
    values = {
        'action':'login',
        'paramData': data1
    }
    data = urllib.parse.urlencode(values).encode('utf-8')
    request = urllib.request.Request(url, data, headers)
    re1 = urllib.request.urlopen(request).read()
    re2 = jiami.DesDecrypt(re1)
    re3 = json.loads(re2)
    can1 = re3['userid']
    can2 = re3['auth']
    return date,can1,can2
def uptou():
    shuju = login()[0]+','+login()[1]+','+login()[2]
    shuju1 = jiami.DesEncrypt(shuju)
    url = 'http://192.168.1.181:8093/interface2/member/avatar.php'
    values = {
        'action':'avatar',
        'paramData':shuju1,
    }
    files = {
        'avatar':('a.jpg',open('C:\\Users\\Administrator\\Desktop\\u=4054100184,7315927&fm=27&gp=0.jpg','rb'),'image/jpeg')
             }
    r = requests.post(url=url,data=values,files=files)
    print(shuju1)
    return r.text
print(json.loads(jiami.DesDecrypt(uptou())))