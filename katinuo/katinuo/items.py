# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KatinuoItem(scrapy.Item):
    # 小说标题
    title = scrapy.Field()
    # 章节名
    chapter = scrapy.Field()
    # 小说内容
    content = scrapy.Field()
