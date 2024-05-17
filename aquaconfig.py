from flask_sqlalchemy import SQLAlchemy

aqua_db = SQLAlchemy()

class aquaConfig(aqua_db.Model):
    __tablename__ = 'config'
    id = aqua_db.Column(aqua_db.Integer, primary_key=True)
    mqtt_host = aqua_db.Column(aqua_db.String, nullable=False, unique=True)
    mqtt_port = aqua_db.Column(aqua_db.Integer, nullable=False, unique=True, default=1883)
    mqtt_topic = aqua_db.Column(aqua_db.String, nullable=False, unique=True)
    config_date = aqua_db.Column(aqua_db.Date, nullable=False, unique=True)
    created = aqua_db.Column(aqua_db.Time, nullable=True)
    
#    aquaConfig = aquaConfig.query.first()
#    if not aquaConfig:
#        aquaConfig = aquaConfig(mqtt_host='127.0.0.1', mqtt_port='1883', mqtt_topic = '/aquapi')
#    else: aquaConfig = aquaConfig.query().first()
    aqua_db.session.commit()
