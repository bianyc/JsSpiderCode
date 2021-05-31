# -*- coding: utf-8 -*-
import json

headers_str = """:authority: www.amazon.com
:method: GET
:path: /s?k=OUTERA&ref=bl_dp_s_web_19825776011
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
cache-control: max-age=0
cookie: session-id=144-0277387-3568143; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:CN"; ubid-main=130-8792086-7901706; session-token=VAVQ5QL1/NgSW0h4ZQCqwN62zRorGyLyUHzq2lJ0n5IZ3PjT6/5EtlZiEj1nnei8yArxgV0eVLCaVrWgULwLmQIuTtZZao7+fwnph7SULTHGyTLzl/wluZ901zTJ646EBTP+dATbUNOm+mP9wrMtXKZS4gIx59EQRSjp0a2g85kA/Hlqu2c01ZeXlRjLy+um; lc-main=en_US; csm-hit=tb:Q80A8VPNH75973JQEYB2+s-Q80A8VPNH75973JQEYB2|1620615494401&t:1620615494402&adb:adblk_no
downlink: 7.65
ect: 4g
rtt: 250
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"
sec-ch-ua-mobile: ?0
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"""


def change_headers(header_str):
    print(header_str.split("\n")[1: -1])
    h = [line.split(": ", 1) for line in header_str.split("\n")[1: -1]]
    print(h)
    headers = dict(h)
    print(json.dumps(headers, ensure_ascii=False, indent=2))


if __name__ == '__main__':

    change_headers(headers_str)


"""
{
  ":authority": "www.amazon.com",
  ":method": "GET",
  ":path": "/s?k=OUTERA&ref=bl_dp_s_web_19825776011",
  ":scheme": "https",
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "cache-control": "max-age=0",
  "cookie": "session-id=144-0277387-3568143; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn=\"L5Z9:CN\"; ubid-main=130-8792086-7901706; session-token=VAVQ5QL1/NgSW0h4ZQCqwN62zRorGyLyUHzq2lJ0n5IZ3PjT6/5EtlZiEj1nnei8yArxgV0eVLCaVrWgULwLmQIuTtZZao7+fwnph7SULTHGyTLzl/wluZ901zTJ646EBTP+dATbUNOm+mP9wrMtXKZS4gIx59EQRSjp0a2g85kA/Hlqu2c01ZeXlRjLy+um; lc-main=en_US; csm-hit=tb:Q80A8VPNH75973JQEYB2+s-Q80A8VPNH75973JQEYB2|1620615494401&t:1620615494402&adb:adblk_no",
  "downlink": "7.65",
  "ect": "4g",
  "rtt": "250",
  "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Microsoft Edge\";v=\"90\"",
  "sec-ch-ua-mobile": "?0",
  "sec-fetch-dest": "document",
  "sec-fetch-mode": "navigate",
  "sec-fetch-site": "same-origin",
  "sec-fetch-user": "?1",
  "upgrade-insecure-requests": "1",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"
}

"""
