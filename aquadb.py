from flask_sqlalchemy import SQLAlchemy
import sqlalchemy_utils

aqua_db = SQLAlchemy()

def aquadbInit(aquaapp):
    
    aquaapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aquapi.sqlite'
    aquaapp.app_context().push()
    
    aqua_db.init_app(aquaapp)
    aqua_db.create_all()
    
    #if not sqlalchemy_utils.database_exists('sqlite:///aquapi.sqlite'):
    #    sqlalchemy_utils.create_database('sqlite:///aquapi.sqlite')

        