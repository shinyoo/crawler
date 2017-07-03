# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CompanyItem(scrapy.Item):
	name = scrapy.Field()
	website = scrapy.Field()
	foundTime = scrapy.Field()
	location = scrapy.Field()
	status = scrapy.Field()
	business = scrapy.Field()
	subBusiness = scrapy.Field()
	fundTotal = scrapy.Field()
	evaluation = scrapy.Field()
	team = scrapy.Field()
	description = scrapy.Field()
	specificLocation = scrapy.Field()
	tel = scrapy.Field()
	email = scrapy.Field()
	
	# the following is seemingly supposed to be
	# within a structure which is an element of
	# a list that is the direct field of the Item 
	fundTime = scrapy.Field()
	fundPhase = scrapy.Field()
	fundAmount = scrapy.Field()
	funder = scrapy.Field()
	# the above need to be in a list say fundInfo?
	# fundInfo = ?


