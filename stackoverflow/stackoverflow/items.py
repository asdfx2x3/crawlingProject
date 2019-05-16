# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StackoverflowItem(scrapy.Item):
    # 问题页地址
    question_url = scrapy.Field()
    # 问题题目
    title = scrapy.Field()
    # 收藏数
    favorite = scrapy.Field()
    # 查看人数
    views = scrapy.Field()
    # 问题文本
    question = scrapy.Field()
    # 最佳答案文本
    best_ans_text = scrapy.Field()
    # 最佳答案点赞数
    up_vote_count = scrapy.Field()
    # 最佳答案打赏数
    bounties = scrapy.Field()
