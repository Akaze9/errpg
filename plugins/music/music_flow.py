from errbot import botflow, FlowRoot, BotFlow


class MusicFlow(BotFlow):
    'flow para a musica'

    @botflow
    def example(self, flow: FlowRoot):
        first_step = flow.connect('musics', auto_trigger=True)
        second_step = first_step.connect('seila')
