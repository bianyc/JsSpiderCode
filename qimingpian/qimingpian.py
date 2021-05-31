# -*- coding: utf-8 -*-
import requests
import execjs
import json

url = 'https://vipapi.qimingpian.com/DataList/productListVip'
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "69",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "vipapi.qimingpian.com",
    "Origin": "https://www.qimingpian.cn",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}

form_data = {
    'page': 1,
    'num': 20
}

response = requests.post(url, data=form_data, headers=headers)
t = response.json()['encrypt_data']
# print(t)
with open(r'qimingpian.js', 'r', encoding='utf-8') as f:
    js_str = f.read()

cjs = execjs.compile(js_str)
data = cjs.call('o', t)

print(json.loads(data))
