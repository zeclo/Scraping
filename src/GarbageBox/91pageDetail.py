"""
  指定URLの指定タグ情報をCSVファイルに書き込む, 

  Todo:
    なし

"""

from requests_html import HTMLSession
import inspect
import csv
import urllib.parse #エンコード処理

url = "https://housefoods-group.com/activity/e-mag/magazine/74.html"

session = HTMLSession()
r = None




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


GetPageDetail(url)