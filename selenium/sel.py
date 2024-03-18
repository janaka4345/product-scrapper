# from selenium.webdriver import chrome
# driver_path='/chromedriver'
# chrome_driver=chrome(executable_path=driver_path)
# print(chrome_driver)
# chrome_driver.get('https://www.lazada.com.my/tag/laptops/?spm=a2o4k.home-my.search.d_go&q=laptops&catalog_redirect_tag=true')
# print(chrome_driver.find_elements('By.CLASS_NAME','Bm3ON'))

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#navigate to the site
driver.get('https://www.aliexpress.com/w/wholesale-watch-smart.html?spm=a2g0o.home.discover_more.2.3a0c76dbQKztsf')
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
