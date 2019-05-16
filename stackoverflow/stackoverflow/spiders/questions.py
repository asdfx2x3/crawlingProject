# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from stackoverflow.items import StackoverflowItem


class QuetionsSpider(CrawlSpider):

    name = 'questions'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/questions/tagged/python?sort=votes&page=1&pagesize=15']

    rules = (
        # 获取详情页
        Rule(LinkExtractor(allow=r'/questions/\w+/',
                           restrict_xpaths='//div[@class="summary"]/h3/a'),
             callback='parse_item',
             follow=False),
        # 获取问题列表页链接
        Rule(LinkExtractor(allow=r'/python\?sort',
             restrict_xpaths='//div[contains(@class,"page") and contains(@class,"fl")]'),
             follow=True),
    )

    def parse_item(self, response):

        item = StackoverflowItem()
        item['title'] = response.xpath('//h1[@itemprop="name"]/a/text()').get()
        item['favorite'] = response.xpath('//button/div/text()').get()
        item['views'] = ''.join(response.xpath('//p[@class="label-key"]/b/text()').getall()).strip()
        item['question'] = response.xpath('//div[contains(@class,"postcell")]').getall()
        item['best_ans_text'] = response.xpath('//div[@itemprop="acceptedAnswer"]//div[contains(@class,"answercell")]').getall()
        item['up_vote_count'] = response.xpath('//div[@itemprop="acceptedAnswer"]//div[@itemprop="upvoteCount"]/text()').get()
        item['bounties'] = response.xpath('//div[@itemprop="acceptedAnswer"]//span[contains(@class,"bounty-award")]/text()').get()
        item['question_url'] = 'https://stackoverflow.com' + response.xpath('//h1[@itemprop="name"]/a/@href').get()

        yield item
