import csv
from playwright.sync_api import Page

import sqlite3

import os
import urllib.parse #エンコード処理
import datetime

csvOutputBasePath = "output/csv_"
htmlOutputBasePath = "output/html_"
logFullPath = "Log.log"

class TestPlanisphere:
    def getPriceData(self, page, stockCode:str):
        hasBodyTR = True
        pageCount = 1

        while hasBodyTR == True:
            url = 'https://info.finance.yahoo.co.jp/history/?code=' + str(stockCode) +'&sy=2020&sm=1&sd=1&ey=2020&em=12&ed=31&tm=d&p=' + str(pageCount)
            writeLOG(url)
            page.goto(url)
            page.waitForLoadState("networkidle")

            # HTMLの保存
            html =  page.content()

            keywordElements = page.querySelectorAll('.boardFin' + '.yjSt' + '.marB6'); #複数クラスのAND条件
    
            f = open(csvOutputBasePath + stockCode + ".csv", 'a')
            for item in keywordElements:
                trs = item.querySelectorAll('tr')
                #writeLOG('TRの件数' + str(len(trs)))
                if len(trs) == 1:
                    hasBodyTR = False
                for tr in trs:
                    if '日付' not in tr.innerHTML(): #テーブルヘッダー行は書き込みをスキップ
                        tds = tr.querySelectorAll('td')
                        tdCount = 0
                        date = ''
                        start = 0
                        high = 0
                        low = 0
                        end = 0
                        volume = 0
                        #writeLOG(str(tr.innerHTML()))
                        for td in tds:
                            if tdCount == 0:
                                #日付
                                date = datetime.datetime.strptime(str(td.innerText()), '%Y年%m月%d日')
                            if tdCount == 1:
                                #始め
                                start = td.innerText().replace(',', '')
                            if tdCount == 2:
                                #高値
                                high = td.innerText().replace(',', '')
                            if tdCount == 3:
                                #安値
                                low = td.innerText().replace(',', '')
                            if tdCount == 4:
                                #終値
                                end = td.innerText().replace(',', '')
                            if tdCount == 5:
                                #出来高
                                volume = td.innerText().replace(',', '')
                            tdCount = tdCount + 1 
                        #レコード記述
                        f.write(str(stockCode) + ',' + date.strftime('%Y%m%d') + ',' + start + ',' + high + ',' + low + ',' + end + ',' + volume + "\n")
            f.close()
            
            pageCount = pageCount + 1

            #f = open(htmlOutputBasePath + stockCode + ".txt", 'a')
            #f.write(html)  
            #f.close()

    def test_reserve_otoku(self, page: Page):
        global stockCode
        #self.getPriceData(page, stockCode)
        
        # データベースファイルのパス
        dbpath = 'db/kabu.db'
        
        # データベース接続とカーソル生成(データベースファイルがない場合は指定ファイル名で自動作成)
        connection = sqlite3.connect(dbpath)
        cursor = connection.cursor()
        cursor.execute('SELECT DISTINCT code ' +
        #'code, name' +
        'FROM base  ')

        for row in cursor:
            self.getPriceData(page, row[0])

        # 接続を閉じる
        connection.close()
        
        
        
        
        
        
        
        
        
        #self.getPriceData(page, '2702')
        #self.getPriceData(page, '7602')
        page.close()

    
def writeLOG(sentence):
    f = open(logFullPath, 'a')
    f.write(sentence + '\n')  
    f.close()