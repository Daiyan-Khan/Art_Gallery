from utils.database import db

class Artifact(db.Model):
    __tablename__ = 'artifacts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    def __init__(self, title, description):
        self.title = title
        self.description = description
        
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
        }
