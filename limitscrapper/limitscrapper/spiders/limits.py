import scrapy
from scrapy.shell import inspect_response

class LimitsSpider(scrapy.Spider):
    name = "limits"
    # allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://drs.faa.gov/guest/login?targetUrl=/search"]

    def parse(self, response):
        inspect_response( response,self)
