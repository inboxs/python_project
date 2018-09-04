# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class ScrapydemoexamplePipeline(object):
    def process_item(self, item, spider):
        #print('item----',item)
        jsonInfo=json.dumps(dict(item),ensure_ascii=False)
        with open('novelInfo.json','a',encoding="utf-8") as wrStream:
            wrStream.write(jsonInfo+"\n")
        return item
