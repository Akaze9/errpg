from errbot import BotPlugin, botcmd
import random

class Rolador(BotPlugin):
    """Rolador de dados"""
    @botcmd(split_args_with=None)
    def roll(self, msg, args):
        # Pegando o primeiro item da lista 'args', que deve ser obrigatoriamente a quantidade
        # e valor do dado, ex: 2d20
        valor = args[0]

        # Cria uma lista contendo a quantidade de dados como primeiro item e o tipo de
        # dado como o segundo
        dado = valor.split("d")

        quant= dado[0]
        tipo = dado[1]

        loop = 0
        total = 0
        numresind = 1
        

        while loop < int(quant):
            resind = random.randint(1, int(tipo))
            total = total+resind
            loop = loop+1

            if 'all' in args:
                yield str(numresind) + 'ª rolagem: ' + str(resind)
                numresind = numresind+1

        yield 'Resultado final: ' + str(total)

