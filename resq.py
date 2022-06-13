# encoding:utf-8
# !/usr/bin/python3
# @AUTHOR : XcNgg
# @IDE:PyCharm 2022.1
# @PROJECT:问答平台
# @FILE:resq.py 
# @TIME:2022/6/11 9:34
import requests
res= requests.get('http://127.0.0.1:5000')
print(res.text)