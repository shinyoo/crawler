# -*- coding: utf-8 -*-
import scrapy
import json
# from scrapy.loader import ItemLoader
from lagou.items import CompanyItem
from lagou.item_loader import CompanyItemLoader
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
    uri_template = 'https://www.lagou.com/gongsi/'
    company_id = 1
    ua_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
        'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
        'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'
    ]

    def start_requests(self):
        # return [FormRequest(url=self.api_url, method='POST', formdata={'pn': str(CompanySpider.pn)}, headers=self.headers)]
        while CompanySpider.company_id < 50000:
            CompanySpider.company_id = CompanySpider.company_id + 1
            yield scrapy.Request(url=self.uri_template + str(CompanySpider.company_id) + '.html', headers={'User-Agent': self.ua_list[CompanySpider.company_id % 10]})

    def parse(self, response):
        # if CompanySpider.company_id < 25000:
        #     yield scrapy.Request(self.uri_template + str(++CompanySpider.company_id) + '.html')

        l = CompanyItemLoader(item=CompanyItem(), response=response)
        l.add_css('name', '.company_main h1 a::text')
        l.add_css('website', '.company_main h1 a::attr(href)')
        found_time = response.css('.company_content p::text').re(r'成立于(\d+)')
        l.add_css('foundTime', found_time)
        l.add_css('location', 'i.address+span::text')
        # l.add_css('status', 'running')
        l.add_css('business', 'i.type+span::text')

        l.add_css('subBusiness', '.product_details li::text')

        l.add_css('team', '.manager_list li .item_manager_name span::text, .manager_list li .item_manager_title::text')

        l.add_css('description', '.company_content p::text')

        l.add_css('specificLocation',
                  '#location_container .li_title_text::text, #location_container .businessarea::text, #location_container .mlist_li_desc::text')

        l.add_css('fundPhase', '.process+span::text')
        l.add_css('size', '.number+span::text')

        # 以下信息页面上没有
        # l.add_css('email', '')
        # l.add_css('tel', '')
        # l.add_css('fund_total', '')
        # l.add_css('evaluation', '')
        yield l.load_item()
        # if response.status != 200:

    # def parse(self, response):
    #     j = json.loads(response.body)
    #     self.logger.debug(j)
    #     for k in j:
    #         i = CompanyItem()
    #         i['location'] = k['city']
    #         i['name'] = k['companyFullName']
    #         i['business'] = k['industryField']
    #         i['fundPhase'] = k['financeStage']
    #         i['description'] = k['companyFeatures']
    #         yield i
    #     ++CompanySpider.pn
    #     yield FormRequest(url=self.api_url, method='POST', formdata={'pn': str(CompanySpider.pn)}, headers=self.headers)
