# -*- coding: utf-8 -*-
import re
import requests


cookie_url = 'http://www.zjmazhang.gov.cn/hdjlpt/published?via-pc'

cookie_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.zjmazhang.gov.cn",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}

post_url = 'http://www.zjmazhang.gov.cn/hdjlpt/letter/pubList'


def get_cookie_token():
    response = requests.get(cookie_url, headers=cookie_headers)
    cookies = response.cookies
    token = re.findall(r"_CSRF = '(.*)';", response.text)[0]
    return cookies, token


def get_list():
    cookies, token = get_cookie_token()
    post_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "32",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "XSRF-TOKEN={}; szxx_session={}".format(cookies['XSRF-TOKEN'], cookies['szxx_session']),
        "Host": "www.zjmazhang.gov.cn",
        "Origin": "http://www.zjmazhang.gov.cn",
        "Referer": "http://www.zjmazhang.gov.cn/hdjlpt/published?via-pc",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "X-CSRF-TOKEN": token
    }

    form_data = {
        'offset': 0,
        'limit': 20,
        'site_id': 759010,
    }

    resp = requests.post(post_url, data=form_data, headers=post_headers)
    print(resp.json())


if __name__ == '__main__':
    get_list()
