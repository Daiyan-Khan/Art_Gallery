from flask import Blueprint, jsonify, request
from models.artifact import Artifact

artifacts_blueprint = Blueprint('artifacts', __name__)

@artifacts_blueprint.route('/artifacts', methods=['POST'])
def create_artifact():
    """
    Create a new artifact.

    This endpoint allows you to create a new artifact with the provided details.

    Request Body:
    {
        "title": "Example Title",
        "description": "Example Description",
        "artist_id": 1
    }

    Returns:
    A JSON object containing the details of the created artifact.
    """
    data = request.get_json()
    new_artifact = Artifact(**data)
    new_artifact.save_to_db()
    return jsonify(new_artifact.json()), 201

@artifacts_blueprint.route('/artifacts', methods=['GET'])
def get_all_artifacts():
    """
    Get all artifacts.

    This endpoint returns a list of all artifacts stored in the database.

    Returns:
    A JSON array containing details of all artifacts.
    """
    artifacts = Artifact.query.all()
    return jsonify([artifact.json() for artifact in artifacts])

@artifacts_blueprint.route('/artifacts/<int:artifact_id>', methods=['GET'])
def get_artifact(artifact_id):
    """
    Get an artifact by ID.

    This endpoint returns the details of the artifact with the specified ID.

    Parameters:
    - artifact_id: The ID of the artifact to retrieve.

    Returns:
    A JSON object containing the details of the artifact.
    """
    artifact = Artifact.find_by_id(artifact_id)
    if artifact:
        return jsonify(artifact.json())
    else:
        return jsonify({'message': 'Artifact not found'}), 404

@artifacts_blueprint.route('/artifacts/<int:artifact_id>', methods=['PUT'])
def update_artifact(artifact_id):
    """
    Update an artifact by ID.

    This endpoint allows you to update the details of the artifact with the specified ID.

    Parameters:
    - artifact_id: The ID of the artifact to update.

    Request Body:
    {
        "title": "Updated Title",
        "description": "Updated Description",
        "artist_id": 2
    }

    Returns:
    A JSON object containing the updated details of the artifact.
    """
    data = request.get_json()
    artifact = Artifact.find_by_id(artifact_id)
    if artifact:
        artifact.title = data.get('title', artifact.title)
        artifact.description = data.get('description', artifact.description)
        artifact.artist_id = data.get('artist_id', artifact.artist_id)
        artifact.save_to_db()
        return jsonify(artifact.json()), 200
    else:
        return jsonify({'message': 'Artifact not found'}), 404

@artifacts_blueprint.route('/artifacts/<int:artifact_id>', methods=['DELETE'])
def delete_artifact(artifact_id):
    """
    Delete an artifact by ID.

    This endpoint allows you to delete the artifact with the specified ID.

    Parameters:
    - artifact_id: The ID of the artifact to delete.

    Returns:
    A JSON object containing a success message if the artifact was deleted successfully.
    """
    artifact = Artifact.find_by_id(artifact_id)
    if artifact:
        artifact.delete_from_db()
        return jsonify({'message': 'Artifact deleted successfully'}), 200
    else:
        return jsonify({'message': 'Artifact not found'}), 404
