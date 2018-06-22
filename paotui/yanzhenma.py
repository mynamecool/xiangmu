#coding:utf-8
import urllib.request
import urllib.parse
import jiami
import time
import json
def yanzhen():
    date = str(int(time.time()))
    phonenum = "16601167297"
    type = "2"
    data = date+","+phonenum+","+type
    data1 = jiami.DesEncrypt(data)
    print(data1)
    url = "http://192.168.1.181:8093/interface2/member/member.post.php"
    headers = {
        'User-Agent': 'okhttp/2.5.0'
    }
    values = {
        'action':'sms',
        'paramData': data1
    }
    data = urllib.parse.urlencode(values).encode('utf-8')
    request = urllib.request.Request(url, data, headers)
    re1 = urllib.request.urlopen(request).read()
    re2 = jiami.DesDecrypt(re1)
    re3 = json.loads(re2)
    print(re1)
    print(re3)
def help():
    url = "http://192.168.1.181:8093/interface/help.php"
    request = urllib.request.Request(url)
    re1 = urllib.request.urlopen(request).read()
    re2 = json.loads(re1)
    print(re2)

def xieyi():
    values = {
        'action':'agree'
    }
    url = "http://192.168.1.181:8093/interface/about.php"
    data = urllib.parse.urlencode(values).encode('utf-8')
    request = urllib.request.Request(url,data)
    re1 = urllib.request.urlopen(request).read()
    re2 = json.loads(re1)
    print(re2)
xieyi()