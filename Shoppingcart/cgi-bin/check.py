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
import user_record
import datetime

from pathlib import Path


################################################################################
################################################################################
###前処理
###ディレクトリ取得
current_directly = os.getcwd()
###時刻設定
time = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
###ユーザの入力情報格納箇所
path_all = './user_record/'


################################################################################
################################################################################
###HTML(画面表示項目)
html_body = """
<!DOCTYPE html>
<html>
<meta charset="UTF-8">
<head>
<title>送付先確認</title>
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
ret = form.getlist('address')


################################################################################
################################################################################
###時刻(のちに注文IDとなる)と、住所、宛名、E-mailの記録機能を実行
###時刻-time
te = user_record.user_record()
time_file = time + "time"
te.set_contents(current_directly, path_all, time_file, "", ret[0])

###送付先(郵便番号)-postal code
postal_file = time + "postal_code"
te.set_contents(current_directly, path_all, postal_file, ret[1], "")

###送付先(住所)-address
address_file = time + "address"
te.set_contents(current_directly, path_all, address_file, ret[2], "")

###お名前(宛名)
name_file = time + "name"
te.set_contents(current_directly, path_all, name_file, ret[3], "")

###E-mail
email_file = time + "e-mail"
#te.set_contents(current_directly, path_all, email_file, ret[4], "")


################################################################################
###前の画面で入力された項目の読み込み
os.chdir(current_directly)
os.chdir(path_all)


################################################################################
###金額の読み込み
price_file = "price"
price = ""

with open(price_file) as f:
    price = f.read()


################################################################################
###購入内容の確認
print(html_body % ("■送付先・購入品・金額をお確かめ頂き、問題なければ「購入」ボタンを押してください"))
print(html_body % ("■内容に誤りがある場合は、お手数ですがブラウザの戻るボタンで前の画面に戻って再度操作願います。"))
print(html_body % ('</br>'))


################################################################################
###送付先確認
print(html_body % ("■送付先"))
print(html_body % (ret[0]))
print(html_body % (ret[1]))
print(html_body % (ret[2]))
print(html_body % (ret[3]))
print(html_body % ('</br>'))

################################################################################
###購入品確認
print(html_body % ("■購入品"))

###購入品の読み込み
item_file = "music"

count = 0
with open(item_file) as f:
    for line in f:
        count += 1

#item_list_tmp = [count]

f = open(item_file, 'r')

#for i in range(count):
item_list_tmp = f.readlines()
print(item_list_tmp)

f.close()

#print(html_body % (line))
print(html_body % ('</br>'))

################################################################################
###金額確認
print(html_body % ("■金額(円)"))
print(html_body % (price))
print(html_body % ("円"))
print(html_body % ('</br>'))

################################################################################
###仮注文票作成
tmp_order_name = str(time)
Path(tmp_order_name).touch()


#注文票へ書き込み
f = open(tmp_order_name, "a")

f.write(str(item_list_tmp))
f.write('\n')

#金額
f.write(price)
f.write('\n')

#送付先・お名前・E-mail
count_items = len(ret)
for i in range(count_items):
    f.write(ret[i])
    f.write('\n')
f.close()

#問題なければ送付先リストのテキスト化とお礼画面
print(html_body % ("■注文IDのチェックは入れたままで「購入」を押してください"))
print(html_body % ("注文ID："))
print(html_body % ('<form action="thank_you.py" method="POST">'))
print(html_body % ('<input type="checkbox" name="order_id" value=' + time + ' checked="checked">' + time + '</br>'))
print(html_body % ('<input type="submit" value="購入"></br>'))
print(html_body % ('</form>'))