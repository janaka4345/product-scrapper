# from selenium.webdriver import chrome
# driver_path='/chromedriver'
# chrome_driver=chrome(executable_path=driver_path)
# print(chrome_driver)
# chrome_driver.get('https://www.lazada.com.my/tag/laptops/?spm=a2o4k.home-my.search.d_go&q=laptops&catalog_redirect_tag=true')
# print(chrome_driver.find_elements('By.CLASS_NAME','Bm3ON'))
import urllib
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
base_url = 'https://proxy.scrapeops.io/v1/'
params = {
    'api_key': '748837e3-9080-420f-b8cb-40fd7633145d',
      'url': 'https://www.aliexpress.com/w/wholesale-watch-smart.html?spm=a2g0o.home.discover_more.2.3a0c76dbQKztsf', 
      'render_js': 'true', 
      'residential': 'true', 
      'country': 'us', 
}

# Encode parameters
encoded_params = urllib.parse.urlencode(params)

# Build the complete URL
complete_url = base_url + encoded_params
print(complete_url)

driver = webdriver.Chrome()
#navigate to the site
# driver.get("https://proxy.scrapeops.io/v1/?api_key=748837e3-9080-420f-b8cb-40fd7633145d&url=https%3A%2F%2Fquotes.toscrape.com%2F&render_js=true&residential=true&country=us")

driver.get('https://www.aliexpress.com/w/wholesale-watch-smart.html?spm=a2g0o.home.discover_more.2.3a0c76dbQKztsf')
# driver.get(complete_url)
sleep(2)
driver.execute_script("window.scrollBy(0, 2000)")
sleep(2)
driver.execute_script("window.scrollBy(0, 2000)")
sleep(2)
driver.execute_script("window.scrollBy(0, 2000)")
sleep(2)
driver.execute_script("window.scrollBy(0, 2000)")
sleep(2)

h1 = driver.find_elements(By.CLASS_NAME, "search-item-card-wrapper-gallery")
print(len(h1))
driver.quit()
