# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CryptocurrencyspiderItem(scrapy.Item):
    name = scrapy.Field()
    marketcap = scrapy.Field()
    price = scrapy.Field()


class DataItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()
    open = scrapy.Field()
    close = scrapy.Field()
    change1 = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    change2 = scrapy.Field()
    volume = scrapy.Field()
    marketcap = scrapy.Field()


class NewItem(scrapy.Item):
    name = scrapy.Field()

class HistoryItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()
    open = scrapy.Field()
    close = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    volume = scrapy.Field()
    marketcap = scrapy.Field()

