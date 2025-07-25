import os

BOT_NAME = "scraper"
SPIDER_MODULES = ["scraper"]
NEWSPIDER_MODULE = "scraper"

ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 1

SHARED_DATA_PATH = os.getenv("SHARED_DATA_PATH", "/shared_data")
FILES_STORE = SHARED_DATA_PATH
