import csv
import pprint
import sqlite3

with open('YahooList.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
#print(l)
#print(l[0][0])


# データベースファイルのパス
dbpath = 'db/kabu.db'
 
# データベース接続とカーソル生成(データベースファイルがない場合は指定ファイル名で自動作成)
connection = sqlite3.connect(dbpath)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
cursor = connection.cursor()
 
# エラー処理（例外処理）
try:
    # CREATE
    cursor.execute("DROP TABLE IF EXISTS Price")
    cursor.execute("CREATE TABLE IF NOT EXISTS Price (Code TEXT, Date DATETIME, Start INTEGER, High INTEGER, Low INTEGER, End INTEGER, Volume INTEGER)")

    for row in l:
        cursor.execute("INSERT INTO Price VALUES ('" + row[0] + "','" + row[1] + "'," + row[2] + "," + row[3] + "," + row[4] + "," + row[5] + "," + row[6] + ")")
    
    
    # INSERT
    #cursor.execute("INSERT INTO sample VALUES (1, '佐藤')")
    
    # プレースホルダの使用例
    # プレースホルダには疑問符(qmark スタイル)と名前(named スタイル)の2つの方法がある
    # 1つの場合には最後に , がないとエラー。('鈴木') ではなく ('鈴木',)
    #cursor.execute("INSERT INTO sample VALUES (2, ?)", ('鈴木',))
    #cursor.execute("INSERT INTO sample VALUES (?, ?)", (3, '高橋'))
    #cursor.execute("INSERT INTO sample VALUES (:id, :name)",
    #               {'id': 4, 'name': '田中'})
    # 複数レコードを一度に挿入 executemany メソッドを使用
    #persons = [
    #    (5, '伊藤'),
    #    (6, '渡辺'),
    #]
    #cursor.executemany("INSERT INTO sample VALUES (?, ?)", persons)
    # わざと主キー重複エラーを起こして例外を発生させてみる
    #cursor.execute("INSERT INTO sample VALUES (1, '中村')")


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
'WHERE p.code = ''7602''')

# 中身を全て取得するfetchall()を使って、printする。
print(cursor.fetchall())

# 接続を閉じる
connection.close()



