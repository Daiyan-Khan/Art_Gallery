from typing import List
from models.artifact import Artifact

class IArtifactDataAccess:
    def get_all_artifacts(self) -> List[Artifact]:
        raise NotImplementedError

    def get_artifact_by_id(self, artifact_id: int) -> Artifact:
        raise NotImplementedError

    def create_artifact(self, artifact: Artifact) -> None:
        raise NotImplementedError

    def update_artifact(self, artifact: Artifact) -> None:
        raise NotImplementedError

    def delete_artifact(self, artifact_id: int) -> bool:
        raise NotImplementedError

    def artifact_exists(self, artifact_id: int) -> bool:
        raise NotImplementedError
