from errbot import botflow, FlowRoot, BotFlow


class NameshelpFlow(BotFlow):
    "Name bank's flow"

    @botflow
    def example(self, flow: FlowRoot):
        first_step = flow.connect('nameshelp', auto_trigger=True)
        second_step = first_step.connect('first')
        third_step = second_step.connect('second')
        fourth_step = third_step.connect('third')
