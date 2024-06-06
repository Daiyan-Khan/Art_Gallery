from flask import Blueprint, request, render_template, redirect, url_for, flash,current_app,jsonify
from flask_login import login_user, logout_user, login_required, current_user
from models.user import User
from persistence.IUserDataAccess import IUserDataAccess

users_blueprint = Blueprint('users', __name__)

def get_user_repository() -> IUserDataAccess:
    return current_app.config['user_repo']

@users_blueprint.route('/users', methods=['GET'])
def get_all_users():
    repo = get_user_repository()
    users = repo.get_all_users()
    return jsonify([user.json() for user in users]), 200

@users_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    if current_user.id != user_id:
        # Unauthorized to delete other users
        return jsonify({'message': 'Unauthorized'}), 403

    repo = get_user_repository()
    user = repo.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Perform the deletion
    repo.delete_user(user_id)
    return jsonify({'message': 'User deleted successfully'}), 200

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')

    return render_template('login.html')

@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        repo = get_user_repository()
        
        if User.query.filter_by(username=username).first() is not None:
            flash('Username already exists')
            return redirect(url_for('users.register'))
        
        if User.query.filter_by(email=email).first() is not None:
            flash('Email already registered')
            return redirect(url_for('users.register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        repo.create_user(new_user)

        flash('Registration successful! Please log in.')
        return redirect(url_for('users.login'))

    return render_template('register.html')
