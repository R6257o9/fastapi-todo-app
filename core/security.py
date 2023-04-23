from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import Union, Any
from jose import jwt

from core.config import settings

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Estas funciones crean JSON Web Tokens (JWT) con fines de autenticación. 


# Función que crea un token JWT que caduca después de un período de tiempo determinado, 
# especificado por el parámetro  expires_delta o el valor predeterminado en la configuración de la app
# subject es el valor que se almacenará en el campo "sub" (asunto) de la carga útil de JWT
# expires_delta es la duración de la validez del token. Si no se proporciona este valor, se utiliza el tiempo de caducidad predeterminado especificado en la configuración de la app
def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.ALGORITHM)    
    return encoded_jwt

# Función crea un token JWT similar, pero con una clave secreta diferente, que se usa para actualizar el token de acceso.
def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_REFRESH_SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt

def get_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)
  