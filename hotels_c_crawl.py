import time
#import excelcrawl
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
class hotels_c_crawl: #호텔스 컴바인 크롤링
    def __init__(self):
        pass
    driver = webdriver.Chrome("/Users/choi/Downloads/chromedriver")
    #addr =excelcrawl.excelcrawl.search_hotels_name()##엑셀파일 에서 가져와야함 배열 로 넣을떄 하나씩 넣을껏
    hotel_name= 'Grasmere Court'
    url = "https://www.hotelscombined.co.uk/"
    response = driver.get(url)
    time.sleep(3)
    try:
        element_popup = driver.find_element_by_xpath("/html/body/div[5]/div/div[3]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/button")
        element_popup.click() #privarcy 팝업 no thanks버튼 클릭
    except:
        print("privacy popup None")
        pass
    element_text_box = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/div[1]/div[1]/div/div[1]/div/div/div/div[3]/div/div/div/div/div[1]/div[1]/div/div')

    element_text_box.click()
    time.sleep(3)
    element_input = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[1]/div[2]/div[1]/input')
    time.sleep(1)
    try:
        element_input.send_keys(hotel_name)
    except:
        driver.close()
    time.sleep(1)
    element_submit = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/div[1]/div[1]/div/div[1]/div/div/div/div[3]/div/div/div/div/div[2]/button')
    #element_submit.click() # 입력한 주소/호텔이름과 ul에 나오는 값과 매칭을 안시켜주면 검색불가
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    lists= soup.select('.QHyi.QHyi-pres-padding-default')
    time.sleep(2)
    index =0
    for i, list in enumerate(lists):
        titles = list.select('.JyN0-name')
        for i,title in enumerate(titles):
            #print(title.text) #title.text 와 비교하는 대상을 비교해서 1순위를 선택
            index =2  #검색결과로 3번째가 가장 비슷할 경우
    element_tab = driver.find
        #호텔이름과 도시이름을 매칭해보고 가장 맞는 쪽으로 선택
        #만약 리스트가 없을 경우를 봐서 예외처리 필요


    driver.close()




id="vMgI-accept"