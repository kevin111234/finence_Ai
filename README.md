# finence_Ai  
주가변동 예측  

/data_processing  
    `데이터 수집`  
        웹 크롤링을 통해 **환율, 주가, 상장법인, 재무상태표** 등을 수집  
    `환율 데이터 전처리`  
        pandas 등의 라이브러리를 활용하여 **환율에 영향을 주는 요인 및 환율 정보**데이터 처리 후 **mysql 데이터베이스**에 데이터 저장  
    `주식 데이터 전처리`  
        pandas 등의 라이브러리를 활용하여 **재무재표, 주가 관련**데이터 처리 후 **mysql 데이터베이스**에 데이터 저장  

/analysis  
    `환율 데이터 분석 및 예측`  
        환율 데이터를 불러온 후**머신러닝 라이브러리 scikit-learn, seaborn**을 통해 환율 예측모델 생성 및 분석  
    `주식 데이터 분석`  
        주가 데이터를 불러온 후 **PER, PBR** 등 가치평가지표를 활용하여 데이터 분석 후 데이터베이스에 저장  
    `모델 선택 및 훈련`  
        **머신러닝 라이브러리 scikit-learn, seaborn**을 통해 주가 흐름 예측 및 시각화  
    `모델 평가`  
        **이후의 주가 흐름과 비교**하면서 피드백  
    `백테스팅`  
        언제 구매해서 언제 팔았다면 **얼마나 이득을 봤을 지**, **복리수익은 어느정도인지** 시각화  
  
/web/backend  
    **스프링부트를 통해 구현예정**  
  
/web/frontend  
    `웹페이지`  
        html, css, javascript 활용   
  
/db  
    `스키마 정의`  
    `데이터 삽입 스크립트`  
    `데이터 호출 스크립트`  
