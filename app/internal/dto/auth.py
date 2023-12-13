from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from internal.repositories.db.models.user import User


class CredentialsDTO(BaseModel):
    login: str
    password: str


_RegisterDTO_Base = pydantic_model_creator(User, exclude=('password_hash', 'id'), name='Register DTO')


class RegisterDTO(_RegisterDTO_Base):
    password: str
