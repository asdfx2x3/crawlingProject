# -*- coding: utf-8 -*-
import scrapy
from tianyankan.items import TianyankanItem


"""
1. 通过遍历最近更新列表中的小说, 达到把全站小说都下载下来的目的.
2. 每部小说都分开在每个目录下存放, 可以更有条例.
3. 其他相关设置比如 时延, UA, 代理等的设置
4. 将要优化方向: 正文的排版完善, 爬虫性能提升.
5. 输出正文内容的同时, 把 url 以及章节名也存进 mongodb.
"""

class NovelsSpider(scrapy.Spider):
    name = 'novels'
    allowed_domains = ['novel.zhwenpg.com']
    start_urls = []
    for num in range(2, 14):  # 最大页码为 14 设为 2 方便测试
        # "更新"页数遍历: 总共 13 页
        start_urls.append('https://novel.zhwenpg.com/index.php?page={}&order=1'.format(num))

    def parse(self, response):
        # item = TianyankanItem()
        # info = response.xpath('//div[@align="center"]/div/table/tr/td/div[@class="cover_wrapper_s"]')
        # for i in info:
        #     items['title'] = i.xpath('a/div/text()').extract_first()  # 小说名
        #     items['urls'] = 'https://' + self.allowed_domains[0] + i.xpath('a/@href').extract_first() 小说详情页
        #     yield items

        # for name_list in response.xpath('//div[@align="center"]/div/table/tr[1]/td[2]/a//text()').getall():
        #     item['title'] = name_list
        #     yield item

        # 这是每个小说最新章节的目录界面
        for url in response.xpath('//div[@align="center"]/div/table/tr[4]/td/a/@href').getall():
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.parse_chapter)

    def parse_chapter(self, response):
        item = TianyankanItem()

        title = response.xpath('/html/head/title/text()').get().split('_')[0]
        content = response.xpath('//td/span[@class="content"]//text()').getall()
        item['title'] = title
        item['chap_name'] = response.xpath('//div/div/table[3]/tr/td/h2/text()').get()
        item['chap_content'] = '\n'.join(content)
        yield item
        # chap_name = response.xpath('//div/div/table[3]/tr/td/h2/text()').get()
        # sort_content = '\n'.join(content)
        # yield {
        #     chap_name: sort_content,
        # }

        # 获取下一章链接, 调用回调函数, 获得下一章节文本
        prev_page = response.xpath('//div/div/table[4]/tr/td[1]/a/@href').get()
        if prev_page is not None:
            prev_page = response.urljoin(prev_page)
            yield scrapy.Request(prev_page, callback=self.parse_chapter)
        # 只需要获取第一章或者最后一章即可
        # 后续的只需要在第一张中获取下一页
        # 进入循环即可获取全部章节
        # t = response.text
        # yield t
        # for first_chap in response.xpath('//ul[@class="clistcontainer"]/li[1]/a/@href').getall():
        #     first_chap = response.urljoin(first_chap)
        #     print(first_chap)
        # yield Request(first_chap, callback=self.parse_content)

    # def parse_content(self, response):
    #     pass
"""

class NovelsSpider(scrapy.Spider):
    name = 'novels'
    allowed_domains = ['novel.zhwenpg.com/']
    start_urls = ['https://novel.zhwenpg.com/index.php?genre=10000']

    def parse(self, response):
        # 导入 items 中的容器类 保存主页面信息
        items = TianyankanItem()
        info = response.xpath('//div[@align="center"]/div/table/tr/td/div[@class="cover_wrapper_s"]')
        # 遍历获取题目信息, 和单个小说的详情页
        for i in info:
            items['title'] = i.xpath('a/div/text()').extract_first()
            items['urls'] = 'https://' + self.allowed_domains[0] + i.xpath('a/@href').extract_first()
            yield items

        yield Request(items['urls'], self.single_detail)

        # for url in items['urls']:
        #     yield Request(url, callback=self.single_detail)

    def single_detail(self, response):
        # 导入 items 容器类 保存小说详情页面信息
        novel_items = NovelDetailItem()
        chap_infos = response.xpath('//ul[@class="clistcontainer"]//li')
        # chap_name_list = response.xpath('a/text()').extract()
        # chap_content_urls = response.xpath('//')
        for chap_info in chap_infos:
            novel_items['chapter_name'] = chap_info.xpath('a/text()').extract_first()
            novel_items['chapter_urls'] = 'https://' + self.allowed_domains[0] + chap_info.xpath('a/@href').extract_first()
            yield novel_items

        # for single_chap in novel_items['chapter_urls']:
        #     yield Request(single_chap, callback=self.content)

    def content(self, response):
        # 导入 items 容器类 保存小说章节内容
        content_items = NovelContentItem()
        # 章节内容
        content_text = response.xpath('//span[@class="content"]/text()').extarct()
        # 章节名字
        content_name = response.xpath('//td[@align="center"]/h2/text()').extract_first()

        for text in content_text:
            content_items['chap_content'] = text
            yield content_items
            """
