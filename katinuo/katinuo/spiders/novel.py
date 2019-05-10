# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from katinuo.items import KatinuoItem


class NovelSpider(CrawlSpider):
    name = 'novel'
    allowed_domains = ['ck101.com']
    start_urls = ['https://ck101.com/forum.php?mod=forumdisplay&fid=3419&page=1']
    # start_urls = ['https://ck101.com/forum.php?mod=viewthread&tid=292604&extra=page%3D176']

    rules = (
        # 小说总列表页获取
        Rule(LinkExtractor(allow=r'&fid=3419&page=\d'), follow=False),
        # 单本小说页获取
        Rule(LinkExtractor(restrict_xpaths='//table/tbody[contains(@id,"normalthread")]//div[@class="titleBox"]/div/a'),callback='parse_item',follow=False),
        # 单本小说章节页获取
        # Rule(LinkExtractor(restrict_xpaths='//div[@class="pg"]/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = KatinuoItem()
        for url in urls:
        item['title'] =  response.xpath('//table/tbody[contains(@id,"normalthread")]//h2/text()')
        # 小说名字
        title =  response.xpath('//table/tbody[contains(@id,"normalthread")]//h2/text()').get()
        # 每部小说内部的下一页
        next_page = response.xpath('//div[@class="pg"]/a[@class="nxt"]')
