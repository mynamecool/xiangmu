#coding:utf-8
from tkinter import *
from pyDes import *
import base64
import json
def DesEncrypt(str,Des_Key):
    k = des(Des_Key,pad=None,padmode=PAD_PKCS5)
    EncryptStr = k.encrypt(str)
    return base64.b64encode(EncryptStr) #转base64编码返回

def DesDecrypt(qw,Des_Key):
    k = des(Des_Key, pad=None, padmode=PAD_PKCS5)
    a = base64.b64decode(qw)
    DecryptStr = k.decrypt(a)
    return DecryptStr
top = Tk()
top.geometry('800x600')

t = Text(top)
t.pack()
e = Entry()
e.pack()
e1 = Entry()
e1.pack()
def printhello():
    a = e.get()
    b = e1.get()
    t.delete(1.0)
    t.insert(1.0,DesEncrypt(a,b))
def printhello1():
    a = e.get()
    b = e1.get()
    t.delete(1.0)
    t.insert(1.0,json.loads(DesDecrypt(a,b)))
com = Button(top,text='加密',command = printhello)
com.pack(side = BOTTOM)
com1 = Button(top,text='解密',command = printhello1)
com1.pack(side = BOTTOM)
# 进入消息循环
top.mainloop()