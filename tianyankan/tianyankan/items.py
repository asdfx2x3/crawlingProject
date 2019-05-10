# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianyankanItem(scrapy.Item):

    # 小说名字
    title = scrapy.Field()
    # 小说详情页
    # urls = scrapy.Field()
    # 小说作者
    # author = scrapy.Field()
    # 章节名字
    chap_name = scrapy.Field()
    # 章节内容
    chap_content = scrapy.Field()
#
#
# class NovelDetailItem(scrapy.Item):
#
#     章节名字
    # chapter_name = scrapy.Field()
    # 章节链接
    # chapter_urls = scrapy.Field()


# class NovelContentItem(scrapy.Item):
#
    # 小说名
    # name = scrapy.Field()
    # 章节名称
    # chap_name = scrapy.Field()
    # 章节内容
    # chap_content = scrapy.Field()
