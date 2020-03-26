#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

#購入リストを記録機能-consumelist record
class user_record():
    
    #コンストラクタ-constructor
    def __init__(self):
        print('')  #実行したモジュール名を表示する
    

    #ユーザの入力内容を表示項目として出力　ー　record and exprt to the file what user enter
    def set_contents(self, current_directly, path_w, file, contents, num):

        os.chdir(current_directly)
        os.chdir(path_w)
  
        s = contents + "\n"

        if not contents:
            s = str(num)

        f = open(file, "a")
        f.write(s)
        f.close()


    #ユーザの入力内容を読み込み　ー　read what user enter
    def get_contents(self, current_directly, path_w, file):

        os.chdir(current_directly)
        os.chdir(path_w)
  
        i = 0

        with open(file) as f:
            for s_line in f:
                list[i] = s_line
                i = i + 1
        
        return list