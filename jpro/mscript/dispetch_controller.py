#from jpro.mscript.set_respons import getFromTournaments
import jpro.mscript.set_respons as setRes
from .get_json01 import tennisinfo_f

def GetTournamentsJlist():
    tennisinfo_f()   # получает Json и заполняет оператвиную таблицу jpro_tournaments
    tournaments_lst = setRes.getFromTournaments() # выдает список турниров из таблицы jpro_tournaments

    return tournaments_lst

def GetMatchDetails(matcheId): # выдает детали матча из таблицы jpro_tournaments
    print('GetMatchDetails: ',matcheId)
    MatchDetailsJ = setRes.GetMatchDetailsJ (matcheId)

    return MatchDetailsJ
