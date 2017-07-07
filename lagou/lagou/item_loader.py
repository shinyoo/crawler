from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class CompanyItemLoader(ItemLoader):

    name_out = Join()
    foundTime_out = Join()
    location = Join()
    # status = scrapy.Field()
    business_out = Join()
    subBusiness_out = Join()
    # fundTotal = scrapy.Field()
    # evaluation = scrapy.Field()
    team_out = Join()
    description_out = Join()
    specificLocation_out = Join()
    # tel = scrapy.Field()
    # email = scrapy.Field()
    size_out = Join()
    website_out = Join()
    # the following is seemingly supposed to be
    # within a structure which is an element of
    # a list that is the direct field of the Item
    # fundTime = scrapy.Field()
    fundPhase = Join()
    # fundAmount = scrapy.Field()
    # funder = scrapy.Field()
    # the above need to be in a list say fundInfo?
    fundInfo_out = Join()