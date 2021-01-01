import csv
from playwright.sync_api import Page

import os
import urllib.parse #エンコード処理


pageCount = 1
hasBodyTR = True


class TestPlanisphere:
    def test_reserve_otoku(self, page: Page):
        global hasBodyTR
        global pageCount

        while hasBodyTR == True:
            url = 'https://info.finance.yahoo.co.jp/history/?code=9983.T&sy=2020&sm=10&sd=5&ey=2020&em=12&ed=3&tm=d&p=' + str(pageCount)
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
                for tr in trs:
                    if '日付' not in tr.innerHTML(): #テーブルヘッダー行は書き込みスキップ
                        f.write(tr.innerHTML() + "\n")
                        bodyCount = bodyCount + 1
            f.close()
            
            if bodyCount == 0:  
                break
            
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