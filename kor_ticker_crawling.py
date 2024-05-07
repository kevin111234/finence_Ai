import requests as rq
from bs4 import BeautifulSoup
import re
from io import BytesIO
import pandas as pd

import pymysql

import json
import time
from tqdm import tqdm

#날짜 데이터 크롤링
url_naverfinence='https://finance.naver.com/sise/sise_deposit.nhn'
data=rq.get(url_naverfinence)
