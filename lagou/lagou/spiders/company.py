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
		l.add_css('name', '.company_main h1 a::text')
		l.add_css('website','.company_main h1 a::attr(href)')
		foundTime = response.css('.company_content p::text').re(r'成立于(\d+)')
		l.add_css('foundTime', foundTime)
		l.add_css('location', 'i.address+span::text')
		l.add_css('status', '运营中')
		l.add_css('business', 'i.type+span::text')

		subs = response.css('.product_details li::text')
		for li in subs:
			l.add_css('subBusiness', li.extract())

		managers = response.css('.manager_list li') 
		for li in managers:
			l.add_css('team', li.css('.item_manager_name span::text').extract() + li.css('.item_manager_title::text'))

		desc = response.css('.company_content p::text')
		for p in desc:
			l.add_css('description', p.extract())

		l.add_css('specificLocation', '#location_container .li_title_text::text, #location_container .businessarea::text, #location_container .mlist_li_desc::text')

		l.add_css('fundPhase', '.process+span::text')
		l.add_css('size', '.number+span::text')
		
		# 以下信息页面上没有
		l.add_css('email', '')
		l.add_css('tel', '')
		l.add_css('fund_total', '')
		l.add_css('evaluation', '')

		return l.load_item()    	
