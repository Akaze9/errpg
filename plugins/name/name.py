from errbot import BotPlugin, botcmd
from pymongo import MongoClient
import random

class Name(BotPlugin):
    """Banco de nomes para NPC"""
    @botcmd(split_args_with=None)
    def names(self, msg, args):
        # Cria as variaveis dependendo da quantidade de argumentos
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

        # Setup do mongo
        client = MongoClient()
        db = client.piDB
        collection = db['Names']

        # Filtros
        cursor = []
        if 'a' in locals():
            cursor = collection.find({"$and": [{"Tags": a}]})
        
        if 'b' in locals():
            cursor = collection.find({"$and": [{"Tags": a}, {"Tags": b}]})
        
        if 'c' in locals():
            cursor = collection.find({"$and": [{"Tags": a}, {"Tags": b}, {"Tags": c}]})

        # Transforma em uma lista
        
        i = list(cursor)
        
        # Verifica se as variaveis foram criadas e se estao corretas

        if len(args) == 0:
            yield 'Please insert at least one tag'
        elif len(i) == 0:
            yield 'Wrong tag insertion'
        else:

        # Printa um item aleatorio da lista filtrada
        
            z = i[random.randint(0, int(len(i))-1)]
            yield z['Name']

















