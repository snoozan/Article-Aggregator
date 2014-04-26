from scrapy.spider import Spider
from scrapy.selector import Selector

from webs.items import WebsItem

class RedditSpider(Spider):
    name = "reddit"
    allowed_domains = ["http://www.reddit.com"]
    start_urls = ["http://www.reddit.com/r/programming"]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('/html/body/div[3]/div[2]/div/div/div[2]')
        items = []

        for site in sites:
            item = WebsItem()
            item['url'] = sel.xpath('./p/a/@href').extract()

            items.append(item)

        return items
