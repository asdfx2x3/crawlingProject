# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaitianItem(scrapy.Item):

    info = scrapy.Field()  # 房屋大概信息
    img = scrapy.Field()  # 房屋图片
    first_pay = scrapy.Field()  # 首付
    size = scrapy.Field()  # 建筑面积
    area = scrapy.Field()  # 区域
    comment = scrapy.Field()  # 房评
