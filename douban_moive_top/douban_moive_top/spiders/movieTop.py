# -*- coding: utf-8 -*-
import scrapy
from douban_moive_top.items import DoubanMoiveTopItem

class MovietopSpider(scrapy.Spider):
    name = 'movieTop'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        items = DoubanMoiveTopItem()
        movies = response.xpath('//ol/li')
        print(str(len(movies)) + '个结果')
        for each in movies:
            # 目标是抓取 5 项内容: 标题 图片 详情链接 评分 短评
            items['title'] = each.xpath('div[@class="item"]/div[@class="info"]//a/span[1]/text()').extract_first()
            items['link'] = each.xpath('div[@class="item"]/div[@class="info"]//a/@href').extract_first()
            items['image'] = each.xpath('div[@class="item"]/div[@class="pic"]/a/img/@src').extract_first()
            items['rating_num'] = each.xpath('div[@class="item"]//span[@class="rating_num"]/text()').extract_first()
            items['quote'] = each.xpath('div[@class="item"]//p[@class="quote"]/span/text()').extract_first()
            yield items

        next_page = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()
        # 如果每个页面都有下一页的话就执行 if 代码块.
        if next_page:
            # 使用 urljoin 方法拼接前往下一页的 url
            next_page_url = response.urljoin(next_page)
            # 使用回调函数循环得到第一页以后的多有内容
            yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=True)
