from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector

from webs.items import WebsItem


class RedditSpider(Spider):
    name = "engadget"
    allowed_domains = ["http://www.engadget.com"]
    start_urls = ["http://www.engadget.com/tag/Python/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('/html/body/div[2]/div/div/article/a/@href')
        items = []

        for site in sites:
            item = WebsItem()
            item['url'] = site.extract()

            items.append(item)

        return items
