#coding:utf-8
import urllib.request
import urllib.parse
import jiami
import time
import json
def xinyong():
    date = str(int(time.time()))
    userid = "594"
    auth = "9cf0a8bc332abe2e6cd3eface8e4fe0c"
    page = "1"
    data = date+","+userid+","+auth+","+page
    data1 = jiami.DesEncrypt(data)
    url = "http://192.168.1.181:8093/interface/member/user.post.php"
    headers = {
        'User-Agent': 'okhttp/2.5.0'
    }
    values = {
        'action':'xinyong',
        'paramData': data1
    }
    data = urllib.parse.urlencode(values).encode('utf-8')
    request = urllib.request.Request(url, data, headers)
    re1 = urllib.request.urlopen(request).read()
    re2 = jiami.DesDecrypt(re1)
    re3 = json.loads(re2)
    print(re1)
    print(re3)