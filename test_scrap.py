# -*- coding: utf-8 -*-
import urllib2
import json

# все лишнее убрал оставил только рабочее состояние захвата страницы

url = 'https://ls.sportradar.com/ls/feeds/?/itf/en/Europe:Berlin/gismo/client_dayinfo/20170628'
respone = urllib2.urlopen(url)
page = respone.read()
data =json.loads(page)
# тут была попытка циклом захватывать все матчи но так как json постоянно меняется попытка не удалась поэтому в ручном режиме вытащил один матч
print data['doc'][0]['data']['matches']['11887608']['param5']