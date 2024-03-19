from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#open Chrome
driver = webdriver.Chrome()
#navigate to the site
driver.get("https://proxy.scrapeops.io/v1/?api_key=748837e3-9080-420f-b8cb-40fd7633145d&url=https%3A%2F%2Fquotes.toscrape.com%2F&render_js=true&residential=true&country=us")

sleep(5)
driver.execute_script("window.scrollBy(0, 2000)")
#find the h1 element
h1 = driver.find_element(By.CSS_SELECTOR, "h1")
#print the h1 element
print(f"H1 element: {h1.text}")