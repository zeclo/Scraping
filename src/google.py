"""
  Googleの検索結果をCSVファイルに書き込む, 

  Todo:
    なし

"""

from requests_html import HTMLSession
import inspect
import csv
import urllib.parse #エンコード処理


session = HTMLSession()
r = None




def GetKeywordResoltList(keyword):
    s_quote = urllib.parse.quote(keyword)
    url = "http://www.google.com/search?q=" + s_quote

    # セッション開始
    global r 
    r = session.get(url)

    #r.html.render(sleep=5)
    r.html.render()

    # == ヘッドレスブラウザで描画されれたHTMLを取得 ==
    #print(r.html.raw_html)

    #2ページ目、3ページ目のURLを取得
    baseurl = "https://www.google.com"
    page2 = ""
    page3 = ""

    targetElement = r.html.find("a")
    if targetElement:
        for item in targetElement:
            if item.attrs.get('aria-label') == "Page 2": #.get('aria-label')は辞書データの取得
                page2 = baseurl +item.attrs.get('href')
            if item.attrs.get('aria-label') == "Page 3":
                page3 = baseurl +item.attrs.get('href')

    print(page2)
    print(page3)

    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    __GetListAndWriteToCSV("a")
    print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
    __GetListAndWriteToCSV("a",page2)
    print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
    __GetListAndWriteToCSV("a",page3)

#Googleリンク一覧をCSV出力する
def __GetListAndWriteToCSV(id,targetURL=""):
    writeCSVFullPath = '90google_list.csv'
    global r 
    print(id)
    if targetURL != "":
        r = session.get(targetURL)
        r.html.render()
    targetElement = r.html.find(id)
    if targetElement:
        #対象要素がページに１つなら配列を直指定
        #print(targetElement[0].text)
        #複数ならループ処理
        for item in targetElement:
            keyword = ""
            if item.attrs.get('href') != "None":
                keyword =str(item.attrs.get('href'))
            if 'google' not in keyword: #指定文字列の存在を確認
                if '/search?' not in keyword:
                        if len(keyword) > 20: #短いURLはGoogle側の飾りと考え除外
                            #Todo hint aタグ→h3タグを検索してみると絞れると思う
                            #print(item.text)
                            with open(writeCSVFullPath, 'a') as f:
                                writer = csv.writer(f)
                                writer.writerow([str(''.join(item.text.splitlines())), str(item.attrs.get('href'))])
    return



def GetPageDetail(url):
    # セッション開始
    global r
    r = session.get(url)

    #r.html.render(sleep=5)
    r.html.render()

    # == ヘッドレスブラウザで描画されれたHTMLを取得 ==
    #print(r.html.raw_html)

    print('取得★★★★★★★★★★★★★★★★★★★★★★★★★★')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    __GetDetailAndWriteToCSV("a")



#Googleリンク一覧をCSV出力する
def __GetDetailAndWriteToCSV(id,targetURL=""):
    writeCSVFullPath = '91pageDetail.csv'
    global r 
    print(id)
    if targetURL != "":
        r = session.get(targetURL)
        r.html.render()
    targetElement = r.html.find("title,h1,h2,h3,h4,h5,p")
    if targetElement:
        #対象要素がページに１つなら配列を直指定
        #print(targetElement[0].text)
        #複数ならループ処理
        for item in targetElement:
            insertSpace = ""
            if item.tag == "title":
                insertSpace = ""
            elif item.tag == "h1":
                insertSpace = "  "
            elif item.tag == "h2":
                insertSpace = "    "
            elif item.tag == "h3":
                insertSpace = "      "
            elif item.tag == "h4":
                insertSpace = "        "
            elif item.tag == "h5":
                insertSpace = "          "
            elif item.tag == "p":
                insertSpace = "            "
            else:
                insertSpace = ""
            
            with open(writeCSVFullPath, 'a') as f:
                writer = csv.writer(f)
                writer.writerow([str(item.tag),insertSpace + str(''.join(item.text.splitlines()))]) #, str(''.join(item.html.splitlines()))])
        return

