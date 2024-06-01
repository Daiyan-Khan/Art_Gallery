from flask import Blueprint, jsonify, request
from models.user import User
from utils.database import db

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user.

    This endpoint allows you to create a new user with the provided details.

    Request Body:
    {
        "username": "User Name",
        "email": "user@example.com"
    }

    Returns:
    A JSON object containing the details of the created user.
    """
    data = request.get_json()
    new_user = User(**data)
    new_user.save_to_db()
    return jsonify(new_user.json()), 201

@users_blueprint.route('/users', methods=['GET'])
def get_all_users():
    """
    Get all users.

    This endpoint returns a list of all users stored in the database.

    Returns:
    A JSON array containing details of all users.
    """
    users = User.query.all()
    return jsonify([user.json() for user in users])

@users_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a user by ID.

    This endpoint returns the details of the user with the specified ID.

    Parameters:
    - user_id: The ID of the user to retrieve.

    Returns:
    A JSON object containing the details of the user.
    """
    user = User.query.get_or_404(user_id)
    return jsonify(user.json())

@users_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a user by ID.

    This endpoint allows you to update the details of the user with the specified ID.

    Parameters:
    - user_id: The ID of the user to update.

    Request Body:
    {
        "username": "Updated User Name",
        "email": "updated@example.com"
    }

    Returns:
    A JSON object containing the updated details of the user.
    """
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.save_to_db()
    return jsonify(user.json())

@users_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user by ID.

    This endpoint allows you to delete the user with the specified ID.

    Parameters:
    - user_id: The ID of the user to delete.

    Returns:
    A JSON object containing a success message if the user was deleted successfully.
    """
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})
