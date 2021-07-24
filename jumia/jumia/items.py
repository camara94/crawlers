# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    designation = scrapy.Field()
    image = scrapy.Field()
    prix = scrapy.Field()
    pourcent = scrapy.Field()
