from models.artifact import Artifact
from utils.database import db
from persistence.IArtifactDataAccess import IArtifactDataAccess

class ArtifactRepository(IArtifactDataAccess):
    
    def get_all_artifacts(self):
        return Artifact.query.all()

    def get_artifact_by_id(self, artifact_id):
        return Artifact.query.get(artifact_id)

    def create_artifact(self, artifact):
        db.session.add(artifact)
        db.session.commit()

    def update_artifact(self, artifact):
        db.session.commit()

    def delete_artifact(self, artifact_id):
        artifact = self.get_artifact_by_id(artifact_id)
        if artifact:
            db.session.delete(artifact)
            db.session.commit()
            return True
        return False

    def artifact_exists(self, artifact_id):
        return db.session.query(db.exists().where(Artifact.id == artifact_id)).scalar()
