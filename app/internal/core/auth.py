from datetime import datetime, timedelta

from fastapi import HTTPException

import config
from jose import JWTError, jwt


def encode_access_token(username: str) -> str:
    expire = datetime.now() + timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {'username': username, 'exp': expire}

    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> dict:
    payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
    return payload


def verify_token(token: str) -> str:
    """Функция для проверки валидности токена.
    При включенном режиме DEBUG пропускает проверку авторизации

    Args:
        token: авторизационный токен доступа

    Returns:
        Имя пользователя
    """
    if config.DEBUG:
        return 'DEBUG'

    if not token:
        raise HTTPException(status_code=401, detail='Token is empty')

    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])

        username = payload.get('username')
        if not username:
            raise HTTPException(status_code=401, detail='Invalid token')

        return username

    except JWTError:
        raise HTTPException(status_code=401, detail='Invalid token')
