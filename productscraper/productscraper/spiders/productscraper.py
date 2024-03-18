import scrapy


class ProductscrapperSpider(scrapy.Spider):
    name = "productscrapper"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
