from errbot import BotPlugin, botcmd
from pymongo import MongoClient
import random

class Name(BotPlugin):
    """Banco de nomes para NPC"""
    @botcmd(split_args_with=None)
    def names(self, msg, args):
        try:
            if args[0].capitalize() == 'All':
                x = args[0].capitalize()
            else:
                a = args[0].capitalize()
        except:
            pass

        try:
            if args[1].capitalize() == 'All':
                x = args[1].capitalize()
            else:
                b = args[1].capitalize()
        except:
            pass

        try:
            if args[2].capitalize() == 'All':
                x = args[2].capitalize()
            else:
                c = args[2].capitalize()
        except:
            pass

        try:
            if args[3].capitalize() == 'All':
                x = args[3].capitalize()
            else:
                d = args[3].capitalize()
        except:
            pass

        try:
            if args[4].capitalize() == 'All':
                x = args[4].capitalize()
            else:
                e = args[4].capitalize()


        #Setup do mongo
        client = MongoClient()
        db = client.piDB
        collection = db['Nomes']

        #Filtros
        if 'a' in locals():
            cursor = collection.find({"Tags": a})
        
        if 'b' in locals():
            cursor = collection.find({"Tags": b})

        if 'c' in locals():
            cursor = collection.find({"Tags": c})

        if 'd' in locals():
            cursor = collection.find({"Tags": d})

        #Transforma em uma lista
        i = list(cursor)
        if len(i) == 0:
            yield 'Wrong tag insertion'
        else:
        #Printa um item aleatorio da lista
            z = i[random.randint(0, int(len(i))-1)]
            yield z['Name']
