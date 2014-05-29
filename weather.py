# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import os
import codecs


URL = "http://www.jma.go.jp/jp/yoho/306.html"
html = ""
with urllib.request.urlopen(URL) as url:
    html = url.read()

soup = BeautifulSoup(html)

data = soup('th', {'class': 'weather'})[0]
weatherinfo = data('img')[0].get('title')
result = {}
result["☁ "] = weatherinfo.find('曇')
result["☀ "] = weatherinfo.find('晴')
result[" | "] = weatherinfo.find('時々')
result["->"] = weatherinfo.find('後')
result["☃ "] = weatherinfo.find('雪')
result["☂ "] = weatherinfo.find('雨')
result["or"] = weatherinfo.find('か')

f = codecs.open('weatherpy.cache', 'w', 'utf-8')
f.write(u'札')
for data, num in sorted(result.items(), key=lambda x: x[1]):
    if -1 != num:
        f.write(data)
f.close()
os.system("cat weatherpy.cache")
