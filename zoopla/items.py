# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZooplaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    Name = scrapy.Field()
    Phone = scrapy.Field()
    #Address = scrapy.Field()
    Street = scrapy.Field()
    Locality = scrapy.Field()
    Zipcode = scrapy.Field()
    #Description = scrapy.Field()
    Website = scrapy.Field()
    #Domain = scrapy.Field()
    #Yell_Image_Url = scrapy.Field()
    pass
