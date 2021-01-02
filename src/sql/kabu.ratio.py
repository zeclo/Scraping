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
        + "ratio ("             #指標テーブル(日別騰落率を保管)
        + "Date DATETIME, "     #日付
        + "Timerange INTEGER, " #時間帯(ex. 11時代、13時代、14時代)
        + "HighCount INTEGER, " #上昇銘柄数
        + "LowCount INTEGER, "  #下降銘柄数
        + "StayCount INTEGER, " #株価変わらず銘柄数
        + "ratio DECIMAL "      #騰落率(計算の上保持)
        + ")")

except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])

# 保存を実行（忘れると保存されないので注意）
connection.commit()

cursor.execute('SELECT * FROM ratio')

# 中身を全て取得するfetchall()を使って、printする。
print(cursor.fetchall())

# 接続を閉じる
connection.close()



