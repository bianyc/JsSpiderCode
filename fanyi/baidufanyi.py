# -*- coding: utf-8 -*-
import execjs
import requests

basic_url = 'https://fanyi.baidu.com/v2transapi?from={}&to={}'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '134',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BAIDUID=60E08CB1407AC930169297521009331D:FG=1; BAIDUID_BFESS=60E08CB1407AC930169297521009331D:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1612232318,1613616189,1613718324,1614563880; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1614583253; __yjs_duid=1_ddc6aab63de084f5fad5d0d97d9c92231614583252605; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjsv5_shitong=1.0_7_ab7904648bf37c3f1e112502d6a1b157b187_300_1614583252843_220.249.6.194_11e3801c; ab_sr=1.0.0_NWY1ZTBjMWY1ZjdkZWVhMDk2MjBkZDI5YTU2ZDdkYTkwMzZmMGE4MWZlMzExZmUxMDA5MTg5ZjhkMzI4YzkwOTQzZGM0NDU0Y2IxNTkzZjdjMzk3MDg1MzA2MGQ5ZWRm',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

data = {
    'from': '',
    'to': '',
    'query': '',
    'transtype': 'translang',
    'simple_means_flag': '3',
    'sign': '',
    'token': '9a58ef9e259524fafad4af6ffd8962c7',
    'domain': 'common'
}


def get_sign(word):
    """执行js，获取sign值"""
    with open('baidu.js', 'r', encoding='utf-8') as f:
        js_str = f.read()

    ctx = execjs.compile(js_str)
    sign = ctx.call('e', word)
    return sign


def translate_word():
    word = input('输入需要翻译的单词：')

    if u'\u4e00' <= word <= u'\u9fa5':
        url = basic_url.format('zh', 'en')
        data['from'] = 'zh'
        data['to'] = 'en'
    else:
        url = basic_url.format('en', 'zh')
        data['from'] = 'en'
        data['to'] = 'zh'
    data['query'] = word
    data['sign'] = get_sign(word)

    response = requests.post(url, data=data, headers=headers).json()
    if not response.get('errmsg'):
        dst = response['trans_result']['data'][0]['dst']
        print('翻译后单词：', dst)
        return
    else:
        print(response)
        return


if __name__ == '__main__':
    translate_word()
