from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
import time
import datetime
import schedule
import telegram


try:
    shutil.rmtree(r"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
except FileNotFoundError:
    pass

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)

driver.get("https://www.freitag.ch/en/f41") ## 자동으로 들어갈 주소 입력



#쿠키 저장안함
driver.find_element_by_class_name('dismiss-cookies').click()


#프탁봇 실행

def ft_bot():

    global curr_items
    global new_src
    
    curr_items = new_src.copy()
    
    #프탁봇 주소 넣기
    token = "5274933678:AAE8ly2W28ghf-n1SGdYEEjQdY2A35HASIs"
    bot = telegram.Bot(token)
    
    
    bot.send_message(5295081893,new_items[0]+"\n 상품이 업데이트 되었습니다")
    
    
    


#새로운 아이템이 업데이트 여부
def check_new_item():
    
    global curr_items
    global new_src
    global new_items
    
    driver.refresh()
    
    #전체 상품 조회
    driver.find_element_by_css_selector('#block-freitag-content > article > section:nth-child(2) > div > div > div > div > div:nth-child(2) > div.container.mx-auto > div > div > a > div').click()

    print(str(datetime.datetime.now()) +' 프라이탁에서 재입고된 아이템이 있는지 확인합니다')
    
    for item in driver.find_elements_by_css_selector('#block-freitag-content > article > section:nth-child(2) > div > div > div > div > div:nth-child(2) > div.container.mx-auto > div > div > div > div.flex.flex-wrap > div:nth-child(n) > div > picture > img'):
        new_src.append(item.get_attribute('src'))
        
    
    # update_src =[]
    
    # for value in new_src:
    #     if value not in update_src:
    #         update_src.append(value)
    
    # print(len(update_src))
    
    
    print(len(curr_items))
    print(len(new_src))
    
    
    
    
    new_items = [x for x in new_src if x not in curr_items]
    print(len(new_items))    
        
    if len(new_items) != 0:
        ft_bot()
        print("재입고 되었습니다")
    
            
    else:
        print("재입고 되지 않았습니다")
    
      
            
new_items =[]            
curr_items =[]
new_src=[]


#새로운 아이템 체크
check_new_item()


# 1분에 한번씩 실행
schedule.every(1).minutes.do(check_new_item)

while True:
    schedule.run_pending()
    time.sleep(1)
