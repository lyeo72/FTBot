import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys ##셀레니움 임포트

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)  ##크롬으로 자동화


driver.get("https://www.freitag.ch/en/f41") ## 자동으로 들어갈 주소 입력



preLinks =[]

newLinks=[]

for item in driver.find_elements_by_css_selector('#block-freitag-content > article > section:nth-child(2) > div > div > div > div > div:nth-child(2) > div.container.mx-auto > div > div > div > div.flex.flex-wrap>div'):
    주소 = int(item.get_attribute('data-index'))

print(주소)





# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
