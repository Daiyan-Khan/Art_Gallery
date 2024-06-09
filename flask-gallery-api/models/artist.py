from utils.database import db

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=True)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'bio': self.bio
        }
