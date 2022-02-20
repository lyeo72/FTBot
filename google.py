import time
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys ##셀레니움 임포트

driver = webdriver.Chrome()

driver.get("https://www.freitag.ch/en/f41") ## 자동으로 들어갈 주소 입력

driver.find_element_by_class_name('dismiss-cookies').click()


new_items = []
for item in driver.find_elements_by_css_selector('#block-freitag-content > article > section:nth-child(2) > div > div > div > div > div:nth-child(2) > div.container.mx-auto > div > div > div > div.flex.flex-wrap > div:nth-child(n) div > picture > img'):
    image_src = item.get_attribute('src')

    new_items.append(image_src)
 
print(new_items)

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
