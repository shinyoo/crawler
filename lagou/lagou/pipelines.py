# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class LagouPipeline(object):

    delimiter = "\t"
    newline = "\n"

    def __init__(self):
        super(self.__class__)
        self.file = None

    def open_spider(self, spider):
        self.file = open('d:/scraped_data/target.csv', 'ab')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        for key in item.keys():
            self.file.write(item[key] + self.delimiter)
        self.file.write(self.newline)
        return item
