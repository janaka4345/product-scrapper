## spider.py
# from typing import Iterable
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from urllib.parse import urlunparse

class selenimusscrapperSpider(scrapy.Spider):
    name = 'selenimusscrapper'

    def start_requests(self):
        # baseUrl = "https://www.lazada.com.my"
        # path = "/tag/xbox"
        # params = {"spm": "a2o4k.home-my.search.d_go",
        #           'q':'xbox'}

        # url = urlunparse((baseUrl.split(':')[0],  # scheme
        #                 baseUrl.split(':')[1][2:], # netloc (remove '//')
        #                 path,
        #                 None,  # fragment
        #                 urllib.parse.urlencode(params),  # query
        #                 None))
        headers={
                'accept':' application/json, text/plain, */*',
                'accept-encoding':' gzip, deflate, br',
                'accept-language':' en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,si;q=0.5',
                'bx-v':' 2.5.11',
                'cache-control':' no-cache',
                'cookie: __wpkreporterwid_=eeb1b87e-aa8e-4fc2-b9c0-7bb5862bb36d; t_fv=1710778238639; t_uid=om8FC2YlCikNj1AxWMbUdEAKYZEhdbtU; hng=MY|en-MY|MYR|458; userLanguageML=en; lzd_cid=e17068f1-2cbc-4fb4-8ea2-ce7f6f595578; cna=s3B+Hge/aBwCAXCGnO4Rv23W; lwrid=AQGOUlnOuOof3blUr2BxX39uI26G; xlly_s=1; lzd_sid=1529a8b84f882647900ee5f51f32f76c; _tb_token_=e3e5e1e30357; t_sid=8Gm2fBa5UvrUk0gCVllP1gpdzpXCtMCP; utm_origin=https':'//www.google.com/; utm_channel=SEO; __itrace_wid=7918d149-87dc-4b25-8395-8332de96cdd5; _m_h5_tk=30bdb7fc7090a1a80a346a7b61e6629c_1711250043931; _m_h5_tk_enc=4af250f93076a2716a9f75659c13776b; tfstk=fV6DoNsjKsRfVB0DA7vbEaKMWtVJhq965NH9WdLaaU8SkqHAblvGmNXTcGzfSOYlrmL2WSgGri_9kVpVI_MGAG6YcdEXhi96QyULpyIfcdgx53m3ygrwfiIswKwdciiz4qQtrJHG0RUKIF7wgLRyDUuq7N-4UuxwXqlZ3NSy5NFY91UcB4O6-DBs6PBY-QTF0E7OWT-rJeS2uAkwonA0Mi8oQAWPaVXz3EPI2F9vlItc5JMX3CfNHLW4zRJFOaXMTpVTcpjlw6dcZrkMytLkTtRuL4x5aiCNhZmiQn6ApCYBZlk66LWpT67mfksy3hSrZblEbbD64lBr1fO2V3YLHj2C7K2zZRZuqXl6g3tVbuqo1fO2V3YLqucHcI-W0G5..; isg=BFNTh_KGMoUQav5WnUr3bk_p4td9COfKls8fcQVwqnKphHMmjdqeG6nSvuzqJD_C; epssw=1*MROO11M7g5niGNzauW14MJtIh2U87RkGB1bCfc7UNbgLa92liMY8ZVz89WV-d-ROFGxMqg1WH962d3VZP_eAhhzBS5B5uEWC3h-wjscAHCLrpjYz8gDS-FAO5xC6K5PrQvzj9G5-yNNsCY2uPU6R3kJQdTHR3kmneto3xaLJFtkPYkmnyg2zzqPdkGPEFzO_aRpt38B0ya6BeDmn',
                'dnt':' 1',
                'pragma':' no-cache',
                'referer: https':'//www.lazada.com.my/',
                'sec-ch-ua':' "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile':' ?0',
                'sec-ch-ua-platform':' "Windows"',
                'sec-fetch-dest':' empty',
                'sec-fetch-mode':' cors',
                'sec-fetch-site':' same-origin',
                'sec-gpc':' 1',
                'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'x-csrf-token':' e3e5e1e30357',
                'x-requested-with':' XMLHttpRequest',
        }
        url = 'https://www.lazada.com.my/tag/xbox/?spm=a2o4k.home-my.search.d_go&q=xbox'
        yield SeleniumRequest(url=url, callback=self.parse ,headers=headers)
        def parse(self, response):
                driver = response.request.meta["driver"]
                # scroll to the end of the page 10 times
                for x in range(0, 10):
                    # scroll down by 10000 pixels
                    ActionChains(driver) \
                        .scroll_by_amount(0, 100) \
                        .perform()
        
                    # waiting 2 seconds for the products to load
                    time.sleep(5)
        
                # select all product elements and iterate over them
                # for product in driver.find_elements(By.CSS_SELECTOR, ".post"):
                #     # scrape the desired data from each product
                #     url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                #     image = product.find_element(By.CSS_SELECTOR, ".card-img-top").get_attribute("src")
                #     name = product.find_element(By.CSS_SELECTOR, "h4 a").text
                #     price = product.find_element(By.CSS_SELECTOR, "h5").text
        
                #     # add the data to the list of scraped items
                #     yield {
                #         "url": url,
                #         "image": image,
                #         "name": name,
                #         "price": price
                #     }
			 
