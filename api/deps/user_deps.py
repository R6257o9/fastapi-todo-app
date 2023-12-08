from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from datetime import datetime
from jose import jwt

from core.config import settings
from models.user_model import User
from schemas.auth_schema import TokenPayload
from services.user_service import UserService

reuseable_oauth = OAuth2PasswordBearer(
    # URL a la que la primera API llamara desde el Front para obtener el token de acceso y actualización
    tokenUrl=f"{settings.API_V1_STR}/auth/login",
    scheme_name="JWT"
)

# Valida el token de autenticación enviado en la solicitud. 
async def get_current_user(token: str = Depends(reuseable_oauth)) -> User:
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        
        # Se verifica si el token ha expirado utilizando la información de tiempo de expiración en el token y la hora actual. Si el token ha expirado, se lanza una excepción HTTP 401
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    # Obtener el objeto de usuario correspondiente al ID de usuario almacenado en el token. Si el usuario no se encuentra en la base de datos, se lanza una excepción HTTP 404.
    user = await UserService.get_user_by_id(token_data.sub)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    # Devuelve el objeto de usuario si se han validado correctamente el token y el usuario
    return user