import scrapy

class JudgmentItem(scrapy.Item):
    case_id = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    pdf_url = scrapy.Field()
    file_path = scrapy.Field()
