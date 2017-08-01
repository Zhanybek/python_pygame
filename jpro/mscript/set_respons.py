import json
import sqlite3 as db

def getFromJpro_tournaments ():
    conn = db.connect('db.sqlite3')
    cursor = conn.cursor()
    sql='SELECT matches_id,tid,param5 FROM jpro_tournaments where matchstatus=\'live\' ORDER BY tid'
    cursor.execute(sql)

    columns = ('matches_id', 'tid', 'param5')
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    jres=json.dumps(results, indent=2)

    return jres