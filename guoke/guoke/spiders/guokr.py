# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from guoke.items import GuokeItem


class GuokrSpider(CrawlSpider):
    name = 'guokr'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/ask/highlight/?page=1']

    rules = (
        # 抓取列表页
        Rule(LinkExtractor(allow=r'/?page='), follow=True),

        # 抓取详情页
        Rule(LinkExtractor(allow=r'/question'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = GuokeItem()
        item['question'] = response.xpath('//h1[@id="articleTitle"]/text()').get()
        item['answer'] = response.xpath("//div[contains(@class,'answerTxt')]//text()").getall()
        yield item
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item