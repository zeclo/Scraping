import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

load_url = "http://aramakijake.jp/keyword/index.php?keyword=%E3%83%9C%E3%83%87%E3%82%A3%E3%83%A1%E3%82%A4%E3%82%AF"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
print(soup)
