from tortoise.contrib.pydantic import pydantic_model_creator

from internal.repositories.db.models import User


UserDTO = pydantic_model_creator(User, name='User DTO', exclude=('password_hash',))
