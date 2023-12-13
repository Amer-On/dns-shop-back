from bcrypt import gensalt, hashpw
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password: str) -> str:
    return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')


def check_password(password: str, password_hash: str):
    return pwd_context.verify(password, password_hash)
