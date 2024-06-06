from flask import Flask, redirect, url_for,jsonify
from models.user import User
from controllers.artists_controller import artists_blueprint
from controllers.artifacts_controller import artifacts_blueprint
from controllers.users_controller import users_blueprint
from persistence import artifacts_repository
from persistence import artists_repository
from persistence import users_repository
from utils.database import Database, db
import config
from flask_login import LoginManager, login_required,FlaskLoginClient


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.init_app(app)
app.config.from_object(config.Config)
# Initialize the database
Database.initialize(app)


login_manager.login_view = 'users.login'  # Redirect to login on unauthorized access

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register the blueprints
app.register_blueprint(artists_blueprint)
app.register_blueprint(artifacts_blueprint)
app.register_blueprint(users_blueprint)

app.config['artifact_repo'] = artifacts_repository.ArtifactRepository()
app.config['artist_repo'] = artists_repository.ArtistRepository()
app.config['user_repo'] = users_repository.UserRepository()
# Create the tables
with app.app_context():
    db.create_all()
app.test_client_class = FlaskLoginClient
# Root route redirecting to /artists
@app.route('/')


def index():
    return redirect(url_for('artists.get_all_artists'))

if __name__ == '__main__':
    app.run(debug=True)
