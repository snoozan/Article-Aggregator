from scrapy.spider import Spider
from scrapy import log
from scrapy.selector import HtmlXPathSelector

from webs.items import WebsItem

class RedditSpider(Spider):
    name = "reddit"
    allowed_domains = ["http://www.reddit.com"]
    start_urls = ["http://www.reddit.com/r/programming"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//*[@id="siteTable"]/div/div[@class="entry unvoted"]//p[@class="title"]/a/@href')
        items = []

        for site in sites:
            item = WebsItem()
            item['url'] = site.extract()

            items.append(item)


        return items
