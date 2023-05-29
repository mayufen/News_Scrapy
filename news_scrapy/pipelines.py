# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from Config import Config
import pymysql


class NewsScrapyPipeline:

    def __init__(self):
 
        self.connect = pymysql.connect(
            host=Config.mysql_host,
            port=Config.mysql_port,
            db=Config.mysql_db,
            user=Config.mysql_user,
            passwd=Config.mysql_pwd,
            charset='utf8'
        )
 
        self.cursor = self.connect.cursor()
    
    def process_item(self, item, spider):
 
        sql = 'INSERT INTO news(title, url, summary, date)VALUES(%s,%s,%s,%s) '
 
        data = (item['title'], item['url'], item['summary'], item['date'])
 
        self.cursor.execute(sql, data)
 
        return item
    
    def close_spider(self, spider):
        self.connect.commit()
        self.connect.close()
