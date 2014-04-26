from scrapy.spider import Spider
from scrapy import log
from scrapy.selector import Selector

from webs.items import WebsItem

class RedditSpider(Spider):
    name = "reddit"
    allowed_domains = ["http://www.reddit.com"]
    start_urls = ["http://www.reddit.com/r/programming"]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*[@id="siteTable"]/div/div[@class="entry unvoted"]')
        items = []

        for site in sites:
            item = WebsItem()
            item['url'] = site.xpath('.//p[@class="title"]/a/@href').extract()

            items.append(item)


        return items
