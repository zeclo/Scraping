import csv
from playwright.sync_api import Page

import os
import urllib.parse #エンコード処理
import datetime


pageCount = 1
hasBodyTR = True
stockCode = 7602


class TestPlanisphere:
    def test_reserve_otoku(self, page: Page):
        global hasBodyTR
        global pageCount

        while hasBodyTR == True:
            url = 'https://info.finance.yahoo.co.jp/history/?code=' + str(stockCode) +'&sy=2020&sm=10&sd=5&ey=2020&em=12&ed=3&tm=d&p=' + str(pageCount)
            writeLOG(url)
            page.goto(url)
            page.waitForLoadState("networkidle")

            # HTMLの保存
            html =  page.content()

            keywordElements = page.querySelectorAll('.boardFin' + '.yjSt' + '.marB6'); #複数クラスのAND条件
    
            path = 'YahooList.txt'
            bodyCount = 0
            f = open(path, 'a')
            for item in keywordElements:
                trs = item.querySelectorAll('tr')
                #writeLOG('TRの件数' + str(len(trs)))
                if len(trs) == 1:
                    hasBodyTR = False
                for tr in trs:
                    if '日付' not in tr.innerHTML(): #テーブルヘッダー行は書き込みスキップ
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
                                #writeLOG(str(td.innerHTML()))
                                #date = int(datetime.datetime.strptime(str(td.innerText()).replace('年', '-').replace('月', '-').replace('日', ''), '%Y-%m-%d'))
                            
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

                        
                        
                bodyCount = bodyCount + 1
            f.close()
            
            pageCount = pageCount + 1

            path = 'YahooListRowData.txt'
            f = open(path, 'a')
            f.write(html)  
            f.close()

        page.close()
    
def writeLOG(sentence):
    path = 'Log.log'
    f = open(path, 'a')
    f.write(sentence + '\n')  
    f.close()