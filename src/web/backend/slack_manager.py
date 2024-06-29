import slack_sdk
import os, sys
from dotenv import load_dotenv
import Dollar_Index
import json
import requests

def notice_message(token, channel, text, attachments):
    attachments = json.dumps(attachments) # 리스트는 Json 으로 덤핑 시켜야 Slack한테 제대로 간다.
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel, "text": text ,"attachments": attachments})


str1_title = f"{Dollar_Index.DollarRate("date")}일 현재 환율정보"
link = 'https://kr.investing.com/currencies/us-dollar-index'
str2_text = "환율정보 안내를 시작합니다."
text = f'''
환율: {Dollar_Index.DollarRate("num")}
달러 인덱스: {Dollar_Index.DollarIndex()}
'''

attach_dict = {
    'color' : '#ff0000',
    'author_name' : 'Slack Bot Notice',
    'title' : str1_title,
    'title_link' : link,
    'text' : text
}
attach_list = [attach_dict]

# 환경변수 불러오기
load_dotenv()
slack_token = os.getenv('API_TOKEN')

# slack과 파이썬 연결
client = slack_sdk.WebClient(token = slack_token)

notice_message(slack_token, "#주가예측-프로그램", str2_text, attach_list)