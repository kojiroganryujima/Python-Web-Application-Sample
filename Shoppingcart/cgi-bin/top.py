#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import codecs
import html

import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # UTF-8に

#cgitb.enable() # トレース出力を有効に

form = cgi.FieldStorage()
html = codecs.open('./html/itemlist.html', 'r', 'utf-8').read()

print("")
print(html)