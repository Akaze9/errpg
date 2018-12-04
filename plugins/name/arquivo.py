from errbot import BotPlugin, botcmd
from pymongo import MongoClient
import random

class Name(BotPlugin):
    """Banco de nomes para NPC"""
    @botcmd(split_args_with=None)
    def names(self, msg, args):
        try:
            a = args[0].capitalize()
        except:
            pass

        try:
            b = args[1].capitalize()
        except:
            pass

        try:
            c = args[2].capitalize()
        except:
            pass

        try:
            d = args[3].capitalize()
        except:
            pass

        #Setup do mongo
        client = MongoClient()
        db = client.piDB
        collection = db['Nomes']

        #Filtros
        try:
            cursor = collection.find({"Tags": a})
        except:
            pass
        
        try:
            cursor = collection.find({"Tags": b})
        except:
            pass

        try:
            cursor = collection.find({"Tags": c})
        except:
            pass

        try:
            cursor = collection.find({"Tags": d})
        except:
            pass

        #Transforma em uma lista
        i = list(cursor)

        #Printa um item aleatorio da lista
        #yield i[random.randint(0, int(len(i))-1)]
        z = i[random.randint(0, int(len(i))-1)]
        yield z['Name']

