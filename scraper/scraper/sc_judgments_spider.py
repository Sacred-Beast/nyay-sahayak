import scrapy
import os
from .items import JudgmentItem
from urllib.parse import urljoin
from scrapy.http import Request
from scrapy.utils.project import get_project_settings

class SCJudgmentsSpider(scrapy.Spider):
    name = "sc_judgments"
    allowed_domains = ["main.sci.gov.in"]
    start_urls = ["https://main.sci.gov.in/judgments"]

    def parse(self, response):
        # Example: Find links to new judgments (simplified for demo)
        for row in response.css("table#judgments tbody tr"):
            pdf_url = row.css("a::attr(href)").get()
            if pdf_url and pdf_url.endswith(".pdf"):
                title = row.css("td::text").get()
                date = row.css("td:nth-child(2)::text").get()
                case_id = pdf_url.split("/")[-1].replace(".pdf", "")
                item = JudgmentItem(
                    case_id=case_id,
                    title=title,
                    date=date,
                    pdf_url=urljoin(response.url, pdf_url)
                )
                yield Request(item["pdf_url"], callback=self.save_pdf, meta={"item": item})

    def save_pdf(self, response):
        item = response.meta["item"]
        settings = get_project_settings()
        shared_path = settings.get("FILES_STORE", "/shared_data")
        filename = f"{item['case_id']}.pdf"
        file_path = os.path.join(shared_path, filename)
        with open(file_path, "wb") as f:
            f.write(response.body)
        item["file_path"] = file_path
        yield item
