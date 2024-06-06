from typing import List
from models.user import User

class IUserDataAccess:
    def create_user(self, user: User) -> None:
        raise NotImplementedError

    def get_all_users(self):
        raise NotImplementedError

    def get_user_by_id(self, user_id: int) -> User:
        raise NotImplementedError

    def update_user(self, user: User) -> None:
        raise NotImplementedError

    def delete_user(self, user_id: int) -> bool:
        raise NotImplementedError
