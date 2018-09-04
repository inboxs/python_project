# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class RenrenchespiderSpider(scrapy.Spider):
    name = 'renrenchespider'
    allowed_domains = ['www.renrenche.com']
    start_urls = ['https://www.renrenche.com/xa/ershouche/?fr=hao123&tg_aid=10029701']

    def parse(self, response):
        #网页数据爬取

        lis = response.xpath("//ul[@class='row-fluid']")
        print('lis中数据个：%d'%len(lis))
        print(lis)
        # for i in lis:


        pass
