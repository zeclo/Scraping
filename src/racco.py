import csv
from playwright.sync_api import Page

import os
import urllib.parse #エンコード処理


keyword = 'システム開発 失敗'

class TestPlanisphere:
    def test_reserve_otoku(self, page: Page):
        s_quote = urllib.parse.quote(keyword)
        url = "https://related-keywords.com/result/suggest?q=" + s_quote
        page.goto(url)
        page.waitForLoadState("networkidle")

        #page.click('text="CSVダウンロード"');
        #page.$()

        with page.expect_download() as download_info:
            page.click('text="CSVダウンロード"')
            #page.click('//*[@id="root"]/div[2]/main/div/div[2]/div[1]/div[3]/div/button[2]')
        download = download_info.value
        #download.saveAs()
        
        #path = download.path()

        #CSVファイルダウンロードデータの書き込み
        #with open('abc.csv', 'w') as f:
        #    writer = csv.writer(f)
        #    writer.writerow([download.url, 1, 2])
        #    writer.writerow(['a', 'b', 'c'])
        

        #page.keyboard.press('Control+A');
        page.screenshot(path="RaccoKeywordList.png")  # スクリーンショット撮影

        # HTMLの保存
        html =  page.content();
        #fs.writeFileSync("page1.html", html);

        #page.$('css=div');
        keywordElements = page.querySelectorAll('.tgzl94-0'+'.sc-1p6awuf-4'); #複数クラスのAND条件
        #print(keywordElements.count);
 
 
        path = 'RaccoKeywordList.txt'
        f = open(path, 'w')
        for item in keywordElements:
            if keyword in item.innerHTML(): #キーワードが入っていない行を削除
                f.write(item.innerHTML() + "\n")  
        f.close()


        path = 'RaccoKeywordRowData.txt'
        f = open(path, 'w')
        f.write(html)  
        f.close()

        page.close()