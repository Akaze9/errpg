from errbot import BotPlugin, botcmd
import random

class Diceroller(BotPlugin):
    """Dice roller"""
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

        
            n = int(loop)
            if 4 <= n <= 20:
                suffix = 'th'
            elif n == 1 or (n % 10) == 1:
                suffix = 'st'
            elif n == 2 or (n % 10) == 2:
                suffix = 'nd'
            elif n == 3 or (n % 10) == 3:
                suffix = 'rd'
            elif n < 100:
                suffix = 'th'
            ord_num = str(n) + suffix
        
            if 'all' in args:

                yield ord_num + ' roll: ' + str(resind)
                numresind = numresind+1

        yield 'Final result: ' + str(total)

