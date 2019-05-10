# -*- coding: utf-8 -*-
import scrapy
from maitian.items import MaitianItem
# from maitian.items import MaitianDetailItem


class MaitianSpider(scrapy.Spider):
    name = 'maiTian'
    allowed_domains = ['maitian.cn']
    url = 'http://bj.maitian.cn/esfall/R3/PG{}'
    page = 1
    start_urls = [url.format(page)]

    def parse(self, response):

        # 1. 获取列表页所有房子
        room_list = response.xpath('//div[@class="list_wrap"]/ul/li')

        if not room_list:
            return

        # 2. 遍历取出所有房子信息
        for room in room_list:
            item = MaitianItem()
            item['info'] = room.xpath('./div[@class="list_title"]/h1/a/text()').get()
            item['img'] = room.xpath('./a/img/@src').get()
            # item['price'] = room.xpath('./div//text()').getall()
            detail_url = 'http://bj.maitian.cn' + room.xpath('./div[@class="list_title"]/h1/a/@href').get()

            # yield item

            # 发送详情页的请求
            yield scrapy.Request(
                detail_url,
                callback=self.parse_detail,
                # 当目前 item 不是完整的时候
                # 可以通过 meta 传到下个响应对象
                meta={'ershou': item}
            )

        # 循环发送 start_urls 中的请求, 获取后面页数的内容
        self.page += 1
        url = self.url.format(self.page)

        yield scrapy.Request(url, callback=self.parse)

    def parse_detail(self, response):
        item = response.meta['ershou']
        item['first_pay'] = response.xpath('//section[2]/div[1]/table/tbody/tr[3]/td[1]/text()').get()
        item['size'] = response.xpath('//section/div[1]/table/tbody/tr[5]/td[1]/text()').get()
        item['area'] = response.xpath('//section/div[1]/table/tbody/tr[7]/td/a/text()').getall()
        item['comment'] = response.xpath('//section/div[1]/table/tbody/tr[10]//label[2]/text()').get()

        yield item
