import requests
from lxml import etree
# @staticmethod

# num = 1
# urls = []
# for i in range(5):
#     urls.append('http://www.xiladaili.com/gaoni/{}/'.format(num))
#     num+=1
#
# for url in urls:
    # tree = getHtmlTree(url)
    # proxies = tree.xpath('//table[@class="fl-table"]//tr/td[1]/text()')
    # for proxy in proxies:
    #     print(proxy)
        # yield proxy


if __name__ == '__main__':
    ret = requests.get('http://www.google.com')
    print(ret.content.decode())
