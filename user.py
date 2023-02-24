class AquaUser(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False, unique=False)
    email = db.Column(db.String, nullable=False, unique=True)
    active = db.Column(db.Boolean, nullable=False, default=True)
    created = db.Column(db.Time, nullable=True)

    @property
    def is_active(self):
        return self.active
    
    def __repr__(self):
        return '<User %r>' % self.username