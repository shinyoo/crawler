# -*- coding: utf-8 -*-
import scrapy


class CompanySpider(scrapy.Spider):
    name = "company"
    allowed_domains = ["lagou.com"]
    start_urls = ['http://lagou.com/']

    def parse(self, response):
        pass
