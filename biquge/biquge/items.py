# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):

    # id
    novel_id = scrapy.Field()
    # 小说名字
    name = scrapy.Field()
    # 卓和名字
    author = scrapy.Field()
    # 小说链接
    url = scrapy.Field()
    # 小说简介
    content = scrapy.Field()
