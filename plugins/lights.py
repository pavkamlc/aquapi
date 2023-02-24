class AquaLight(db.Model):
    __tablename__ = 'light'
    id = db.Column(db.Integer, primary_key=True)
    lightchannel = db.Column(db.Integer, nullable=False)
    lightminute = db.Column(db.Integer, nullable=False)
    lightvalue = db.Column(db.SmallInteger, nullable=False)