# 웹스크롤링을 위한 코드로 크롤링 이외의 상황에 사용되지는 않음

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# mongodb 연결
from pymongo import MongoClient
mongoclient = MongoClient("mongodb://192.168.10.235:27017")
database = mongoclient['click_tech']
coll = database['gifty_info']


browser = webdriver.Chrome()
browser.get(str("https://www.giftishow.com/brand/brandList.mhows"))


# 각 항목에 대한 요소들
for i in range(16) :
    # 항목 클릭하기
    browser.find_element(by=By.CSS_SELECTOR, value="#swiperWrapper > li.swiper-slide.categorylist_23").click()
    # 마지막까지 스크롤하기
    element_body = browser.find_element(by=By.CSS_SELECTOR, value="body")
    previous_scrollHeight = 0
    while True : 
        element_body.send_keys(Keys.END)

        current_scrollHeight = browser.execute_script("return document.body.scrollHeight")
        if previous_scrollHeight >= current_scrollHeight:
            break
        else : 
            previous_scrollHeight = current_scrollHeight
        time.sleep(1)
        pass
    
    # 아이템 선택해서 저장하기
    while True : 
        try : 
            browser.find_element(by=By.CSS_SELECTOR, value="#goodsSection > li").click()
            gifty_style = browser.find_element(by=By.CSS_SELECTOR, value="#swiperWrapper > li > a > p") # 스타일
            # 데이터 뽑아오기
            gifty_image =  browser.find_element(by=By.CSS_SELECTOR, value="#renewal > div.giftyDetail.comp > div > div.imgWrap > img") #이미지
            gifty_brand = browser.find_element(by=By.CSS_SELECTOR, value="div > div.txtWrap > div.txtWrap-min > a > div > span") #브랜드
            gifty_name =  browser.find_element(by=By.CSS_SELECTOR, value="div > div.txtWrap > div.txtWrap-min > div.giftyNm") #제품 이름
            gifty_price =  browser.find_element(by=By.CSS_SELECTOR, value="div.txtWrap > div.txtWrap-min > div.giftyPrice > span") #가격
            # 상세 정보 이미지
            try :  
                gifty_detail_image = browser.find_element(by=By.CSS_SELECTOR, value="#cont2 > p") #상세정보 이미지
            except NoSuchElementException :
                pass
            gifty_detail = browser.find_element(by=By.CSS_SELECTOR, value="#cont1 > pre")
            browser.find_element(by=By.CSS_SELECTOR, value="div:nth-child(1) > div > div.tab.current").click() #주의사항 클릭
            gifty_caution = browser.find_element(by=By.CSS_SELECTOR, value="#cont2 > p").click() # 주의사항 저장
            # 상세정보 이미지
            browser.find_element(by=By.CSS_SELECTOR, value="div:nth-child(1) > div > div:nth-child(3)").click() #이용방법 클릭
            try : 
                gifty_method = browser.find_element(by=By.CSS_SELECTOR, value="#cont3 > ul") #이용방법 이미지
            except NoSuchElementException : 
                pass
            pass
            browser.back()

            coll.insert_one({'gifty_style' : gifty_style, 'gifty_image' : gifty_image, 'gifty_brand' : gifty_brand, 'gifty_name' : gifty_name, 'gifty_price' : gifty_price, 'gifty_detail_image' : gifty_detail_image, 'gifty_detail' : gifty_detail, 'gifty_cautioin' : gifty_caution, 'gifty_method' : gifty_method})



        except NoSuchElementException :
            break






