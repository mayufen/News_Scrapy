# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsScrapyItem(scrapy.Item):

    title = scrapy.Field()
    url = scrapy.Field()
    summary = scrapy.Field()
    date = scrapy.Field()
