# -*- coding: utf-8 -*-
import scrapy
from scrapydemoExample.items import ScrapydemoexampleItem
import urllib
class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['hao123.zongheng.com']
    start_urls = ['http://hao123.zongheng.com/store/c0/w0/s0/p1/all.html']
    def __init__(self):
         self.base_url = "http://hao123.zongheng.com/"
    def parse(self, response):
        lis = response.xpath("//div[@class='infos']")
        for li in lis:
            href = li.xpath("h2/a/@href").extract()[0]
            name = li.xpath("h2/a/@title").extract()[0]
            author = li.xpath("div/span/a/text()").extract()[0]
            # print(author)
            # print(name)
            # print(href)
            item = ScrapydemoexampleItem()
            item['novelname'] = name
            item['novelauthor'] = author
            item['novelhref'] = href
            yield item
        for i in range(2,50):
            i = str(i)
            next_url = "http://hao123.zongheng.com/store/c0/w0/s0/p" + i + "/all.html"
            print(next_url)
            yield scrapy.Request(next_url)
            # print(ainfo)

        pass
