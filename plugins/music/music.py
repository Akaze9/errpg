from errbot import BotPlugin, botcmd, botmatch


tem = None
sit = None

class Music(BotPlugin):
    """Musica para ambientaçao"""
    @botcmd
    def musics(self, msg, args):
        'Pergunta o tema da musica'
        yield'Choose the theme:\nMedieval | Sci-fi'
    

    @botmatch(r'.*$', flow_only=True)
    def seila(self, msg, match):
        'faz algo '
        global tem
        tem = match.string.capitalize()
        if tem == 'Sci-fi':
            yy = 'Cyberpunk | Other'

        elif tem == 'Medieval':                         
            xx = 'Town | Forest | Battles | Ambient | Tavern '           
        else:
            yield 'Wrong insertion'
        #Mostra as opcoes na tela        
        try:
            yield xx
        except:
            pass
        try:
            yield yy
        except:
            pass
    @botmatch(r'.*$', flow_only=True)
    def papagaio(self, msg, match):
        'mostra as opcoes de musica para cada topico e situacao'
        global tem
        global sit
        sit = match.string.capitalize()
        
        if sit == 'Forest':
           yield 'These are the available musics for \"Forest\"' 
           self.send_stream_request(msg.frm, open('audio/treespiritjurak.mp3', 'rb'),
				     name='treespiritjurak.mp3', stream_type='audio')
         
           self.send_stream_request(msg.frm, open('audio/mushroomglade.mp3', 'rb'),
				     name='mushroomglade.mp3', stream_type='audio')
 
           self.send_stream_request(msg.frm, open('audio/mermaidsofraindroplake.mp3', 'rb'),
				     name='mermaidsofraindroplake.mp3', stream_type='audio')
         
           self.send_stream_request(msg.frm, open('audio/sylphcloudcanopy.mp3', 'rb'),
				     name='sylphcloudcanopy.mp3', stream_type='audio')

        elif sit == 'Town':

           yield 'These are the available musics for \"Town\"'
           self.send_stream_request(msg.frm, open('audio/cityofsails.mp3', 'rb'),
                                    name='miniboi.mp3', stream_type='audio')
        
           self.send_stream_request(msg.frm, open('audio/merchant.mp3', 'rb'),
                                    name='merchant.mp3', stream_type='audio')
        
        
        
        elif sit == 'Battles':
           yield'These are the available musics for \"Battles\"'
           self.send_stream_request(msg.frm, open('audio/jugger.mp3', 'rb'),
                                    name='jugger.mp3', stream_type='audio')
        
           self.send_stream_request(msg.frm, open('audio/gloryseeker.mp3', 'rb'),
                                    name='gloryseeker.mp3', stream_type='audio')
        elif sit == 'Ambient':
           yield 'These are the available musics for \"Ambient\"'
           self.send_stream_request(msg.frm, open('audio/1ambient.mp3', 'rb'),
                                    name='1ambient.mp3', stream_type='audio')
        
           self.send_stream_request(msg.frm, open('audio/2ambient.mp3', 'rb'),
                                    name='2ambient.mp3', stream_type='audio')
        
        elif sit == 'Cyberpunk':
           yield 'These are the available musics for \"Cyberpunk\"'
           self.send_stream_request(msg.frm, open('audio/1cyberpunk.mp3', 'rb'),
                                    name='1cyberpunk.mp3', stream_type='audio')

           self.send_stream_request(msg.frm, open('audio/2cyberpunk.mp3', 'rb'),
                                    name='2cyberpunk.mp3', stream_type='audio')
                    
        elif sit == 'Tavern':
           yield 'These are the available musics for \"Tavern\"'
           self.send_stream_request(msg.frm, open('audio/1tavern', 'rb'),
                                    name='1tavern.mp3', stream_type='audio')


           self.send_stream_request(msg.frm, open('audio/2tavern', 'rb'),
                                    name='2tavern.mp3', stream_type='audio')

        else:
            yield 'Wrong insertion'
