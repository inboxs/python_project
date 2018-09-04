# -*- coding: utf-8 -*-
import scrapy


class DouanmoviespiderSpider(scrapy.Spider):
    name = 'douanmoviespider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/cinema/nowplaying/beijing/']

    def parse(self, response):
        pass
