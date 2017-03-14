# coding:utf-8
# 采集手机价格
import urllib2
import re


url1 = 'https://search.jd.com/search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=2&cid2=653&cid3=655&ev=exprice_2000-3000%40&page='
url2 = '&s='
url3 = '&click=0'
get_price = []
for i in xrange(1,11):
    if i == 1:
        out_url = 'https://search.jd.com/search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=2&cid2=653&cid3=655&ev=exprice_2000-3000%40&click=0'
    else:
        out_url =  url1 + str(i*2-1) + url2 + str(i*60+1) + url3
    html = urllib2.urlopen(out_url).read()
    page_price = re.findall(r'data-price="(.*?)"><em>¥</em>',html)
    get_price.append(page_price)
#print get_price

# 由于京东推荐设置为2K-3K时会显示低于2k价格的手机 下面进行去虫
all_list = re.findall(r'\'(.*?)\'', str(get_price))
# 浮点数形式的字符串
list1 = map(eval, all_list)
for i in list1: 
	if i >= 2000:
		print i,




