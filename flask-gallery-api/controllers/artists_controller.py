from flask import Blueprint, jsonify, request, current_app
from models.artist import Artist
from persistence.IArtistDataAccess import IArtistDataAccess

artists_blueprint = Blueprint('artists', __name__)

def get_artist_repository() -> IArtistDataAccess:
    return current_app.config['artist_repo']

@artists_blueprint.route('/artists', methods=['POST'])
def create_artist():
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
    repo = get_artist_repository()
    artists = repo.get_all_artists()
    return jsonify([artist.json() for artist in artists]), 200

@artists_blueprint.route('/artists/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    repo = get_artist_repository()
    artist = repo.get_artist_by_id(artist_id)
    if artist:
        return jsonify(artist.json()), 200
    else:
        return jsonify({'message': 'Artist not found'}), 404

@artists_blueprint.route('/artists/<int:artist_id>', methods=['PUT'])
def update_artist(artist_id):
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
    repo = get_artist_repository()
    if repo.delete_artist(artist_id):
        return jsonify({'message': 'Artist deleted successfully'}), 200
    else:
        return jsonify({'message': 'Artist not found'}), 404
