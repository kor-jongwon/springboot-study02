import numpy as np
import requests
from selenium import webdriver
import cv2
#import excelcrawl
from bs4 import BeautifulSoup
class crawl:
    def __init__(self):
        pass
    driver = webdriver.Chrome("/Users/choi/Downloads/chromedriver")
    #addr =excelcrawl.excelcrawl.search_subhotel_addr()##엑셀파일 에서 가져와야함 배열 로 넣을떄 하나씩 넣을껏
    addr = '3 Lisles Hill Road, Aughafatten   BT42 4LJ'
    url = "https://www.google.com/" # 접속할 url
    response = driver.get(url) # 접속 시도
    element = driver.find_element_by_name('q') #q테그찾기
    print(element)
    element.send_keys(addr) #주소값 입력
    element.submit() #검색
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    v = soup.select('.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc')
    text_arr = list()
    for i in v:
        tag = i.find_all("em")
        append_list = list()
        for j in tag:
            append_list.append(j.string)
        text_arr.append(append_list)
    #<em>테그에 있는 문자열 배열에 저장.
    #엑셀에서 가져온 sub_hotel_addr과 em 테그안에 값을 비교하여 가장 높은 정확도가 높은 사이트에 들어갈 알고리즘 필요

    for upperlist in text_arr:
        for lowerlist in upperlist:
            print(lowerlist)
    links = soup.select('.yuRUbf')
    link_arr = list()
    for link in links:
        print(link.select_one('.LC20lb.DKV0Md').text)  # 제목
        print(link.a.attrs['href'])  # 링크
        print()
        link_arr.append(i.a.attrs['href'])
        #높은 확률이 나온 링크매칭해서 그 링크로 들어감
    response = driver.get(link_arr[1]) ## /www.tripadvisor.com 에 해당 각 홈페이지에 테그 클래스 네임에 맞게 함수 필요
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    v = soup.select('._1a4WY7aS.RcPVTgNb')
    for image in v:
        url = image['src']
        image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
        image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
        print(image.shape)
        cv2.imshow('Image from url', image)
        cv2.waitKey(5000) #이미지 가져오기 성공

        #호텔스 컴바인 작업 필요 위와같이

