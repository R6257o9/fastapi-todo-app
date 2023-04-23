from core.security import get_password
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