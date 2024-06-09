from flask import Blueprint, jsonify, request, current_app
from models.artifact import Artifact
from persistence import IArtifactDataAccess
from flask_login import login_required, current_user

artifacts_blueprint = Blueprint('artifacts', __name__)


def get_artifact_repository() -> IArtifactDataAccess:
    """
    Retrieves the artifact repository from the current Flask application configuration.

    Returns:
        IArtifactDataAccess: The artifact repository implementation.
    """
    return current_app.config['artifact_repo']

@artifacts_blueprint.route('/protected')
@login_required
def protected():
    """
    Endpoint to test login-required functionality.

    Returns:
        str: A message indicating successful access to a protected route.
    """
    return 'This is a protected route.'

@artifacts_blueprint.route('/artifacts', methods=['POST'])
@login_required
def create_artifact():
    """
    Endpoint for creating a new artifact.

    Request Body:
        {
            "title": "string",       # The title of the artifact (required)
            "description": "string"  # Optional description of the artifact
        }

    Returns:
        JSON: The created artifact object with status code 201.
    """
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
    """
    Endpoint for retrieving all artifacts.

    Returns:
        JSON: List of artifact objects with status code 200.
    """
    repo = get_artifact_repository()
    artifacts = repo.get_all_artifacts()
    return jsonify([artifact.json() for artifact in artifacts]), 200

@artifacts_blueprint.route('/artifacts/<int:artifact_id>', methods=['GET'])
def get_artifact(artifact_id):
    """
    Endpoint for retrieving a specific artifact by ID.

    Args:
        artifact_id (int): The ID of the artifact to retrieve.

    Returns:
        JSON: The artifact object with status code 200 if found, or a message with status code 404 if not found.
    """
    repo = get_artifact_repository()
    artifact = repo.get_artifact_by_id(artifact_id)
    if artifact:
        return jsonify(artifact.json()), 200
    else:
        return jsonify({'message': 'Artifact not found'}), 404

@artifacts_blueprint.route('/artifacts/<int:artifact_id>', methods=['PUT'])
def update_artifact(artifact_id):
    """
    Endpoint for updating an existing artifact by ID.

    Args:
        artifact_id (int): The ID of the artifact to update.

    Request Body:
        {
            "title": "string",       # The updated title of the artifact
            "description": "string"  # Optional updated description of the artifact
        }

    Returns:
        JSON: The updated artifact object with status code 200 if found, or a message with status code 404 if not found.
    """
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
    """
    Endpoint for deleting an artifact by ID.

    Args:
        artifact_id (int): The ID of the artifact to delete.

    Returns:
        JSON: A message indicating success or failure of the deletion operation with status code 200 if successful,
              or a message with status code 404 if the artifact was not found.
    """
    repo = get_artifact_repository()
    if repo.delete_artifact(artifact_id):
        return jsonify({'message': 'Artifact deleted successfully'}), 200
    else:
        return jsonify({'message': 'Artifact not found'}), 404
