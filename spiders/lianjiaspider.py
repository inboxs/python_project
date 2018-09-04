# -*- coding: utf-8 -*-
import scrapy


class LianjiaspiderSpider(scrapy.Spider):
    name = 'lianjiaspider'
    allowed_domains = ['xa.fang.lianjia.com']
    start_urls = ['https://xa.fang.lianjia.com/loupan/']

    def parse(self, response):
        lis=response.xpath("//ul[@class='resblock-list-wrapper']")
        print(lis)

        for i in lis:
            print("aaa",i.xpath("//div[@class='resblock-name']/a").extract()[0])
            print("aaa",i.xpath("//div[@class='resblock-name']/span").extract()[0])
            print("aaa",i.xpath("//div[@class='resblock-name']/span").extract()[1])
            print("aaa",i.xpath("//div[@class='resblock-desc-wrapper']/div[@class='resblock-location']/span").extract()[0])
            print("aaa",i.xpath("//div[@class='resblock-desc-wrapper']/div[@class='resblock-location']/span").extract()[1])
            print("aaa",i.xpath("//div[@class='resblock-desc-wrapper']/div[@class='resblock-location']/a").extract()[0])


        pass
