# 데이터 크롤링 정리.
# 환율, 달러인덱스
# 주가, 재무제표, 차트
# sql에 저장하는 방법 구분(초기 데이터 구성, 데이터 업데이트)
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from tqdm import tqdm
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

class ExchangeRateCrawler: # 데이터 구성용 class
    def __init__(self): #class 정의 시 바로 실행
        load_dotenv()
        self.db_host = os.getenv('DB_HOST')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.db_name = os.getenv('DB_NAME')
        self.db_port = os.getenv('DB_PORT')
        self.base_url = 'https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_USDKRW&page='
        self.date_list = []
        self.rate_list = []

    def generate_urls(self, pages): # url 구성
        return [f'{self.base_url}{i+1}' for i in range(pages)]
    
    def crawl_data(self, urls): # 크롤링 진행
        for url in tqdm(urls, desc="크롤링 진행도", unit="page"):
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            for row in soup.find_all("tr"):
                cells_date = row.find_all("td", class_="date")
                cells_num = row.find_all("td", class_="num")
                if cells_date and cells_num:
                    date_text = cells_date[0].text.strip()
                    rate_text = cells_num[0].text.strip().replace(",", "")
                    self.date_list.append(date_text)
                    self.rate_list.append(float(rate_text))

    def create_dataframe(self): # 데이터프레임으로 변환
        return pd.DataFrame({
            "날짜": self.date_list,
            "환율": self.rate_list
        })

    def save_to_database(self, df): # 데이터베이스에 저장
        db_url = f'mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'
        engine = create_engine(db_url)
        df.to_sql('exchange_rate', con=engine, if_exists='replace', index=False)

    def run(self): # 함수 실행문
        urls = self.generate_urls(37)
        self.crawl_data(urls)
        df = self.create_dataframe()
        print(df, "다음 내용을 데이터베이스에 저장합니다...")
        self.save_to_database(df)
        print("데이터베이스에 저장 완료!")

class ExchangeRateData: # 환율 관련 추가 데이터 크롤링 class
    def __init__(self):
        print()

# 필요한 데이터
"""
경제 성장률: 한국의 경제 성장률이 미국보다 높으면 원화가 강세를 보이고, 반대의 경우 달러화가 강세를 보입니다.

무역 수지: 한국의 대미 무역 수지 흑자 규모가 클수록 원화 강세 압력이 높아집니다. 반대로 무역 적자가 커지면 달러화 강세 압력이 높아집니다.

금리 차이: 미국의 기준금리가 한국보다 높으면 달러화 강세 요인이 됩니다.

외국인 투자 동향: 외국인의 한국 주식 및 채권 투자 규모 변화가 환율에 영향을 줍니다. 외국인 자금 유출시 원화 약세 요인이 됩니다.

국제 원자재 가격: 국제 유가, 곡물 가격 등 원자재 가격 변동은 수출입 물가에 영향을 미쳐 환율 변동을 초래합니다.

시장 심리: 투자자들의 환율에 대한 심리적 기대감도 실제 환율 변동에 영향을 줍니다.
"""

"""
무역수지
    무역수지 데이터는 보통 월별로 발표되므로 월별 시계열 데이터로 구축
    무역수지 금액을 GDP 대비 비율로 변환하여 활용하면 더욱 유의미한 지표가 될 수 있음
    계절성 요인 제거를 위해 12개월 이동평균 등을 활용할 수 있음

금리 차이
    한국과 미국의 정책금리, 국채금리, 회사채금리 등 다양한 금리지표를 활용 가능
    두 국가 간 금리 차이를 계산하여 시계열 데이터로 구축
    금리 데이터는 일별, 주별 등 고빈도로 관측되므로 적절한 주기로 집계

외국인 투자 동향
    외국인의 주식/채권 순매수 규모를 시계열 데이터로 구축
    외국인 투자 비중 등 다른 지표들도 함께 고려할 수 있음
    계절성, 추세 등 제거를 위해 데이터 정규화 및 차분 등의 전처리 필요

경제성장률 차이
    한국과 미국의 분기별 GDP 성장률 데이터를 활용
    두 국가 간 성장률 차이를 계산하여 시계열 데이터로 구축
    계절조정 데이터 사용, 전년동기 대비 증감률 등으로 변환 가능

물가상승률 차이
    한국과 미국의 소비자물가지수(CPI) 데이터를 활용
    두 국가 간 물가상승률 차이를 계산하여 시계열 데이터로 구축
    계절조정, 근원 물가지수 등으로 변환하여 활용 가능

정책금리 차이
    한국과 미국의 기준금리 데이터를 활용
    두 국가 간 정책금리 차이를 계산하여 시계열 데이터로 구축

국제 원자재 가격
    국제 유가, 곡물가격 등의 시계열 데이터를 구축
    가격 변동성, 변동폭 등의 지표로 활용 가능
"""
