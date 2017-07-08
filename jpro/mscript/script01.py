import requests
import json

def matchstatus_live(p1, p2, p3):
    jdatal = {}
    jdatal['param5'] = p3['param5']
    jdatal['started'] = p3['match']['timeinfo']['started']
    jdatal['ended'] = p3['match']['timeinfo']['ended']
    return jdatal


def scriptJ():
    print('script J')

    try:
        response = requests.get(
            'https://ls.sportradar.com/ls/feeds/?/itf/en/Europe:Berlin/gismo/client_dayinfo/20170708', timeout=(10, 10))
        #   print(response.content)

        data = json.loads(response.content)
        print('=========')
        jdata = {}
        my_list = data['doc'][0]['data']['matches']

        for elm in my_list:
            matchstatus = data['doc'][0]['data']['matches'][elm]['match']['matchstatus']
            if matchstatus == 'live':
                jdata[elm] = elm
                jdata[elm] = matchstatus_live(elm, matchstatus,data['doc'][0]['data']['matches'][elm])
                json_data = json.dumps(jdata)
        print('json_data: ',json_data)
        print(jdata)
        return json_data
    except requests.exceptions.ConnectTimeout:
        print('Oops. Problems requests!')
        return None
