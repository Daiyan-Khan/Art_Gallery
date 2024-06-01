from utils.database import db

class Artifact(db.Model):
    __tablename__ = 'artifacts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    def __init__(self, title, description, artist_id):
        self.title = title
        self.description = description

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, artifact_id):
        return cls.query.filter_by(id=artifact_id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
        }
