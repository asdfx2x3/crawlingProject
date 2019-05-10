import requests
from lxml import etree
@staticmethod

num = 1
urls = []
for i in range(5):
    urls.append('http://www.xiladaili.com/gaoni/{}/'.format(num))
    num+=1

for url in urls:
    tree = getHtmlTree(url)
    proxies = tree.xpath('//table[@class="fl-table"]//tr/td[1]/text()')
    for proxy in proxies:
        yield proxy

