import json
import requests
import datetime
from time import time

from jpro.models import tennisinfo
from .Conn_DB import f_conn_BD

def matchstatus_live(ij, matchstatus, matches_ij,tournaments): #data['doc'][0]['data']['matches'][ij]
    jdatal = {}

    jdatal['matches_id'] = ij
    jdatal['tid'] = matches_ij['match']['_tid']
    jdatal['matchstatus'] = matchstatus
    jdatal['param5'] = matches_ij['param5']
    jdatal['param10'] = matches_ij['param10']
#    print('matches_ij: ',matches_ij )
#    print('tournaments: ', tournaments)
    #    jdatal['started'] = matches_ij['match']['timeinfo']['started']
    #    jdatal['ended'] = matches_ij['match']['timeinfo']['ended']
    my_list = tournaments
    for ijt in my_list:
         if tournaments[ijt]['_id'] == matches_ij['match']['_tid']:
             jdatal['city'] = tournaments[ijt]['tennisinfo']['city']
             jdatal['gender'] = tournaments[ijt]['tennisinfo']['gender']
             jdatal['type'] = tournaments[ijt]['tennisinfo']['type']
             jdatal['kind_sport'] = 'tennis'
             jdatal['prize_amount'] = tournaments[ijt]['tennisinfo']['prize']['amount']
             jdatal['prize_currency'] = tournaments[ijt]['tennisinfo']['prize']['currency']
             jdatal['itfid'] = tournaments[ijt]['itfid']
             jdatal['itfname'] = tournaments[ijt]['itfname']
             jdatal['ground_id'] = tournaments[ijt]['ground']['_id']
             jdatal['ground_name'] = tournaments[ijt]['ground']['name']
             jdatal['ground_mainid'] = tournaments[ijt]['ground']['mainid']
             jdatal['ground_main'] = tournaments[ijt]['ground']['main']
    '''
'id,               
'matches_id,      matches."12094402"
 tid              matche._tid
'matchstatus,     matches.match.matchstatus
'param5,          matches.param5
'param10,         matches.param10
'city,            tournaments.tennisinfo.city
'gender,          tournaments.tennisinfo.gender
'type,            tournaments.tennisinfo.type
'kind_sport,      "tennis"
'prize_amount,    tournaments.tennisinfo.prize.amount
'prize_currency,  tournaments.tennisinfo.prize.currency
'itfid,           tournaments.itfid
'itfname,         tournaments.itfname
'ground_id,       tournaments.ground._id
'ground_name,     tournaments.ground.name
'ground_mainid,   tournaments.ground.mainid
'ground_main'     tournaments.ground.main
'''
    return jdatal

def tennisinfo_f():
    '''
    json_rec = tennisinfo.objects.all()
    q1 = json_rec[0]
    s=''
    for q in json_rec:
        if s!='':
            s=s+', \n'
        s=s + q.gjson
    print(s)
    '''
    now_date_str = datetime.datetime.now().strftime('%Y%m%d')
    ourUrl = 'https://ls.sportradar.com/ls/feeds/?/itf/en/Europe:Berlin/gismo/client_dayinfo/'
    ourUrl += now_date_str
    #ourUrl += '20170801'
    try:
        response = requests.get(ourUrl, timeout=(10, 10))
    except requests.exceptions.ConnectTimeout:
        print('Oops. Problems requests!')
        return None

    print(ourUrl)

    data = json.loads(response.content)
    json_data = json.dumps(None)
    jdata = []
#{"queryUrl":"client_dayinfo\/20170729","doc":[{"event":
    my_list = data['doc'][0]['data']['matches']
    for ij in my_list:
        matchstatus = data['doc'][0]['data']['matches'][ij]['match']['matchstatus']
        if matchstatus == 'live':
            jdata.append(matchstatus_live(ij, matchstatus, data['doc'][0]['data']['matches'][ij],
                                          data['doc'][0]['data']['tournaments']))
            #jdata.append(data['doc'][0]['data'])
            json_data = json.dumps(jdata)
#    print('json_data: ', json_data) #None
    if json_data != 'null':
        tic = time()
        f_conn_BD('jpro_tournaments', json_data)
        toc = time()
        print('diffTime: ',toc - tic)

    if len(jdata) >= 4:
        json_data = json.dumps(jdata)

        #        insrec = tennisinfo(gjson=json_data)
        #        insrec.save()
        #        print('len= ', len(jdata), '  json_data: ', json_data)
        return json_data
    else:
        print('Oops. no data!')
        return None
