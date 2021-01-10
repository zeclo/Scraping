import csv
import pprint

import glob #フォルダ内ファイル一覧取得に利用

##########################################################################
#　処理概要：散布図ファイルを読み込んでaOutut.htmlを生成
##########################################################################

inputDataPath = "output/"
targetFileFullName = "output/aOutput.html"
outputPart1FullName = "src/aOutput.html.partial1"
outputPart2FullName = "src/aOutput.html.partial2"

f = open(targetFileFullName, 'w')
f.write('')
f.close()

f = open(targetFileFullName, 'a')
f2 = open(outputPart1FullName, 'r')
while True:
  line = f2.readline()
  if line:
    #print(row_no, ":", line)
    f.write(line)  
  else:
    break
f2.close()
f.close()

# エラー処理（例外処理）
try:
    files = glob.glob(inputDataPath + "*.png")
    for fileFullName in files:
        stockCode = fileFullName.replace("output/chart_","").replace(".png","")
        code = "        { name: '" + stockCode + "', checked: false },"
        print(code)
        f = open(targetFileFullName, 'a')
        f.write(code + '\n')  
        f.close()

except Error as e:
    print('sqlite3.Error occurred:', e.args[0])

f = open(targetFileFullName, 'a')
f2 = open(outputPart2FullName, 'r')
while True:
  line = f2.readline()
  if line:
    #print(row_no, ":", line)
    f.write(line)  
  else:
    break
f2.close()
f.close()

print("完了")


