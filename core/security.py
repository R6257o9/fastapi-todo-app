from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import Union, Any
from jose import jwt

from core.config import settings

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)