
global dataDo
    
class PluginMQTT(plugins.plugin.Plugin):
    def __init__(self):    
        pass
    
    def render(self):
        print(dataDo, _('Read temperature...'))
        print(dataDo, 'Read watter level...')
        print(dataDo, 'Redraw info display...')
    
        print(dataDo, 'Setup lights...')
        print(dataDo, 'Publish mqtt data...')
        dataDo = dataDo + 1