# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.loader import ItemLoader
from lagou.items import CompanyItem
from scrapy.http import FormRequest, Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CompanySpider(scrapy.Spider):

    name = "company"
    allowed_domains = ["lagou.com"]
    api_url = 'https://www.lagou.com/gongsi/0-0-0.json'
    headers = {'X-Anit-Forge-Code': 0, 'X-Anit-Forge-Token': 'None', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    pn = 1
    # handle_httpstatus_list = [301, 302, 303]
    # start_urls = ['https://www.lagou.com/gongsi/1000.html']
    # rules = (
    #     Rule(LinkExtractor(allow=(r'.*\.html',)), callback='parse_item'),
    # )
    # uri_template = 'https://www.lagou.com/gongsi/'
    # company_id = 1

    def start_requests(self):
        return [FormRequest(url=self.api_url, method='POST', formdata={'pn': CompanySpider.pn}, headers=self.headers)]
        # return [scrapy.Request(self.uri_template + str(CompanySpider.company_id) + '.html')]

    # def parse(self, response):
    #     if CompanySpider.company_id < 25000:
    #         yield scrapy.Request(self.uri_template + str(++CompanySpider.company_id) + '.html')
    #
    #     l = ItemLoader(item=CompanyItem(), response=response)
    #     l.add_css('name', '.company_main h1 a::text')
    #     l.add_css('website', '.company_main h1 a::attr(href)')
    #     found_time = response.css('.company_content p::text').re(r'成立于(\d+)')
    #     l.add_css('foundTime', found_time)
    #     l.add_css('location', 'i.address+span::text')
    #     # l.add_css('status', 'running')
    #     l.add_css('business', 'i.type+span::text')
    #
    #     subs = response.css('.product_details li::text')
    #     for li in subs:
    #         l.add_css('subBusiness', li.extract())
    #
    #     managers = response.css('.manager_list li')
    #     for li in managers:
    #         l.add_css('team', li.css('.item_manager_name span::text').extract() + li.css('.item_manager_title::text'))
    #
    #     desc = response.css('.company_content p::text')
    #     for p in desc:
    #         l.add_css('description', p.extract())
    #
    #     l.add_css('specificLocation',
    #               '#location_container .li_title_text::text, #location_container .businessarea::text, #location_container .mlist_li_desc::text')
    #
    #     l.add_css('fundPhase', '.process+span::text')
    #     l.add_css('size', '.number+span::text')
    #
    #     # 以下信息页面上没有
    #     # l.add_css('email', '')
    #     # l.add_css('tel', '')
    #     # l.add_css('fund_total', '')
    #     # l.add_css('evaluation', '')
    #     yield l.load_item()
    #     # if response.status != 200:

    def parse(self, response):
        j = json.load(response.body)
        for k in j:
            i = CompanyItem()
            i['location'] = k['city']
            i['name'] = k['companyFullName']
            i['business'] = k['industryField']
            i['fundPhase'] = k['financeStage']
            i['description'] = k['companyFeatures']
            yield i
        ++CompanySpider.pn
        yield FormRequest(url=self.api_url, method='POST', formdata={'pn': CompanySpider.pn}, headers=self.headers)
