# 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import sqlalchemy
import pymysql
import os
from dotenv import load_dotenv

# 프로젝트 루트 디렉토리 경로 가져오기
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# .env 파일 경로 지정
env_path = os.path.join(project_root, 'FINENCE_AI', '.env')

# .env 파일 로드
load_dotenv(dotenv_path=env_path)

# 데이터베이스 연결 정보 가져오기
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_port = int(os.getenv('DB_PORT'))

# 환율 정보 크롤링
# 날짜 설정
today_date = datetime.now()

# 크롤링할 주소 설정
base_url = 'https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_USDKRW&page='
urls = []
for i in range(37):
    page_url = f'{base_url}{i+1}'
    urls.append(page_url)

date_list = []
rate_list = []
# 크롤링 수행
for url in urls:
    # 요청 보내기
    response = requests.get(url)
    # HTML 파싱
    soup = BeautifulSoup(response.content, "html.parser")
    # 파싱한 soup 변수에서 div > table > tbody > <tr class="up">, <tr class="down"> 모두 정리하기
    # print(soup)
    for row in soup.find_all("tr"):
        cells_date = row.find_all("td", class_="date")
        cells_num = row.find_all("td", class_="num")
        if cells_date and cells_num:
            date_text = cells_date[0].text.strip()
            rate_text = cells_num[0].text.strip().replace(",", "")
            date_list.append(date_text)
            rate_list.append(float(rate_text))

# 데이터프레임 생성
exchange_rate_df = pd.DataFrame({
    "날짜": date_list,
    "환율": rate_list
})
# print(exchange_rate_df)

# 달러 인덱스 크롤링
dollar_index_url = 'https://kr.investing.com/currencies/us-dollar-index'
response = requests.get(dollar_index_url)
# HTML 파싱
soup = BeautifulSoup(response.content, "html.parser")
dollar_index_value = soup.find("span", {"id": "last_last"})
time_index = soup.select_one("#quotes_summary_current_data > div.instrumentDataDetails > div.left.current-data > div.bottom.lighterGrayFont.arial_11 > span.bold.pid-8827-time")
if dollar_index_value:
    print(f"시간: {time_index.text.strip()} 달러 인덱스 값: {dollar_index_value.text.strip()}")
else:
    print("달러 인덱스 값을 찾을 수 없습니다.")

# 데이터베이스에 저장
