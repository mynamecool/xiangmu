#coding:utf-8
import base64
from pyDes import *
import json
Des_Key = "6V94Ru3T"
#Des_IV = "7C0jQ4M8"  自定IV向量
def DesEncrypt(str):
    k = des(Des_Key,pad=None,padmode=PAD_PKCS5)
    EncryptStr = k.encrypt(str)
    return base64.b64encode(EncryptStr) #转base64编码返回

def DesDecrypt(qw):
    k = des(Des_Key, pad=None, padmode=PAD_PKCS5)
    a = base64.b64decode(qw)
    DecryptStr = k.decrypt(a)
    return DecryptStr
'''
print(DesEncrypt("1529550145,594,19ef7a5f06b5d1534feef661cc327d4b"))
josn1 = DesDecrypt('Fsby3VC+SLTntyrclKTNaHLpRGlhOGk643YgZv8NuFxJ2T8pbGuJCyAOlSAUQk7H/mDO3GdlMvUOmqz4EI8MQqmQdQ4q0PHn')
print(json.loads(josn1))

'''

