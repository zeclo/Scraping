import sqlite3
import csv
import pprint

# データベースファイルのパス
dbpath = 'db/kabu.db'
 
# データベース接続とカーソル生成(データベースファイルがない場合は指定ファイル名で自動作成)
connection = sqlite3.connect(dbpath)
cursor = connection.cursor()
 
# エラー処理（例外処理）
try:
    if False:
        # CREATE
        cursor.execute("CREATE TABLE IF NOT EXISTS "
        + "base ("                  #銘柄基本テーブル(銘柄基本情報。コードと更新日でユニークになる)
        + "Code TEXT, "             #銘柄コード
        + "Name TEXT, "             #銘柄名
        + "TosanRatio INTEGER, "    #倒産指数(はっしゃんさんサイト参照)
        + "UpdateDate DATETIME "    #更新日
        + ")")
    else:
        with open('test.csv') as f:
            reader = csv.reader(f)
            l = [row for row in reader]
        print('csv読取完了')
        print(l)
        for row in l:
            cursor.execute("INSERT INTO base VALUES ( " 
            + "'" + row[0] + "'," 
            + "'" +row[1] + "'," 
            + row[2] + "," 
            + "'" +row[3] + "'" 
            + ")")
        

except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])

# 保存を実行（忘れると保存されないので注意）
connection.commit()

cursor.execute('SELECT * FROM base')

# 中身を全て取得するfetchall()を使って、printする。
print(cursor.fetchall())

# 接続を閉じる
connection.close()



