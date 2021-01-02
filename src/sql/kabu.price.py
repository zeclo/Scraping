import sqlite3

# データベースファイルのパス
dbpath = 'db/kabu.db'
 
# データベース接続とカーソル生成(データベースファイルがない場合は指定ファイル名で自動作成)
connection = sqlite3.connect(dbpath)
cursor = connection.cursor()
 
# エラー処理（例外処理）
try:
    if True:
        # CREATE
        cursor.execute("CREATE TABLE IF NOT EXISTS "
        + "Price ( "        #株価テーブル
        + "Code TEXT, "     #銘柄コード
        + "Date DATETIME, " #日付 
        + "Start INTEGER, " #始値
        + "High INTEGER, "  #高値 
        + "Low INTEGER, "   #安値 
        + "End INTEGER, "   #終値 
        + "Volume INTEGER"  #出来高 
        + ")")

except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])
    
# 保存を実行（忘れると保存されないので注意）
connection.commit()

cursor.execute('SELECT * FROM Price')

# 中身を全て取得するfetchall()を使って、printする。
print(cursor.fetchall())

# 接続を閉じる
connection.close()



