from flask import Blueprint, jsonify, request, current_app
from models.artifact import Artifact
from persistence import IArtifactDataAccess
from flask_login import login_required,current_user

artifacts_blueprint = Blueprint('artifacts', __name__)

def get_artifact_repository() -> IArtifactDataAccess:
    return current_app.config['artifact_repo']

@artifacts_blueprint.route('/protected')
@login_required
def protected():
    return 'This is a protected route.'


@artifacts_blueprint.route('/artifacts', methods=['POST'])
@login_required
def create_artifact():
    data = request.get_json()
    if not data or not 'title' in data:
        return jsonify({'message': 'Invalid input'}), 400
    
    new_artifact = Artifact(
        title=data['title'],
        description=data.get('description', ''),
    )

    repo = get_artifact_repository()
    repo.create_artifact(new_artifact)

    return jsonify(new_artifact.json()), 201

@artifacts_blueprint.route('/artifacts', methods=['GET'])
@login_required
def get_all_artifacts():
    repo = get_artifact_repository()
    artifacts = repo.get_all_artifacts()
    return jsonify([artifact.json() for artifact in artifacts]), 200

@artifacts_blueprint.route('/artifacts/<int:artifact_id>', methods=['GET'])
def get_artifact(artifact_id):
    repo = get_artifact_repository()
    artifact = repo.get_artifact_by_id(artifact_id)
    if artifact:
        return jsonify(artifact.json()), 200
    else:
        return jsonify({'message': 'Artifact not found'}), 404

@artifacts_blueprint.route('/artifacts/<int:artifact_id>', methods=['PUT'])
def update_artifact(artifact_id):
    data = request.get_json()
    repo = get_artifact_repository()
    artifact = repo.get_artifact_by_id(artifact_id)
    if artifact:
        artifact.title = data.get('title', artifact.title)
        artifact.description = data.get('description', artifact.description)
        repo.update_artifact(artifact)
        return jsonify(artifact.json()), 200
    else:
        return jsonify({'message': 'Artifact not found'}), 404


@artifacts_blueprint.route('/artifacts/<int:artifact_id>', methods=['DELETE'])
def delete_artifact(artifact_id):
    repo = get_artifact_repository()
    if repo.delete_artifact(artifact_id):
        return jsonify({'message': 'Artifact deleted successfully'}), 200
    else:
        return jsonify({'message': 'Artifact not found'}), 404
