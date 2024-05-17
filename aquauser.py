from flask_sqlalchemy import SQLAlchemy

aqua_db = SQLAlchemy()

class aquaUser(aqua_db.Model):
    __tablename__ = 'users'
    id = aqua_db.Column(aqua_db.Integer, primary_key=True)
    username = aqua_db.Column(aqua_db.String, nullable=False, unique=True)
    password = aqua_db.Column(aqua_db.String, nullable=False, unique=False)
    email = aqua_db.Column(aqua_db.String, nullable=False, unique=True)
    active = aqua_db.Column(aqua_db.Boolean, nullable=False, default=True)
    created = aqua_db.Column(aqua_db.Time, nullable=True)

    @property
    def is_active(self):
        return self.active
    
    def __repr__(self):
        return '<User %r>' % self.username
    
#if not aquaUser.query.filter_by(username='admin').first():
#    admin = aquaUser(username='admin', email='admin@example.com', password = 'asdf')
#    aqua_db.session.add(admin)
#if not aquaUser.query.filter_by(username='guest').first():
#    guest = aquaUser(username='guest', email='guest@example.com', password='')
#    aqua_db.session.add(guest)
aqua_db.session.commit()
