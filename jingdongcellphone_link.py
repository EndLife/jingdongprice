# coding:utf-8

# 采集京东手机价格

import urllib2
import re
import cookielib

hosturl = 'https://search.jd.com/search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=1&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&ev=exprice_2000-3000%40&page=1&s=1&click=0'

# cookie
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)
h = urllib2.urlopen(hosturl)

headers = {
    'Referer':'http://search.jd.com/search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=1&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&ev=exprice_2000-3000%40&page=1&s=1&click=0',
    'Host':	'search.jd.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
    # Accept	text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    # Accept-Language	zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
    # Accept-Encoding	gzip, deflate, br
    # Cookie	__jda=122270672.1701241918.1486660470.1486660470.1486993661.1; xtest=8734.4408.d9798cdf31c02d86b8b81cc\
    # 119d94836.b7a782741f667201b54880c925faec4b; mx=0_X; ipLoc-djd=1-72-2799-0; __jdb=122270672.1.1701241918|1.1486993\
    # 661; __jdc=122270672; __jdv=122270672|direct|-|none|-|1486993660994; __jdu=1701241918; rkv=V0300; ipLocation=\
    # %u5317%u4EAC
}

url_list = []
for i in xrange(0,12):
    if i == 0:
        post_url = 'http://search.jd.com/search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=1&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&ev=exprice_2000-3000%40&page=1&s=1&click=0'
    else:
        post_url = 'https://search.jd.com/search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=1&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&ev=exprice_2000-3000%40&page=' + str(i*2+1) + '&s=' + str(i*60) + '&click=0'

    req = urllib2.Request(post_url)
    for key in headers:
        req.add_header(key, headers[key])
    html = urllib2.urlopen(req).read()
    find_url = re.findall(r'href="//item.jd.com/(.*?)\.html" onclick', html)
    for item in find_url:
        x = item.find('"')
        if x > 0:
            out_url = item[:x]
        else:
            out_url = item
        url_list.append("http://item.jd.com/" + out_url)

for item in url_list:
    print item



