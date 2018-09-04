# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class ScrapydemoexamplePipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('localhost','root','root','test')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        sql = "insert into novel(name,author,href) values(%s,%s,%s)"
        self.cursor.execute(sql,(item['novelname'],item['novelauthor'],item['novelhref']))
        self.conn.commit()
        if item['novelname'] is None:
            self.conn.close()
        return item
