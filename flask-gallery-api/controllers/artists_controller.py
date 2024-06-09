from flask import Blueprint, jsonify, request, current_app
from models.artist import Artist
from persistence.IArtistDataAccess import IArtistDataAccess

artists_blueprint = Blueprint('artists', __name__)

def get_artist_repository() -> IArtistDataAccess:
    """
    Retrieves the artist repository from the current Flask application configuration.

    Returns:
        IArtistDataAccess: The artist repository implementation.
    """
    return current_app.config['artist_repo']

@artists_blueprint.route('/artists', methods=['POST'])
def create_artist():
    """
    Endpoint for creating a new artist.

    Request Body:
        {
            "name": "string",  # The name of the artist (required)
            "bio": "string"    # Optional biography of the artist
        }

    Returns:
        JSON: The created artist object with status code 201.
    """
    data = request.get_json()
    if not data or not 'name' in data:
        return jsonify({'message': 'Invalid input'}), 400
    
    new_artist = Artist(
        name=data['name'],
        bio=data.get('bio', '')
    )

    repo = get_artist_repository()
    repo.create_artist(new_artist)

    return jsonify(new_artist.json()), 201

@artists_blueprint.route('/artists', methods=['GET'])
def get_all_artists():
    """
    Endpoint for retrieving all artists.

    Returns:
        JSON: List of artist objects with status code 200.
    """
    repo = get_artist_repository()
    artists = repo.get_all_artists()
    return jsonify([artist.json() for artist in artists]), 200

@artists_blueprint.route('/artists/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    """
    Endpoint for retrieving a specific artist by ID.

    Args:
        artist_id (int): The ID of the artist to retrieve.

    Returns:
        JSON: The artist object with status code 200 if found, or a message with status code 404 if not found.
    """
    repo = get_artist_repository()
    artist = repo.get_artist_by_id(artist_id)
    if artist:
        return jsonify(artist.json()), 200
    else:
        return jsonify({'message': 'Artist not found'}), 404

@artists_blueprint.route('/artists/<int:artist_id>', methods=['PUT'])
def update_artist(artist_id):
    """
    Endpoint for updating an existing artist by ID.

    Args:
        artist_id (int): The ID of the artist to update.

    Request Body:
        {
            "name": "string",  # The updated name of the artist
            "bio": "string"    # Optional updated biography of the artist
        }

    Returns:
        JSON: The updated artist object with status code 200 if found, or a message with status code 404 if not found.
    """
    data = request.get_json()
    repo = get_artist_repository()
    artist = repo.get_artist_by_id(artist_id)
    if artist:
        artist.name = data.get('name', artist.name)
        artist.bio = data.get('bio', artist.bio)
        repo.update_artist(artist)
        return jsonify(artist.json()), 200
    else:
        return jsonify({'message': 'Artist not found'}), 404

@artists_blueprint.route('/artists/<int:artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    """
    Endpoint for deleting an artist by ID.

    Args:
        artist_id (int): The ID of the artist to delete.

    Returns:
        JSON: A message indicating success or failure of the deletion operation with status code 200 if successful,
              or a message with status code 404 if the artist was not found.
    """
    repo = get_artist_repository()
    if repo.delete_artist(artist_id):
        return jsonify({'message': 'Artist deleted successfully'}), 200
    else:
        return jsonify({'message': 'Artist not found'}), 404
