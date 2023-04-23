from typing import Optional

from core.security import get_password, verify_password
from models.user_model import User
from schemas.user_schema import UserAuth


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=get_password(user.password)
        )
        # si los datos estan Ok se guardan en la db
        await user_in.save()
        return user_in

    @staticmethod
    async def authenticate(email: str, password:str) -> Optional[User]:
        user = UserService.get_user_by_email(email = email)
        if not user:
            return
        if not verify_password(password=password, hashed_pass=User.hashed_password):
            return None

        return user
            

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email == email) 
        return user   



