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
        result = f"현재 달러 인덱스 값: {dollar_index_value.text.strip()}"
    else:
        result = "달러 인덱스 값을 찾을 수 없습니다."
    str(result)
    return result
# print(result)