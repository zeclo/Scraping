import sqlite3
import csv
import pprint

# データベースファイルのパス
dbpath = 'db/kabu.db'
 
# データベース接続とカーソル生成(データベースファイルがない場合は指定ファイル名で自動作成)
connection = sqlite3.connect(dbpath)
cursor = connection.cursor()

cursor.execute('SELECT * FROM base')

# 中身を全て取得するfetchall()を使って、printする。
print(cursor.fetchall())

# 接続を閉じる
connection.close()



