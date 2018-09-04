# -*- coding: utf-8 -*-
import scrapy

from scrapydemoExample.items import  ScrapydemoexampleItem

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):

        pass
