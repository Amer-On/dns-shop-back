from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist, IntegrityError

from internal.core.utils import check_password, hash_password
from internal.dto.auth import CredentialsDTO, RegisterDTO
from internal.dto.user import UserDTO
from internal.repositories.db.base import BaseRepository
from internal.repositories.db.models import User


class UserRepository(BaseRepository):
    model = User

    async def get_all(self) -> tuple[UserDTO]:
        users = await self.model.all()
        return tuple(UserDTO.from_orm(user) for user in users)

    async def get(self, user_id: int) -> User:
        try:
            user = await self.model.get(id=user_id)
            return UserDTO.from_orm(user)
        except DoesNotExist as e:
            raise HTTPException(status_code=404, detail='User does not exist') from e

    async def create(self, user_data: RegisterDTO) -> UserDTO:
        try:
            user = await self.model.create(**user_data.model_dump(exclude=('password',)), password_hash=hash_password(user_data.password))
        except IntegrityError as e:
            raise HTTPException(status_code=409, detail='User already exists') from e
        return UserDTO.from_orm(user)

    async def check_user_credentials(self, credentials: CredentialsDTO) -> bool:
        user = await self.model.get(login=credentials.login)
        return check_password(credentials.password, user.password_hash)

    async def delete(self, user_id: int) -> None:
        try:
            await self.model.filter(id=user_id).delete()
        except DoesNotExist as e:
            raise HTTPException(status_code=404, detail='User does not exist') from e
