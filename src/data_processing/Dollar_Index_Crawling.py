# 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

# 환율 정보 크롤링

# 크롤링 기간 설정 (최근 1년)
start_date = datetime.now() - timedelta(days=365)
end_date = datetime.now()


# 달러 인덱스 크롤링

# 데이터 가공

# 데이터베이스에 저장
