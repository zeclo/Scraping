from requests_html import HTMLSession
import inspect
import re

url = "https://minkabu.jp/news/search?category=market&page=1&q=%E5%80%A4%E4%B8%8A%E3%81%8C%E3%82%8A%E5%80%A4%E4%B8%8B%E3%81%8C%E3%82%8A%E9%8A%98%E6%9F%84%E6%95%B0"

#11時のニュースURL
urlAt11 = ''
#1時のニュースURL
urlAt01 = ''
#2時のニュースURL
urlAt02 = ''



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
        #print(targetElement[0].text)
        #複数ならループ処理
        for item in targetElement:
            if '今日' in item.text:
                if '午前１１時現在' in item.text:
                    abc = item.find("a")
                    global urlAt11 
                    urlAt11 = 'https://minkabu.jp' + abc[0].attrs['href']
                if '午後１時現在' in item.text:
                    abc = item.find("a")
                    global urlAt01 
                    urlAt01 = 'https://minkabu.jp' + abc[0].attrs['href']
                if '午後２時現在' in item.text:
                    abc = item.find("a")
                    global urlAt02
                    urlAt02 = 'https://minkabu.jp' + abc[0].attrs['href']
    return


def getNewsDetail(url):
    global session
    r = session.get(url)
    r.html.render()
    
    targetElement = r.html.find('.md_box.fsize_m.md_normalize')
    if targetElement:
 
        #print(targetElement[0].text.splitlines()[0])

        #置換パターンの設定
        trans_table = str.maketrans({"０":"0", "１":"1", "２":"2", "３":"3", "４":"4", "５":"5", "６":"6", "７":"7", "８":"8", "９":"9"})

        raw_abc = r'値上がり銘柄数は[０１２３４５６７８９]+'
        matchobj = re.search(raw_abc, targetElement[0].text)
        print(matchobj.group().replace('値上がり銘柄数は', '').translate(trans_table))

        raw_abc = r'値下がり銘柄数は[０１２３４５６７８９]+'
        matchobj = re.search(raw_abc, targetElement[0].text)
        print(matchobj.group().replace('値下がり銘柄数は', '').translate(trans_table))

        raw_abc = r'変わらずは[０１２３４５６７８９]+'
        matchobj = re.search(raw_abc, targetElement[0].text)
        print(matchobj.group().replace('変わらずは', '').translate(trans_table))

        #複数ならループ処理
        #for item in targetElement:
        #    print(item.text)
    return

getValue(".cell")

print(urlAt11)
print(urlAt01)
print(urlAt02)
#(☆_☆) 70%→79%→89% 騰落率レポ
# ニュース記事を出す 

getNewsDetail(urlAt11)