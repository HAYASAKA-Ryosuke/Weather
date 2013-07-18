#! /usr/local/bin/python
# -*- coding: utf-8 -*-

#湿度も取得して温度と交互に表示する
import urllib2
import json
import codecs
import os
def writecache(output):
    f=codecs.open('/Users/hayasaka/weatherpy.cache','w','utf-8')
    f.write(output)
    f.close()
    
def readcache():
    f=codecs.open('/Users/hayasaka/weatherpy.cache','r','utf-8')
    cachedata=f.readline()
    f.close()
    if(u"％" in cachedata):
        return description+":"+str(temp)+u'℃'
    else:
        return description+":"+str(humidity)+u'％'

try:
    URL="http://api.openweathermap.org/data/2.5/weather?q=Sapporo,jp"
    data = urllib2.urlopen(URL)
    j = json.load(data)
    description= j["weather"][0]['description']
    temp= (float(j["main"]["temp"]))-273.15
    #writecache(str(description)+':'+str(temp))
    humidity= (float(j["main"]["humidity"]))
    output=readcache()
    writecache(output)
    os.system("cat /Users/hayasaka/weatherpy.cache")
except:
    print "error"
