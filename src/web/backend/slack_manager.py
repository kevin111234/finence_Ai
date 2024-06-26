import slack_sdk
import os, sys
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from data_processing import Dollar_Index

# 환경변수 불러오기
load_dotenv()
slack_token = os.getenv('API_TOKEN')

# slack과 파이썬 연결
client = slack_sdk.WebClient(token = slack_token)

client.chat_postMessage(channel = '#주가예측-프로그램',
                        text = f'{Dollar_Index.DollarIndex()}')