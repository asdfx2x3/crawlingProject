# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BanzhuItem(scrapy.Item):
    # 小说名
    title = scrapy.Field()
    # 类型
    category = scrapy.Field()
    # 章节名
    chap_name = scrapy.Field()
    # 章节正文
    content = scrapy.Field()
