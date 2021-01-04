import csv
import pprint
import sqlite3

import glob #フォルダ内ファイル一覧取得に利用

##########################################################################
#　処理概要：outputフォルダからcsvファイルを取得しDBへ追記
##########################################################################

inputDataPath = "output/"

# データベースファイルのパス
dbpath = 'db/kabu.db'
 
# データベース接続とカーソル生成(データベースファイルがない場合は指定ファイル名で自動作成)
connection = sqlite3.connect(dbpath)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
cursor = connection.cursor()
 
# エラー処理（例外処理）
try:
    files = glob.glob(inputDataPath + "*.csv")
    for file in files:
        with open(file) as f:
            reader = csv.reader(f)
            l = [row for row in reader]
            #print(l)
            #print(l[0][0])
            for row in l:
                cursor.execute("INSERT INTO Price VALUES ('" + row[0] + "','" + row[1] + "'," + row[2] + "," + row[3] + "," + row[4] + "," + row[5] + "," + row[6] + ")")

except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])
 
# 保存を実行（忘れると保存されないので注意）
connection.commit()

cursor.execute('SELECT * FROM Price')
cursor.execute('SELECT p.code' +
',date' +
',end' +
',start' +
',high' +
',yp.yHigh' +
',yp.yLow' +
',0.01' +
',1' +
' ' +
'FROM Price p ' +
'INNER JOIN (SELECT code,max(high) as ''yHigh'',min(low) as ''yLow'' FROM Price WHERE code = ''7602'' AND Date BETWEEN ''20200101'' AND ''20201231'' GROUP BY code) yp ' +
'   ON p.code = yp.code ' +
'WHERE p.code = ''7602'' ORDER BY p.date DESC ')

# 中身を全て取得するfetchall()を使って、printする。
#print(cursor.fetchall())
print("完了")

# 接続を閉じる
connection.close()



