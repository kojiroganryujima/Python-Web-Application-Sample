#!/usr/bin/python3
# -*- coding: utf-8 -*-

################################################################################
###インポート
import cgi
import codecs
import html

import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # UTF-8に
#cgitb.enable() # トレース出力を有効に

import os
import shutil

################################################################################
###ディレクトリ取得
current_directly = os.getcwd()


################################################################################
###ユーザの入力情報格納箇所
path_all = './user_record/'


################################################################################
###注文票(確定版))格納箇所
path_order = './order/'


################################################################################
###HTML(画面表示項目)
html_body = """
<!DOCTYPE html>
<html>
<meta charset="UTF-8">
<head>
<title>購入ありがとうございました-Thank You！！</title>
<style>
h1 {
font-size: 3em;
}
</style>
</head>
<body>
<h4>%s</h4>

</body>
</html>
"""

################################################################################
###cgiのおまじない(画面から入力された情報をプログラム内で扱えるようにする)
form = cgi.FieldStorage()
ret = form.getlist('order_id')


################################################################################
###注文票確定処理
os.chdir(current_directly)

tmp_order_path = path_all + ret[0]
order_path = path_order + ret[0]

shutil.copyfile(tmp_order_path, order_path)


################################################################################
###お礼-Thank You
print(html_body % ("購入ありがとうございました-Thank You！！"))
print(html_body % ("こちらの振込先に代金を振り込んで頂け次第、商品を発送致します。"))
print(html_body % ("■振込先"))
print(html_body % ("銀行名：XXXXXX"))
print(html_body % ("口座：普通"))
print(html_body % ("口座番号：XXXXXX"))
print(html_body % ("口座名義：XXXXXX"))