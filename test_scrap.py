
# -*- coding: utf-8 -*-
##import urllib2

import json

def matchstatus_live(p1,p2):
    print(p1, ' ', p2)
    return 'ok'

from urllib.request import urlopen
html = urlopen("https://ls.sportradar.com/ls/feeds/?/itf/en/Europe:Berlin/gismo/client_dayinfo/20170628")
#print(html)

page = html.read()
data =json.loads(page)

#print(data)
print (data['doc'][0]['data']['matches']['11887608']['param5'])
print('=========')

my_list = data['doc'][0]['data']['matches']
for elm in my_list:
    matchstatus = data['doc'][0]['data']['matches'][elm]['match']['matchstatus']
    if matchstatus == 'live':
        matchstatus_live(elm, matchstatus)

#print (data['doc'][0]['data']['matches'])

#from urllib.request import urlopen
#url = urlopen(url = 'https://ls.sportradar.com/ls/feeds/?/itf/en/Europe:Berlin/gismo/client_dayinfo/20170628')
#print(url)

#import json

## все лишнее убрал оставил только рабочее состояние захвата страницы
## тут у меня была переменная даты проведения турнира которую я вставлял в самом конце
## потом шел цикл изменения даты и сверка с системным временем
##url = 'https://ls.sportradar.com/ls/feeds/?/itf/en/Europe:Berlin/gismo/client_dayinfo/20170628'

#respone = urllib2.urlopen(url)
#page = respone.read()
#data =json.loads(page)
## тут была попытка циклом захватывать все матчи но так как json постоянно меняется попытка не удалась поэтому в ручном режиме вытащил один матч
#print data['doc'][0]['data']['matches']['11887608']['param5']
