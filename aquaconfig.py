import aquadb
import sqlalchemy
      
class aquaConfig(aquadb.aqua_db.Model):
    __tablename__ = 'config'
    id = aquadb.aqua_db.Column(aquadb.aqua_db.Integer, primary_key=True)
    mqtt_host = aquadb.aqua_db.Column(aquadb.aqua_db.String, nullable=False, unique=True)
    mqtt_port = aquadb.aqua_db.Column(aquadb.aqua_db.Integer, nullable=False, unique=True, default=1883)
    mqtt_topic = aquadb.aqua_db.Column(aquadb.aqua_db.String, nullable=False, unique=True)
    config_date = aquadb.aqua_db.Column(aquadb.aqua_db.Date, nullable=False, unique=True)
    created = aquadb.aqua_db.Column(aquadb.aqua_db.Time, nullable=True)
    
    def aquaconfigInit():
        # if not exist table config then create default
        if sqlalchemy.inspect(aquadb.aqua_db.engine).has_table('config'):
            aqua_config = aquaConfig(mqtt_host='127.0.0.1', mqtt_port='1883', mqtt_topic = '/aquapi')
            aquadb.aqua_db.session.commit()
            
aqua_config = aquaConfig.query().first()   
        
aqua_config = aquaConfig()         