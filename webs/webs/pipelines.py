# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker

class WebsPipeline(object):

    def __init__(self):
        """
        initializes the database session
        creates search term tables
        """
        engine = db_connect()
        #create_*_table(engine)
        self.Session = sessionmakers(bind=engine)

    def process_item(self, item, spider):
        """
        saves all dat shit in da DB
        """
        return item
