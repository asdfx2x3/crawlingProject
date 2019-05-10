import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


num = 1
class NovelSpider(CrawlSpider):
    name = 'novel'
    allowed_domains = ['novel.zhwenpg.com']
    start_urls = ['https://novel.zhwenpg.com/b.php?id=8uncbn']

    rules = (
        Rule(LinkExtractor(allow=r'r\.\w{3}\?\w{2}='), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'php\?page=\d+&order'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)

    def parse_body(self, response):
        pass
