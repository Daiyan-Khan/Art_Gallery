from flask import Blueprint, request, jsonify
from models.artist import Artist

artists_blueprint = Blueprint('artists', __name__)

@artists_blueprint.route('/artists', methods=['POST'])
def create_artist():
    """
    Create a new artist.

    This endpoint allows you to create a new artist with the provided details.

    Request Body:
    {
        "name": "Artist Name",
        "bio": "Artist Bio (optional)"
    }

    Returns:
    A JSON object containing the details of the created artist.
    """
    data = request.get_json()
    new_artist = Artist(name=data['name'], bio=data.get('bio'))
    try:
        new_artist.save_to_db()
        return jsonify(new_artist.json()), 201
    except Exception as e:
        return jsonify({'message': 'An error occurred while creating the artist', 'error': str(e)}), 500

@artists_blueprint.route('/artists', methods=['GET'])
def get_all_artists():
    """
    Get all artists.

    This endpoint returns a list of all artists stored in the database.

    Returns:
    A JSON array containing details of all artists.
    """
    try:
        artists = Artist.query.all()
        return jsonify([artist.json() for artist in artists]), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred while retrieving artists', 'error': str(e)}), 500

@artists_blueprint.route('/artists/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    """
    Get an artist by ID.

    This endpoint returns the details of the artist with the specified ID.

    Parameters:
    - artist_id: The ID of the artist to retrieve.

    Returns:
    A JSON object containing the details of the artist.
    """
    try:
        artist = Artist.find_by_id(artist_id)
        if artist:
            return jsonify(artist.json()), 200
        else:
            return jsonify({'message': 'Artist not found'}), 404
    except Exception as e:
        return jsonify({'message': 'An error occurred while retrieving the artist', 'error': str(e)}), 500

@artists_blueprint.route('/artists/<int:artist_id>', methods=['PUT'])
def update_artist(artist_id):
    """
    Update an artist by ID.

    This endpoint allows you to update the details of the artist with the specified ID.

    Parameters:
    - artist_id: The ID of the artist to update.

    Request Body:
    {
        "name": "Updated Artist Name",
        "bio": "Updated Artist Bio (optional)"
    }

    Returns:
    A JSON object containing the updated details of the artist.
    """
    data = request.get_json()
    try:
        artist = Artist.find_by_id(artist_id)
        if artist:
            artist.name = data.get('name', artist.name)
            artist.bio = data.get('bio', artist.bio)
            artist.save_to_db()
            return jsonify(artist.json()), 200
        else:
            return jsonify({'message': 'Artist not found'}), 404
    except Exception as e:
        return jsonify({'message': 'An error occurred while updating the artist', 'error': str(e)}), 500

@artists_blueprint.route('/artists/<int:artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    """
    Delete an artist by ID.

    This endpoint allows you to delete the artist with the specified ID.

    Parameters:
    - artist_id: The ID of the artist to delete.

    Returns:
    A JSON object containing a success message if the artist was deleted successfully.
    """
    try:
        artist = Artist.find_by_id(artist_id)
        if artist:
            artist.delete_from_db()
            return jsonify({'message': 'Artist deleted successfully'}), 200
        else:
            return jsonify({'message': 'Artist not found'}), 404
    except Exception as e:
        return jsonify({'message': 'An error occurred while deleting the artist', 'error': str(e)}), 500
