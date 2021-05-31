# -*- coding: utf-8 -*-
import execjs
import time
import requests

basic_url = 'http://match.yuanrenxue.com/api/match/1?page={}&m={}'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'match.yuanrenxue.com',
    'Referer': 'http://match.yuanrenxue.com/match/1',
    'User-Agent': 'yuanrenxue.project',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_js_m():
    """js逆向"""
    with open(r'jscode/01_answer.js', 'r', encoding='utf-8') as f:
        m_js = f.read()

    etx = execjs.compile(m_js)
    psd = etx.call('request')
    print(psd)
    return psd


def get_page(page):
    """请求页面"""
    m = get_js_m().replace('丨', '%E4%B8%A8')
    url = basic_url.format(page, m)
    print(url)

    response = requests.get(url, headers=headers).json()
    data = [price['value'] for price in response['data']]
    print('第{}页价格列表：'.format(page), data)
    print('==' * 50)
    return data


def average():
    """计算平均数"""
    average_list = []
    for i in range(1, 6):
        average_list += get_page(i)
        time.sleep(1)

    print('5页总价格：', sum(average_list))
    print('5页平均价格：', sum(average_list) / len(average_list))


if __name__ == '__main__':
    average()
