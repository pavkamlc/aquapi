from flask_sqlalchemy import SQLAlchemy

global db

db = SQLAlchemy()

db.init_app(app)
db.create_all()