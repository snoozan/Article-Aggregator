# Scrapy settings for webs project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'webs'

SPIDER_MODULES = ['webs.spiders']
NEWSPIDER_MODULE = 'webs.spiders'

DATABASE = {'drivername': 'postgres',
        'host': 'localhost',
        'port': '5432',
        'username': 'susan',
        'database': 'articles'
        }

ITEM_PIPELINES = ['webs.pipelines.WebsPipeLine']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'webs (+http://www.yourdomain.com)'
