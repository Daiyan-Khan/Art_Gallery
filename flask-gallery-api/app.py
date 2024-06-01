from flask import Flask, redirect, url_for
from controllers.artists_controller import artists_blueprint
from controllers.artifacts_controller import artifacts_blueprint
from controllers.users_controller import users_blueprint
from utils.database import Database, db

app = Flask(__name__)

# Initialize the database
Database.initialize(app)

# Register the blueprints
app.register_blueprint(artists_blueprint)
app.register_blueprint(artifacts_blueprint)
app.register_blueprint(users_blueprint)

# Create the tables
with app.app_context():
    db.create_all()

# Root route redirecting to /artists
@app.route('/')
def index():
    return redirect(url_for('artists.get_all_artists'))

if __name__ == '__main__':
    app.run(debug=True)
