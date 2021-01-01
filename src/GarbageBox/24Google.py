import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

load_url = "https://www.google.com/search?safe=off&sxsrf=ALeKk01RMvd019FexMuWWYrKLUN3jM6D9g%3A1605183994975&ei=-imtX7eMO4-2mAXnpYzABw&q=%E3%83%9E%E3%83%8A%E3%83%96%E3%83%AD%E3%82%B0&oq=%E3%83%9E%E3%83%8A%E3%83%96%E3%83%AD%E3%82%B0&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABgxyNoAHACeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwi38caugP3sAhUPG6YKHecSA3gQ4dUDCA0&uact=5"
load_url = "http://www.google.com/search?q=%E3%83%9E%E3%83%8A%E3%83%96%E3%83%AD%E3%82%B0&amp;num=100"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
print(soup)

#特定タグのリストを出力
elems = soup.select('h3')
for elem in elems:
    print(elem)