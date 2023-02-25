import db

global myconfig

class myConfig(db.Model):
    __tablename__ = 'config'
    id = db.Column(db.Integer, primary_key=True)
    mqtt_host = db.Column(db.String, nullable=False, unique=True)
    mqtt_port = db.Column(db.Integer, nullable=False, unique=True, default=1883)
    mqtt_topic = db.Column(db.String, nullable=False, unique=True)
    config_date = db.Column(db.Date, nullable=False, unique=True)
    created = db.Column(db.Time, nullable=True)
    
    myconfig = myConfig.query.first()
    if not myconfig:
        myconfig = AquaConfig(mqtt_host='127.0.0.1', mqtt_port='1883', mqtt_topic = '/aquapi')
    else: myconfig = AquaConfig.query().first()
    db.session.commit()    