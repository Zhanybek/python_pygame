from jpro.mscript.set_respons import getFromTournaments
from .get_json01 import tennisinfo_f

def runner():
    tennisinfo_f()
    tournaments_lst = getFromTournaments()

    return tournaments_lst