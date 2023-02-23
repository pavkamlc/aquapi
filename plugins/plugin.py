class Plugin:
    def __init__(self):
        raise AttributeError("undefined init method")
    
    # load library for working with plugin
    def load():
        raise AttributeError("undefined load method")
    
    # setup connection/variables
    def setup():
        raise AttributeError("undefined setup method")
    
    # render data to web
    def view():
        raise AttributeError("undefined view method")
    
    # repeated action w/wo time parameter
    def periodical():
        raise AttributeError("undefined periodical method")
    
    # unload to finish work with plugin
    def unload():
        raise AttributeError("undefined unload method")  
    
    def readconfig():
        a=1
        
    def writeconfig():
        a=2
        