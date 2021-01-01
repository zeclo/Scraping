"""
  Googleの検索結果をCSVファイルに書き込む, 

  Todo:
    なし

"""



from requests_html import HTMLSession
import inspect
import csv
import urllib.parse #エンコード処理

s = 'ダイエット'
s_quote = urllib.parse.quote(s)
url = "https://related-keywords.com/result/suggest?q=%E3%83%80%E3%82%A4%E3%82%A8%E3%83%83%E3%83%88"

# セッション開始
session = HTMLSession()
r = session.get(url)

#r.html.render(sleep=5)
r.html.render()

# == ヘッドレスブラウザで描画されれたHTMLを取得 ==
#print(r.html.raw_html)






#Googleリンク一覧をCSV出力する
def getValue(id,targetURL=""):
    global r 
    print(id)
    if targetURL != "":
        r = session.get(targetURL)
        r.html.render()
    
    print(r.html.find("body")[0].html)

    """
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
                            #print('')
                            with open('90google_list.csv', 'a') as f:
                                writer = csv.writer(f)
                                writer.writerow([str(''.join(item.text.splitlines())), str(item.attrs.get('href'))])
    """
    return

print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
getValue("a")



#price
#yearLow
#volume