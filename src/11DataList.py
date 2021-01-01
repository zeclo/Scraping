import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

load_url = "http://kabuka.biz/riron/7000/7238.htm"
# 決算データ → 取得OK
load_url = "https://www.nikkei.com/markets/kigyo/money-schedule/kessan/?ResultFlag=3&kwd=7777"
#株価データ → 取得NG 株価が埋め込まれていない
load_url = "https://jp.kabumap.com/servlets/kabumap/Action?SRC=basic/top/base&codetext=7777"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
print(soup)
