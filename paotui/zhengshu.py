#coding:utf-8
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
def upzs():
    url = 'http://192.168.1.181:8093/interface/member/user.post.php'
    shuju = login()[0]+','+login()[1]+','+login()[2]+','+u'我是证书'
    shuju1 = shuju.encode('utf-8')
    shuju2 = jiami.DesEncrypt(shuju1)
    values = {
        'action':'rebook',
        'paramData':shuju2
    }
    files = {
        'thumb1':('a.jpg',open('C:\\Users\\Administrator\\Desktop\\u=4054100184,7315927&fm=27&gp=0.jpg','rb'),'image/jpeg'),
        'thumb2':('b.jpg',open('C:\\Users\\Administrator\\Desktop\\u=4054100184,7315927&fm=27&gp=0.jpg','rb'),'image/jpeg')

    }
    r = requests.post(url=url,data=values,files=files).text
    r1 = jiami.DesDecrypt(r)
    r2 = json.loads(r1)
    print(r2)
upzs()