# -*- coding: utf-8 -*-
import requests
import hashlib
import time
import random


url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '256',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=481809845@10.108.160.100; OUTFOX_SEARCH_USER_ID_NCOO=1392394617.7743514;8',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def salt_lts():
    """生成salt、lts"""
    lts = str(int(time.time() * 1000))
    salt = lts + str(random.randint(0, 9))
    return salt, lts


def sign_md5(e, i):
    """生成sign"""
    s_str = "fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@"
    md = hashlib.md5()
    md.update(s_str.encode())
    return md.hexdigest()


def translation_word():
    """翻译"""
    word = input('输入需要翻译的单词：')
    salt, lts = salt_lts()
    sign = sign_md5(word, salt)

    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': lts,
        'bv': '0785986963146aebf8c240a24088d066',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }
    html = requests.post(url, data=data, headers=headers).json()
    if html.get('errorCode'):
        # print('输入单词有误！')
        print(html)
        return
    tgt = html['translateResult'][0][0]['tgt']
    print('翻译后单词：', tgt)


if __name__ == '__main__':
    translation_word()
