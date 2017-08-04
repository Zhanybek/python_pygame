import json
import sqlite3 as db

from django import template


def getFromTournaments ():
    conn = db.connect('db.sqlite3')
    sql='SELECT matches_id,tid,param5 FROM jpro_tournaments group by tid ORDER BY tid' # where matchstatus=\'live\'
    cursor = conn.cursor()
    cursor.execute(sql)

    columns = ('matches_id', 'tid', 'param5')
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    jres=json.dumps(results, indent=2)

    return jres

register = template.Library()
@register.inclusion_tag('templates/jpro/jonny_base.html')

def GetMatchDetailsJ(matcheId):
    conn = db.connect('db.sqlite3')
    sql='SELECT t.gender, t.ground_name, t.itfname,t.prize_amount,t.prize_currency,t.type FROM jpro_tournaments t' \
        ' WHERE t.matches_id IN ('+matcheId+')'
    cursor = conn.cursor()
    print(sql)
    cursor.execute(sql)
    MatchDetailsJ =cursor.fetchall()

    jres = json.dumps(MatchDetailsJ, indent=2)
    print(jres)
    return jres
#    return {'MatchDetailsJ': jres}
    pass

