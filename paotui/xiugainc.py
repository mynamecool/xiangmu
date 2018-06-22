#coding:utf-8
'''
author：微凉
修改昵称需注意事项，对中文进行des加密，des无法直接对中文进行加密，需要先把中文字符转化为字节流之后进行加密
具体转化方法：
a = u'我是谁'
b = a.encode('utf-8')
'''
import urllib.request
import urllib.parse
import jiami
import time
import json
import login
def xiugai():
    url = 'http://192.168.1.181:8093/interface2/member/user.post.php'
    passport = u'我是谁'
    shuju = login.login()[0]+','+login.login()[1]+','+login.login()[2]+','+passport
    shuju = shuju.encode('utf-8')
    shuju1 = jiami.DesEncrypt(shuju)
    shuju2 = {
        'action':'passport',
        'paramData':shuju1
    }
    shuju3 = urllib.parse.urlencode(shuju2).encode('utf-8')
    request = urllib.request.Request(url, shuju3)
    re1 = urllib.request.urlopen(request).read()
    re2 = jiami.DesDecrypt(re1)
    re3 = json.loads(re2)
    print(re3)
xiugai()
