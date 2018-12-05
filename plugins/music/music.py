from errbot import BotPlugin, botcmd, botmatch

class Music(BotPlugin):
    """Musica para ambientaçao"""
    @botcmd
    def musics(self, msg, args):
        'Pergunta o tema da musica'
        yield'Escolha o tema da musica: Medieval\nContemporanea'
    

    @botmatch(r'.*$', flow_only=True)
    def seila(self, msg, match):
        'faz algo '
        global tem
        tem = match.string.capitalize()
        if tem == 'Contemporanea':
            yield 'olha essa musica legal demais'
            self.send_stream_request(msg.frm, open('audio/miniboi.mp3', 'rb'),
                                     name='miniboi.mp3', stream_type='audio')
        elif tem == 'Medieval':            
            yield'olha essa musica legal demais 2'
            self.send_stream_request(msg.frm, open('audio/treespiritjurak.mp3', 'rb'),
				     name='treespiritjurak.mp3', stream_type='audio')
        else:            
            yield 'deu erro ai meu truta'
