from models.user import User
from utils.database import db
from persistence.IUserDataAccess import IUserDataAccess
from flask_login import LoginManager, login_user, logout_user, current_user

login_manager = LoginManager()

class UserRepository(IUserDataAccess):
    def create_user(self, user: User):
        db.session.add(user)
        db.session.commit()

    def get_all_users(self):
        return User.query.all()

    def get_user_by_id(self, user_id: int):
        return User.query.get(user_id)

    def update_user(self, user: User):
        db.session.commit()

    def delete_user(self, user_id: int):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
