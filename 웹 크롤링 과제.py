from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time

ask=input("웹사이트 주소: ") #사이트 입력받기
while True:
    now = datetime.now() #시작 시간 측정
    now1 = "%s%s%s%s%s"%(now.year,now.month,now.day,now.hour,now.minute) #파일명 생성을 위한 작업

    url = "https://www.skku.edu/skku/campus/skk_comm/news.do" #웹사이트명 저장
    a = urlopen(url)
    page = BeautifulSoup(a.read(), "html.parser") #웹사이트를 불러들이는 작업
    file = open(now1+'.csv', 'w',newline='') #csv파일 열기위한 작업
    writer = csv.writer(file)
    writer.writerow(['제목', '내용', '기사 번호', '작성 날짜','조회수']) #첫 행 저장
    news_list = page.find('div', {"class":"news_listWrap"}).find('ul',{'class': 'news_list'}).find_all('li', {'class': ' '}) #묶음 대상을 포괄하는 태그 저장

    for news in news_list: #각 하위태그들로부터 원하는 정보를 불러들이기 위한 반복문 실행
        tc = news.find('div',{'class': 'news_listCont'}) #공통적인 상위 태그 불러들이기
        title = tc.find('h4').find('a').text.strip() #제목
        content = tc.find('p').text.strip() #내용
    
        info = tc.find('ul',{'class': 'news_iconList'}).find_all('li') #공통적인 묶음 대상을 포괄하는 상위 태그 저장
        num = info[0].find('span').text.strip() #기사 번호
        time = info[1].find_all('span')[1].text #작성 날짜
        view = info[2].find_all('span')[1].text #조회수

        writer.writerow([title, content, num, time, view]) #하나로 묶어 각 행에다가 저장
    file.close() #파일 닫아주기

    print(now1+'.csv' '파일에 크롤링 결과가 저장되었습니다.') #파일 저장되었음을 알리기
    now2 = datetime.now() #완료 시간 측정
    print("소요 시간: %s"%(now2-now)) #소요 시간
    print("시작 시간: %s년 %s월 %s일 %s시 %s분 %s초"%(now.year,now.month,now.day,now.hour,now.minute,now.second)) #시작 시간
    print("완료 시간: %s년 %s월 %s일 %s시 %s분 %s초"%(now2.year,now2.month,now2.day,now2.hour,now2.minute,now2.second)) #완료 시간

    cont=input("계속 하시겠습니까?(Y/N)")
    while not (cont=='Y' or cont=='y' or cont=='N' or cont=='n'):
        cont=input("계속 하시겠습니까?(Y/N)")
    if cont=="y" or cont=="Y":
        ask=input("웹사이트 주소: ") #사이트 입력받기
        continue
    else:
        break

print("안녕히 가십시오") #종료 알리기
    
