import requests
from bs4 import BeautifulSoup

def DollarIndex():
# 달러 인덱스 크롤링
    dollar_index_url = 'https://kr.investing.com/currencies/us-dollar-index'
    response = requests.get(dollar_index_url)
    # HTML 파싱
    soup = BeautifulSoup(response.content, "html.parser")
    dollar_index_value = soup.find("span", {"id": "last_last"})
    time_index = soup.select_one("#quotes_summary_current_data > div.instrumentDataDetails > div.left.current-data > div.bottom.lighterGrayFont.arial_11 > span.bold.pid-8827-time")
    if dollar_index_value:
        result = f"{dollar_index_value.text.strip()}"
    else:
        result = "달러 인덱스 값을 찾을 수 없습니다."
    str(result)
    return result
# print(result)

def DollarRate(tag):
    dollar_rate_url = 'https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_USDKRW&page=1'
    response = requests.get(dollar_rate_url)
    # HTML 파싱
    soup = BeautifulSoup(response.content, "html.parser")
    cells_date = soup.select_one("div > table > tbody > tr:nth-child(1) > td:nth-child(1)")
    cells_num = soup.select_one("div > table > tbody > tr:nth-child(1) > td:nth-child(2)")
    cells_date = cells_date.text.strip()
    cells_num = cells_num.text.strip()
    if tag == "date":
        return cells_date
    if tag == "num":
        return cells_num