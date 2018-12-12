from errbot import botflow, FlowRoot, BotFlow


class MusicFlow(BotFlow):
    'flow para a musica'

    @botflow
    def musics_flow(self, flow: FlowRoot):
        'Musics flow'
        fruta = flow.connect('musics', auto_trigger=True)
        verdura = fruta.connect('seila')
        vegetal = verdura.connect('papagaio')
