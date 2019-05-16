# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NovelSpider(CrawlSpider):
    name = 'novel'
    allowed_domains = ['23us.so']
    start_urls = ['https://www.23us.so/xiaoshuo/414.html']

    rules = (
        Rule(LinkExtractor(allow=r'xiaoshuo/\d*\.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'files/article/html/\d*?/\d*?.index.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'files/article/html/\d*?/\d*?/\d*?.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'.'), follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
