import json
#import datetime
from time import gmtime, strftime

def RealiTournaments(cursor, conn, jdata):
    #    print('data is commit begin: ', strftime("%Y-%m-%d %H:%M:%S:%m", gmtime()))
    jdata = json.loads(jdata)

    #    if jdata!=None:
    my_list = jdata
#    sql = 'update jpro_tournaments set matchstatus=\'''\''
#    cursor.execute(sql)
#    conn.commit()
    TournamentsArc(conn,cursor,my_list)
#    conn.commit()
    recsIns=0
    for ji in my_list:
        recsIns = recsIns+ jpro_tournaments_insert(cursor, ji)
#        recsUpd = jpro_tournaments_update(cursor, ji)
    conn.commit()
    #    print('data is commit end: ', strftime("%Y-%m-%d %H:%M:%S:%m", gmtime()), '  recsIns: ', recsIns)
    print('  recsIns: ', recsIns)
    pass


def TournamentsArc (conn,cursor,my_list):
    wheres =''
    for il in my_list:
        wheres+=il['matches_id']+","

    wheres = ' WHERE matches_id not in ('+wheres[:-1]+')'

    sql='replace into tournaments_arc select * from jpro_tournaments' + wheres
    print(sql)
    cursor.execute(sql)
    #conn.commit()
    sql = 'delete from jpro_tournaments' + wheres
    print(sql)
    cursor.execute(sql)
    conn.commit()


def jpro_tournaments_insert(cursor,ji):
    recsIns = 0
    sql = 'INSERT INTO jpro_tournaments'
    sql += ' SELECT ' + str(ji['matches_id']) + ','
    sql += '\'' + str(ji['tid']) + '\','
    sql += '\'' + ji['matchstatus'] + '\','
    sql += '\'' + ji['param5'] + '\','
    sql += '\'' + ji['param10'] + '\','
    sql += '\'' + ji['city'] + '\','
    sql += '\'' + ji['gender'] + '\','
    sql += '\'' + ji['type'] + '\','
    sql += '\'' + ji['kind_sport'] + '\','
    sql += '\'' + ji['prize_amount'] + '\','
    sql += '\'' + ji['prize_currency'] + '\','
    sql += '\'' + ji['itfid'] + '\','
    sql += '\'' + ji['itfname'] + '\','
    sql += '\'' + ji['ground_id'] + '\','
    sql += '\'' + ji['ground_name'] + '\','
    sql += '\'' + ji['ground_mainid'] + '\','
    sql += '\'' + ji['ground_main'] + '\''
    sql += ' WHERE NOT EXISTS(SELECT 1 FROM jpro_tournaments WHERE'
    sql += ' matches_id=' + str(ji['matches_id']) + ')'
    res = cursor.execute(sql)
    recsIns = recsIns + res.rowcount
    return  recsIns


def jpro_tournaments_update(cursor,ji):
    recsUpd = 0
    sql = 'update jpro_tournaments'
    sql += ' SET matches_id=' + str(ji['matches_id']) + ','
    sql += 'tid=\'' + str(ji['tid']) + '\','
    sql += 'matchstatus=\'' + ji['matchstatus'] + '\','
    sql += 'param5=\'' + ji['param5'] + '\','
    sql += 'param10=\'' + ji['param10'] + '\','
    sql += 'city=\'' + ji['city'] + '\','
    sql += 'gender=\'' + ji['gender'] + '\','
    sql += 'type=\'' + ji['type'] + '\','
    sql += 'kind_sport=\'' + ji['kind_sport'] + '\','
    sql += 'prize_amount=\'' + ji['prize_amount'] + '\','
    sql += 'prize_currency=\'' + ji['prize_currency'] + '\','
    sql += 'itfid=\'' + ji['itfid'] + '\','
    sql += 'itfname=\'' + ji['itfname'] + '\','
    sql += 'ground_id=\'' + ji['ground_id'] + '\','
    sql += 'ground_name=\'' + ji['ground_name'] + '\','
    sql += 'ground_mainid=\'' + ji['ground_mainid'] + '\','
    sql += 'ground_main=\'' + ji['ground_main'] + '\''
    sql += ' WHERE matches_id=' + str(ji['matches_id'])#+' and matchstatus=\'live\''
    #print(sql)
    res = cursor.execute(sql)
    recsUpd = recsUpd + res.rowcount
    return  recsUpd



'''
    sql='insert into jpro_tournaments ' \
    '(matches_id,tid,matchstatus,param5,param10,city,gender,type,kind_sport,prize_amount,prize_currency,' \
    'itfid,itfname,ground_id,ground_name,ground_mainid,ground_main)'  \
    ' VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

#    jdata=json.loads(jdata)
    my_list = jdata
    for ji in jdata:
        cursor.execute(sql,
                       (ji['matches_id'],
                        ji['tid'],
                        ji['matchstatus'],
                        ji['param5'],
                        ji['param10'],
                        ji['city'],
                        ji['gender'],
                        ji['type'],
                        ji['kind_sport'],
                        ji['prize_amount'],
                        ji['prize_currency'],
                        ji['itfid'],
                        ji['itfname'],
                        ji['ground_id'],
                        ji['ground_name'],
                        ji['ground_mainid'],
                        ji['ground_main']
                        )
                       )
        conn.commit()
#    results = cursor.fetchall()
'''
