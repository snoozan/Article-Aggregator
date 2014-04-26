# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from models import URLs, db_connect, create_url_table

class WebsPipeline(object):

    def __init__(self):
        """
        initializes the database session
        creates search term tables
        """
        engine = db_connect()
        create_url_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        saves all dat shit in da DB
        """
        session = self.Session()
        urls = URLs(**item)
        try:
            session.add(urls)
            session.commit()
        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item
