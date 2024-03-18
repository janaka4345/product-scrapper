from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#open Chrome
driver = webdriver.Chrome()
#navigate to the site
driver.get("https://quotes.toscrape.com")

#find the h1 element
h1 = driver.find_element(By.CSS_SELECTOR, "h1")
#print the h1 element
print(f"H1 element: {h1.text}")