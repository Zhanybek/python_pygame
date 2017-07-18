import datetime
from time import strftime

import requests
import json

def matchstatus_live(p1, p2, p3):
    jdatal = {}
    jdatal['id'] = p1
    jdatal['param5'] = p3['param5']
    jdatal['started'] = p3['match']['timeinfo']['started']
    jdatal['ended'] = p3['match']['timeinfo']['ended']

    return jdatal

def scriptJ():
    now_date_str = datetime.datetime.now().strftime('%Y%m%d')
#    date_str = str(now_date.year)+ str(now_date.month)+ str(now_date.day)

    try:
        response = requests.get(
           'https://ls.sportradar.com/ls/feeds/?/itf/en/Europe:Berlin/gismo/client_dayinfo/'+now_date_str, timeout=(10, 10))
#           'https://ls.sportradar.com/ls/feeds/?/itf/en/Europe:Berlin/gismo/client_dayinfo/20170717', timeout = (10, 10))
        print('https://ls.sportradar.com/ls/feeds/?/itf/en/Europe:Berlin/gismo/client_dayinfo/'+now_date_str)

        data = json.loads(response.content)
        json_data = json.dumps(None)
        print('====+scriptJ()+====')
        jdata = []

        my_list = data['doc'][0]['data']['matches']
        i=0
        for elm in my_list:
            matchstatus = data['doc'][0]['data']['matches'][elm]['match']['matchstatus']
            if matchstatus == 'live':
#                jdata[elm] = elm
                jdata.append(matchstatus_live(elm, matchstatus,data['doc'][0]['data']['matches'][elm]))
                json_data = json.dumps(jdata)

        if len(jdata)>=4:
            json_data = json.dumps(jdata)
            print('len= ', len(json_data), '  json_data: ', json_data)
            return json_data
        else:
            print('Oops. no data!')
            return None

    except requests.exceptions.ConnectTimeout:
        print('Oops. Problems requests!')
        return None
