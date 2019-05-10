# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from biquge.items import BiqugeItem


class NovelsSpider(scrapy.Spider):
    name = 'novels'
    allowed_domains = ['qu.la']
    start_urls = ['http://qu.la/']

    def parse(self, response):
        pass
