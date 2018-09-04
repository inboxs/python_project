# -*- coding: utf-8 -*-
import scrapy
from scrapydemoExample.items import ScrapydemoexampleItem #导入实体类

class KugouspiderSpider(scrapy.Spider):
    name = 'kugouspider'
    allowed_domains = ['www.kugou.com']
    start_urls = ['http://www.kugou.com/yy/html/rank.html']

    def parse(self, response):
        #网页数据爬取
        lis = response.xpath("//li[@class=' ']")
        print('lis中数据个：%d'%len(lis))
        print(lis)

        # for li in lis:
        #     info = li.xpath("a/text()").extract()[0]
        #
        #     singer=info.split("-")[0]
        #     print(singer)
        #
        #     musicName = info.split("-")[1]
        #     print(musicName)
        #     musicItem = ScrapydemoexampleItem()
        #
        #     musicItem['singer'] = singer
        #     musicItem['musicname'] = musicName
        #     yield musicItem
        pass
