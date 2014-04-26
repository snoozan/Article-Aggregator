from scrapy.spider import Spider
from scrapy.selector import Selector, HtmlXPathSelector

from webs.items import WebsItem


class HackerNewsSpider(Spider):
    name = "hackernews"
    allowed_domains = ["https://news.ycombinator.com"]
    start_urls = ["https://news.ycombinator.com/"]


    def parse(self, response):
        if 'news.ycombinator.com' in response.url:
             hxs = HtmlXPathSelector(response)
             sites = hxs.select('//td[@class="title"]//a/@href')
             items = []
             for site in sites:
                 item = WebsItem()
                 item['url'] = site.extract()

                 items.append(item)

             return items

