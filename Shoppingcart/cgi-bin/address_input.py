#!/usr/bin/python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
###インポート
import cgi
import codecs
import html

import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # UTF-8に
#cgitb.enable() # トレース出力を有効に

import os
import os.path
import user_record
import datetime
import shutil


################################################################################
################################################################################
###前処理
###ユーザの入力情報格納箇所
path_all = './user_record/'
###ディレクトリ取得
current_directly = os.getcwd()


################################################################################
###HTML(画面表示項目)
html_body = """
<!DOCTYPE html>
<html>
<meta charset="UTF-8">
<head>
<title>受信したデータを表示</title>
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
################################################################################
###cgiのおまじない(画面から入力された情報をプログラム内で扱えるようにする)
form = cgi.FieldStorage()
ret = form.getlist('chkbox')


################################################################################
################################################################################
###ユーザが購入揮毫している商品の確認&金額の計算
#購入品確認
print(html_body % ('◆あなたの購入希望品-What you want is …'))

#金額を一旦¥0にセット
price = 0

#金額計算
count_items = len(ret)
for i in range(count_items):
    print(html_body % (ret[i]))

    if ret[i] == "空も飛べるはず":
        price = price + 1000
    
    if ret[i] == "ロビンソン":
        price = price + 500

    if ret[i] == "チェリー":
        price = price + 100


#金額を表示
print(html_body % ('</br>'))
print(html_body % ('◆合計金額(円)-Total price(¥) is …'))
print(html_body % (price))


################################################################################
################################################################################
###購入リスト、金額のを記録機能を実行

###購入リストを記録機能を実行
shutil.rmtree('user_record')
os.mkdir('user_record')

te = user_record.user_record()
for i in range(count_items):
    i = i - 1
    item_file = "music"
    te.set_contents(current_directly, path_all, item_file, ret[i],"")
    #print(html_body % (ret[i]))

###金額記録機能を実行
price_file = "price"
te.set_contents(current_directly, path_all, price_file, "", price)


################################################################################
################################################################################
###住所情報入力画面
print(html_body % ('</br>'))
print(html_body % ('</br>'))
print(html_body % ("◆送付先住所を入力ください↓↓↓"))
print(html_body % ('<form action="check.py" method="POST">'))
print(html_body % ("郵便番号　："'<input type="text" name="address" value=""></br>'))
print(html_body % ("住所　　　："'<input type="text" name="address" value=""></br>'))
print(html_body % ("送付先宛名："'<input type="text" name="address" value=""></br>'))
print(html_body % ("E-mail　　："'<input type="text" name="address" value=""></br>'))
print(html_body % ('</br>'))
print(html_body % ('<input type="submit" value="確認画面へ"></br>'))
print(html_body % ('</form>'))