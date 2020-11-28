#!/bin/sh

#ファイル削除 -f 存在しない削除処理のエラーが出なくなる
rm -f src.zip

#zip化 -m zip化したファイルを削除、-r 配下のファイルも対象
zip -m -r -e src.zip src