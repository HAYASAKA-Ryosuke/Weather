#! /usr/bin/python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2
import sys
import codecs
import commands
import os
URL="http://www.jma.go.jp/jp/yoho/306.html"

html = urllib2.urlopen(URL).read()
soup = BeautifulSoup(html)

#本日の天気予報を取得 備考:[0]:本日取得[1]:明日
data= soup('th',{'class':'weather'})[0]
weatherinfo="".encode('utf-8')
weatherinfo=data('img')[0].get('title').encode('utf-8')
result={}
#if(0!=weatherinfo.find('曇')):
result[unicode("☁ ",'utf-8')]=weatherinfo.find('曇')
result[unicode("☀ ",'utf-8')]=weatherinfo.find('晴')
result[unicode(" | ",'utf-8')]=weatherinfo.find('時々') 
result[unicode("->",'utf-8')]=weatherinfo.find('後')
result[unicode("☃ ",'utf-8')]=weatherinfo.find('雪')
result[unicode("☂ ",'utf-8')]=weatherinfo.find('雨')

#print weatherinfo
#print info('img')[0].get('title')

f=codecs.open('weatherpy.cache','w','utf-8')
output=""
for data,num in sorted(result.items(),key=lambda x:x[1]):
    if(-1!=num):
        f.write(data)
#print output
#f.write(unicode(output,'utf-8'))
f.close()
os.system("cat ~/Documents/PythonWorks/weatherpy.cache")

