from scrapy.spider import Spider
from scrapy.selector import Selector

from webs.items import WebsItem


class HackerNewsSpider(Spider):
    name = "hackernews"
    allowed_domains = ["https://news.ycombinator.com"]
    start_urls = ["https://news.ycombinator.com/"]


    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('/html/body/center/table/tbody/tr[3]/td/table/tbody/tr/td[3]')
        items = []

        for site in sites:
            item = WebsItem()
            item['url'] = sel.xpath('./a/@href').extract()

            items.append(item)

        return items

