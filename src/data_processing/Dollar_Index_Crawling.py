# 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

# 환율 정보 크롤링
# 날짜 설정
today_date = datetime.now()

# 크롤링할 주소 설정
base_url = 'https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_USDKRW&page='
urls = []
for i in range(1): # 나중에 37로 수정하기
    page_url = f'{base_url}{i+1}'
    urls.append(page_url)
print(urls)

# 크롤링 수행
for url in urls:
    # 요청 보내기
    response = requests.get(url)
    # HTML 파싱
    soup = BeautifulSoup(response.content, "html.parser")
    # 파싱한 soup 변수에서 div > table > tbody > <tr class="up">, <tr class="down"> 모두 정리하기
    print(soup)


# 달러 인덱스 크롤링

# 데이터 가공

# 데이터베이스에 저장
