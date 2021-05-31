# -*- coding: utf-8 -*-
import execjs
import requests
import time


def get_m_cookie():
    with open(r'jscode/02_answer.js', 'r', encoding='utf-8') as f:
        js_str = f.read()

    cjs = execjs.compile(js_str)
    m = cjs.call('get_m_cookie')
    print('Cookie:', m)
    return m


def get_result(page, m):
    url = 'http://match.yuanrenxue.com/api/match/2?page={}'.format(page)
    headers = {
        # "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        # "Connection": "keep-alive",
        "Cookie": m,
        "Host": "match.yuanrenxue.com",
        "Referer": "http://match.yuanrenxue.com/match/2",
        "User-Agent": "yuanrenxue.project",
        "X-Requested-With": "XMLHttpRequest"
    }
    res = requests.get(url, headers=headers)
    data = [heat['value'] for heat in res.json()['data']]
    print('page {} data: '.format(page), data)
    print('=' * 100)
    return data


def start():
    heat = []
    for i in range(1, 6):
        m = get_m_cookie()
        heat += get_result(i, m)
        time.sleep(1)

    print('热度值和为：', sum(heat))


if __name__ == '__main__':
    start()
