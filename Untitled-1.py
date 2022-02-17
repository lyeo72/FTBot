import requests
from bs4 import BeautifulSoup
import datetime

현재 = str(datetime.datetime.now())
# print(현재)

날 = "2020" + "09" + 현재[8:10]
# print(날)

req = requests.get("https://school.cbe.go.kr/chungjuja-e/M01040504/list?ymd=" + 날)
# print(req.text)
soup = BeautifulSoup(req.text, "html.parser")
# print(soup)

atag = soup.find("a", href="/chungjuja-e/M01040504/list?ymd="+날)
# print(atag)					

li = atag.find_all('li')
# print(li)
식단 = ""

for i in li:
    식단 = 식단 + i.text + "\n"
 # print(식단)


##텔레그램 봇

import telegram

토큰 ="5269381334:AAGIZI9HUq-vLCiw9T_-8qTO4GXZlwL-Pbk"
봇 = telegram.Bot(token=토큰)
# for i in 봇.getUpdates():
#    print(i.message)

봇.send_message(5295081893,식단)

