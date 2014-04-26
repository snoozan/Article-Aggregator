from scrapy.spider import Spider
from scrapy.selector import Selector

from webs.items import WebsItem


class RedditSpider(Spider):
    name = "engadget"
    allowed_domains = ["http://www.engadget.com"]
    start_urls = ["http://www.engadget.com/tag/Python/"]

    def parse(self, response):
        sel.Selector(response)
        sites = sel.xpath('/html/body/div[2]/div/div/article')
        items = []

        for site in sites:
            item = WebsItem()
            item['url'] = sel.xpath('./a/@href').extract()

            items.append(item)

        return items
