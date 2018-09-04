# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#爬去数据实体类
class ScrapydemoexampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    singer = scrapy.Field()  # 定义歌手名字
    musicname = scrapy.Field()  # 定义歌曲名称

    novelname = scrapy.Field() #小说名称
    novelauthor = scrapy.Field() #小说作者
    novelhref = scrapy.Field() #小说链接



    pass
