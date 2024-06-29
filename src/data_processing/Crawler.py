# 메인 크롤러 실행 파일
import Exchange_Rate_Crawling

# 환율 데이터 크롤링
i = input('환율데이터를 크롤링하시겠습니까?(y/n): ')
if i == 'y':
    crawler = Exchange_Rate_Crawling.ExchangeRateCrawler()
    crawler.run()