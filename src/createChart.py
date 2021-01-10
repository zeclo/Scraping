import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Noto Sans CJK JP'#'IPAexGothic'

import sqlite3

##########################################################################
#　処理概要：DBデータから散布図ファイルを作成
##########################################################################

dbpath = 'db/kabu.db'
pngFullPath = "output/chart_"


def createPngfile(stockCode:str, stockName:str):
    # データベース接続とカーソル生成(データベースファイルがない場合は指定ファイル名で自動作成)
    connection = sqlite3.connect(dbpath)
    cursor = connection.cursor()
    cursor.execute('SELECT DISTINCT p.code' +
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
    "INNER JOIN (SELECT code,max(high) as 'yHigh', min(low) as 'yLow' FROM Price WHERE code = '" + stockCode + "' AND Date BETWEEN '20200101' AND '20201231' GROUP BY code) yp " +
    '   ON p.code = yp.code ' +
    "WHERE p.code = '" + stockCode + "' ORDER BY p.date DESC ")


    #散布図描画init処理
    fig = plt.figure()
    ax = fig.add_subplot(111, xlabel='x上昇率', ylabel='y相対株価')
    #散布図にタイトルを設定
    ax.set_title("" + stockCode +": "+ stockName, loc='center')

    nextStart = 1
    nextHigh = 1
    breakCounter = 0
    protCounter = 0
    for row in cursor:
        #print(str(row[0]) + "," + str(row[1]))
        if nextStart == 1:
            nextStart = row[2]
            nextHigh = row[2]
        #print('日付' + str(row[1])
        #+ '前日終' + str(row[2])
        #+ '当日始上昇率' + str(int(100.00*nextStart/int(row[2]))-100) 
        #+ '当日高値上昇率'  + str(int(100.00*nextHigh/int(row[2]))-100)
        #+ '株価相対位置' + str(int(100.00 *(int(row[2])-int(row[6]))/(int(row[5])-int(row[6])))) )
        
        x = int(100.00*nextHigh/int(row[2]))-100
        y = int(100.00 *(int(row[2])-int(row[6]))/(int(row[5])-int(row[6])))
        
        nextStart = row[3]
        nextHigh = row[4]
        protClolr = 'blue'
        
        if x > 5:
            #print(breakCounter)
            if breakCounter > 10:
                protClolr = 'green'
            if breakCounter > 20:
                protClolr = 'yellow'
            if breakCounter > 30:
                protClolr = 'red'
            breakCounter = 0
        
        if x < -5:
            #print(breakCounter)
            if breakCounter > 10:
                protClolr = 'green'
            if breakCounter > 20:
                protClolr = 'yellow'
            if breakCounter > 30:
                protClolr = 'red'
            breakCounter = 0
        
        if protCounter == 0:
            ax.scatter(x, y,s=100, c='red', marker='*')
        else:
            if protClolr != 'blue':
                ax.scatter(x, y,s=50, c=protClolr)
            else:
                ax.scatter(x, y, s=10, c=protClolr)
        breakCounter = breakCounter + 1
        protCounter = protCounter + 1

    # 接続を閉じる
    connection.close()

    fig.savefig(pngFullPath + stockCode + ".png")
    #plt.show()
    #print(mlt.get_cachedir())
    plt.close()



# データベース接続とカーソル生成(データベースファイルがない場合は指定ファイル名で自動作成)
connection2 = sqlite3.connect(dbpath)
cursor2 = connection2.cursor()
cursor2.execute('SELECT DISTINCT code, name ' +
'FROM base  ')

for row in cursor2:
    createPngfile(row[0], row[1])

# 接続を閉じる
connection2.close()
        