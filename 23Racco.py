import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

load_url = "https://related-keywords.com/result/suggest?q=%E3%83%80%E3%82%A4%E3%82%A8%E3%83%83%E3%83%88"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
print(soup)
