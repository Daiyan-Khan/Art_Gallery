from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Database:
    URI = 'postgresql://postgres:1234@localhost/sit331'

    @staticmethod
    def initialize(app):
        app.config['SQLALCHEMY_DATABASE_URI'] = Database.URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)

    @staticmethod
    def get_database():
        return db
