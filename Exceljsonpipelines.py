# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from openpyxl import Workbook
class ScrapydemoexamplePipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['小说名称', '小说作者', '小说链接'])  # 设置表头
    def process_item(self, item, spider):
        print(item['novelname'])
        line = [item['novelname'], item['novelauthor'], item['novelhref']]  # 把数据中每一项整理出来
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('C:\\novel\\novel.xlsx')  # 保存xlsx文件
        return item
