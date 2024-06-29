# 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from tqdm import tqdm
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# 환경변수 불러오기
load_dotenv()
DB_Host = os.getenv('DB_HOST')
DB_User = os.getenv('DB_USER')
DB_Password = os.getenv('DB_PASSWORD')
DB_Name = os.getenv('DB_NAME')
DB_Port = os.getenv('DB_PORT')

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
for url in tqdm(urls, desc="크롤링 진행도", unit="page"):
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
print(exchange_rate_df, "다음 내용을 데이터베이스에 저장합니다...")

# 데이터베이스에 저장
db_url = f'mysql+pymysql://{DB_User}:{DB_Password}@{DB_Host}:{DB_Port}/{DB_Name}'
engine = create_engine(db_url)
exchange_rate_df.to_sql('exchange_rate', con=engine, if_exists='replace', index=False)

print("데이터베이스에 저장 완료!")