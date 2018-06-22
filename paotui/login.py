#coding:utf-8
import urllib.request
import urllib.parse
import jiami
import time
import json
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
    return date, can1, can2