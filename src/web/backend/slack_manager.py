import slack_sdk
import os
from dotenv import load_dotenv

# 환경변수 불러오기
load_dotenv()
slack_token = os.getenv('API_TOKEN')

# slack과 파이썬 연결
client = slack_sdk.WebClient(token = slack_token)

client.chat_postMessage(channel = '#주가예측-프로그램',
                        text = '')