
class Plugin:
    def __init__(self):
        raise AttributeError("undefined init method")
    
    # load library for working with plugin
    def load(self):
        raise AttributeError("undefined load method")
    
    # setup connection/variables
    def setup(self):
        raise AttributeError("undefined setup method")
    
    # render data to web
    def view(self):
        raise AttributeError("undefined view method")
    
    # repeated action w/wo time parameter
    def periodical(self):
        raise AttributeError("undefined periodical method")
    
    # action when event occurs
    def event(self, eventname, eventparameter):
        raise AttributeError("undefined event method")

    # unload to finish work with plugin
    def unload(self):
        raise AttributeError("undefined unload method")  
    
    def readconfig(self):
        pass
        
    def writeconfig(self):
        pass
        