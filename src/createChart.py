import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

import sqlite3


# データベースファイルのパス
dbpath = 'db/kabu.db'
 
# データベース接続とカーソル生成(データベースファイルがない場合は指定ファイル名で自動作成)
connection = sqlite3.connect(dbpath)
cursor = connection.cursor()
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


#散布図描画init処理
fig = plt.figure()
ax = fig.add_subplot(111, xlabel='xjiku', ylabel='yjiku')

nextStart = 1
nextHigh = 1
for row in cursor:
    #print(str(row[0]) + "," + str(row[1]))
    if nextStart == 1:
        nextStart = row[2]
        nextHigh = row[2]
    print('日付' + str(row[1])
    + '前日終' + str(row[2])
    + '当日始上昇率' + str(int(100.00*nextStart/int(row[2]))-100) 
    + '当日高値上昇率'  + str(int(100.00*nextHigh/int(row[2]))-100)
    + '株価相対位置' + str(int(100.00 *(int(row[2])-int(row[6]))/(int(row[5])-int(row[6])))) )
    nextStart = row[3]
    nextHigh = row[4]

    ax.scatter(int(100.00*nextStart/int(row[2]))-100, int(100.00 *(int(row[2])-int(row[6]))/(int(row[5])-int(row[6]))), c='blue')




# 接続を閉じる
connection.close()


fig.savefig('YahooChart.png')

#plt.show()
#print(mlt.get_cachedir())