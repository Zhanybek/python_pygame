import json
#import datetime
#from time import gmtime, strftime

from jpro.models import Tournaments

# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3 as db

from jpro.mscript.set_tournaments import RealiTournaments


def f_conn_BD(tbl, jdata):
# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
    conn = db.connect('db.sqlite3')
    #conn.execute()
# Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor = conn.cursor()

# ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
    RealiTournaments(cursor,conn, jdata)
#    addToJpro_tournaments(cursor,conn, jdata)

#    cursor.execute('SELECT tid,name FROM jpro_tournaments ORDER BY tid LIMIT 3')

# КОД ДАЛЬНЕЙШИХ ПРИМЕРОВ ВСТАВЛЯТЬ В ЭТО МЕСТО

#    results = cursor.fetchall()

#    print(results)
# Не забываем закрыть соединение с базой данных
    conn.close()
