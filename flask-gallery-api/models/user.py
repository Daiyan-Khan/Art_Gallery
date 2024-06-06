from utils.database import db
from flask_login import UserMixin
from passlib.hash import bcrypt

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    
    def set_password(self, password):
        self.password = bcrypt.hash(password)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password)

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role' : self.role
        }
