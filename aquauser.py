import aquadb
import sqlalchemy

class aquaUser(aquadb.aqua_db.Model):
    __tablename__ = 'users'
    id = aquadb.aqua_db.Column(aquadb.aqua_db.Integer, primary_key=True)
    username = aquadb.aqua_db.Column(aquadb.aqua_db.String, nullable=False, unique=True)
    password = aquadb.aqua_db.Column(aquadb.aqua_db.String, nullable=False, unique=False)
    email = aquadb.aqua_db.Column(aquadb.aqua_db.String, nullable=False, unique=True)
    active = aquadb.aqua_db.Column(aquadb.aqua_db.Boolean, nullable=False, default=True)
    created = aquadb.aqua_db.Column(aquadb.aqua_db.Time, nullable=True)
    
    @property
    def is_active(self):
        return self.active
    
    def __repr__(self):
        return '<User %r>' % self.username
     
    def aquauser_init():
        # exist table users?
        aqua_config = sqlalchemy.inspect(aquadb.aqua_db.engine).has_table('users')

        # exist user admin?
        if not aqua_config or not aquaUser.query.filter_by(username='admin').first():
            admin = aquaUser(username='admin', email='admin@example.com', password = 'asdf')
            aquadb.aqua_db.session.add(admin)
        # exist user guest?
        if not aqua_config or not aquaUser.query.filter_by(username='guest').first():
            guest = aquaUser(username='guest', email='guest@example.com', password='')
            aquadb.aqua_db.session.add(guest)
        
        aquadb.aqua_db.create_all()
    
        aquadb.aqua_db.session.commit()
