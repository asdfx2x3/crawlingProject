# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from banzhu.items import BanzhuItem


class NovelSpider(CrawlSpider):
    name = 'novel'
    allowed_domains = ['banzhuer.com']
    start_urls = ['https://www.banzhuer.com/jingpinxiaoshuo/']

    rules = (
        Rule(LinkExtractor(allow=r'/\d_\d+.html', restrict_xpaths='//div[@id="pagelink"]'), follow=True),

        Rule(LinkExtractor(allow=r'/\d+_\d+/\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = BanzhuItem()
        item['title'] = response.xpath('//div[@class="content_read"]/div/div/a[3]/text()').get()
        item['chap_name'] = ''.join(response.xpath('//div[@class="content_read"]/div/div[@class="con_top"]/text()').getall()).split('>')[-1].strip()
        item['content'] = '\n'.join(response.xpath('//*[@id="content"]//text()').getall()).strip()
        return item
