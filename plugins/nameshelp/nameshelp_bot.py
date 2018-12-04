from errbot import BotPlugin, botcmd, botmatch
from pymongo import MongoClient
import random

amb = None
typ = None
sex = None

class NamesHelp(BotPlugin):
    'Name bank step-by-step'

    @botcmd
    def nameshelp(self, msg, args):
        'Asks which context the character is inserted in'
        yield 'In which context will the character be?'
        yield 'Available contexts:\nFantasy | Present'

    @botmatch(r'.*$', flow_only=True)
    def first(self, msg, match):
        'Filtra as ambientações e pergunta o tipo'
 
        # "Capturando" o input e colocando na global
        global amb
        amb = match.string.capitalize()
        
        # Preparando as respostas
        if amb == 'Fantasy':
            aa = 'Avaiable races for Fantasy:\nCentaur | Demon | Dragon\nDryad | Dwarf | Elemental\nEnt | Fairy | Ghostn\nGiant | Gnome | Goblin\nGod | Golem | Hobbit\nHuman | Minotaur | Monster\nElf | Ogre | Orc\nSea_creatures | Troll | Wizard'
        elif amb == 'Present':
            ab = 'Avaiable nationalities for Present:\nAmerican | Australian | Brazilian\nBritish | Chinese | French'
        else:
            yield 'Wrong context insertion'

        try:
            yield aa
        except:
            pass

        try:
            yield ab
        except:
            pass

    @botmatch(r'.*$', flow_only=True)
    def second(self, msg, match):
        'Filtra o tipo e pergunta o genero'
        
        # "Capturando" o input e colocando na global
        global typ
        typ = match.string.capitalize()

        yield "And finally, which will be the gender of the character?"
        yield 'Male (M) | Female (F) | Any (A)'

    @botmatch(r'.*$', flow_only=True)
    def third(self, msg, match):
        'Filtra o tudo e da o resultado'
        
        # Importa o que foi recebido nos ultimos comnados e adiciona o genero
        global amb
        global typ
        global sex

        sex = match.string.capitalize()
 
        # Importa os nomes do Mongo
        client = MongoClient()
        db = client.piDB
        collection = db['Names']
        
        # Faz o filetro, dependendo do sexo
        if sex == 'A':    
            cursor = collection.find({"$and": [{"Tags": amb}, {"Tags": typ}]})
        else:
            cursor = collection.find({"$and": [{"Tags": amb}, {"Tags": typ}, {"Tags": sex}]})
        
        # Transforma o que foi filtrado em uma lista
        i = list(cursor)
        
        # Faz o processo de filtragem tres vezes, mandando o resultado final
        yield 'Random names for your character:'
        o = 0
        for x in range(3):
            z = i[random.randint(0, int(len(i))-1)]
            print(x)
            if o == 0:
                if sex == 'M':
                    if 'F' in z['Tags']:
                        if amb == 'Fantasy':
                            yield '# Please note: This race is genderless'
                elif sex == 'F':
                    if 'M' in z['Tags']:
                        if amb == 'Fantasy':
                            yield '# Please note: This race is genderless'
            o = o + 1
            if sex == 'A':
                if 'M' in z['Tags'] and 'F' in z['Tags']:
                    j = 'Genderless'
                elif z['Tags'][2] == 'M':
                    j = 'Male'
                elif z['Tags'][2] == 'F':
                    j = 'Female'
                yield str(z['Name']) + ' (' + j + ')'

            if sex == 'M' or sex == 'F':
                yield z['Name']
























