#! /usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import codecs
import os
URL="http://api.openweathermap.org/data/2.5/weather?q=Sapporo,jp"
data = urllib2.urlopen(URL)
j = json.load(data)
print j
description= j["weather"][0]['description']
temp= (float(j["main"]["temp"]))-273.15

#
##本日の天気予報を取得 備考:[0]:本日取得[1]:明日
#
#result[unicode("☁ ",'utf-8')]=weatherinfo.find('曇')
#result[unicode("☀ ",'utf-8')]=weatherinfo.find('晴')
#result[unicode(" | ",'utf-8')]=weatherinfo.find('時々') 
#result[unicode("->",'utf-8')]=weatherinfo.find('後')
#result[unicode("☃ ",'utf-8')]=weatherinfo.find('雪')
#result[unicode("☂ ",'utf-8')]=weatherinfo.find('雨')
#result[unicode("or",'utf-8')]=weatherinfo.find('か')

f=codecs.open('weatherpy.cache','w','utf-8')
output=description+":"+str(temp)+u"℃"
f.write(output)
f.close()
os.system("cat weatherpy.cache")

