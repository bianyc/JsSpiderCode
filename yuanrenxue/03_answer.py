# -*- coding: utf-8 -*-
import requests
import time

logo_url = 'http://match.yuanrenxue.com/logo'
url = 'http://match.yuanrenxue.com/api/match/3?page={}'

# 请求头参数设置
headers = {
    'Host': 'match.yuanrenxue.com',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'User-Agent': 'yuanrenxue.project',
    'Accept': '*/*',
    'Origin': 'http://match.yuanrenxue.com',
    'Referer': 'http://match.yuanrenxue.com/match/3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


def get_page(page):
    session = requests.session()
    session.headers = headers  # session层面设定headers，发送的是有序字典
    r = session.post(logo_url)
    print('Cookies:', r.headers['Set-Cookie'])

    # 请求数据并打印结果
    res = session.get(url.format(page))
    data = [d['value'] for d in res.json()['data']]
    print('page {} datas:'.format(page), data)
    print('=' * 100)
    return data


def start():
    data_list = []
    for i in range(1, 6):
        data_list += get_page(i)
        time.sleep(1)

    print('出现频率最高的申请号:', max(data_list, key=data_list.count))


if __name__ == '__main__':
    start()
