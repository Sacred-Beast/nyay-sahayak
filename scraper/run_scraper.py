import os
from scrapy.crawler import CrawlerProcess
from scraper.sc_judgments_spider import SCJudgmentsSpider

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(SCJudgmentsSpider)
    process.start()
