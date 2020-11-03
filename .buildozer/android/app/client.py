# -*- coding: utf-8 -*-
# @时间 : 2020/11/3 11:49 下午
# @作者 : 陈祥安
# @文件名 : client.py
# @公众号: Python学习开发
import requests
files = {'media': open('/Users/chennan/pythonproject/kivyproject/data/presplash.jpg', 'rb')}
try:
    requests.post('http://192.168.199.169:9999/', files=files)
except requests.exceptions.ConnectionError:
    print("Connection Error! Make Sure Server is Active.")