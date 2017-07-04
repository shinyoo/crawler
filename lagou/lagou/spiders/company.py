# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from lagou.items import CompanyItem

class CompanySpider(scrapy.Spider):
    name = "company"
    allowed_domains = ["lagou.com"]
    start_urls = ['https://www.lagou.com/gongsi/86068.html']

    def parse(self, response):
		l = ItemLoader(item=CompnayItem(), response=response)
		l.add_xpath('name', '//div[@class="product_name"]')
		l.add_xpath('name', '//div[@class="product_title"]')
		l.add_xpath('price', '//p[@id="price"]')
		l.add_css('stock', 'p#stock]')
		l.add_value('last_updated', 'today') # you can also use literal values
		return l.load_item()    	
