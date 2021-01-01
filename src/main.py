
import google
import csv

#google.GetKeywordResoltList('システム開発 失敗 要件定義')


csv_file = open("90google_list.csv", "r", encoding="utf_8", errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
for row in f:
    #rowはList
    #row[0]で必要な項目を取得することができる
    #print(row[1])
    google.GetPageDetail(row[1])



#ラッコキーワードは、pytestを使っているためmain.pyで実行できない。