import sqlite3

# データベースファイルのパス
dbpath = 'db/kabu.db'
 
# データベース接続とカーソル生成(データベースファイルがない場合は指定ファイル名で自動作成)
connection = sqlite3.connect(dbpath)
cursor = connection.cursor()
 
# エラー処理（例外処理）
try:
    cursor.execute('DELETE FROM Price')

except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])
    
# 保存を実行（忘れると保存されないので注意）
connection.commit()


# 接続を閉じる
connection.close()



