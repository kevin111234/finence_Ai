# 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

# 환율 정보 크롤링
# 날짜 설정
today_date = datetime.now()

# 크롤링할 주소 설정
base_url = 'https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_USDKRW'

# 크롤링 수행
for page in range(37):
    url = f'{base_url}&page={page}'

# 달러 인덱스 크롤링

# 데이터 가공

# 데이터베이스에 저장
