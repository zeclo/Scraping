from requests_html import HTMLSession
import inspect

url = "https://search.yahoo.co.jp/realtime"
url = "https://jp.kabumap.com/servlets/kabumap/Action?SRC=basic/top/base&codetext=7777"

# セッション開始
session = HTMLSession()
r = session.get(url)

#r.html.render(sleep=5)
r.html.render()

# == ヘッドレスブラウザで描画されれたHTMLを取得 ==
#print(r.html.raw_html)

def getValue(id):
    print(id)
    targetElement = r.html.find(id)
    if targetElement:
        #対象要素がページに１つなら配列を直指定
        print(targetElement[0].text)
        #複数ならループ処理
        for item in targetElement:
            print(item.text)
    return

getValue("#yearHigh")
getValue("#price")
getValue("#yearLow")
getValue("#volume")


#price
#yearLow
#volume