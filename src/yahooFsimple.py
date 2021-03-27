import csv
from playwright.sync_api import Page

import sqlite3

import os
import urllib.parse #エンコード処理
import datetime

##########################################################################
#　処理概要：Yahooファイナンスの株価を取得(CSV形式保存)
##########################################################################

##########################################################################
#　実行方法：pytest ファイル名
##########################################################################

csvOutputBasePath = "output/csv_"
htmlOutputBasePath = "output/html_"
logFullPath = "Log.log"
targetCode = "23337" #★★★★取得する証券コードをセット
startDate = "2020/01/01"
endDate = "2021/03/31"

class TestPlanisphere:
    def getPriceData(self, page, stockCode:str):
        hasBodyTR = True
        pageCount = 1

        while hasBodyTR == True:
            # 文字列の切り出しの引数に注意。終端は+1を指定
            dateUrl = '&sy=' + startDate[0:4] + '&sm=' + startDate[5:7] + '&sd=' + startDate[8:10] + '&ey=' + endDate[0:4] + '&em=' + endDate[5:7] + '&ed=' + endDate[8:10] + '&tm=d&p='
            writeLOG('日付条件' + dateUrl )
            url = 'https://info.finance.yahoo.co.jp/history/?code=' + str(stockCode) + dateUrl + str(pageCount)
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
                        #レコード記述 指数を取得する場合は出来高を記述しないコードを使うこと
                        #f.write(str(stockCode) + ',' + date.strftime('%Y%m%d') + ',' + start + ',' + high + ',' + low + ',' + end + ',' + volume + "\n")
                        f.write(str(stockCode) + ',' + date.strftime('%Y%m%d') + ',' + start + ',' + high + ',' + low + ',' + end + "\n")
            f.close()
            
            pageCount = pageCount + 1

            #f = open(htmlOutputBasePath + stockCode + ".txt", 'a')
            #f.write(html)  
            #f.close()

    def test_reserve_otoku(self, page: Page):
        global stockCode
        
        writeLOG('コード' + targetCode + ' データ取得開始')
        self.getPriceData(page, targetCode)

        page.close()

    
def writeLOG(sentence):
    f = open(logFullPath, 'a')
    f.write(sentence + '\n')  
    f.close()