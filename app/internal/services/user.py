from fastapi.exceptions import HTTPException

from internal.core.auth import encode_access_token
from internal.dto.auth import CredentialsDTO, RegisterDTO
from internal.dto.user import UserDTO
from internal.repositories.db.user import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository

    async def login(self, data: CredentialsDTO) -> str:
        if await self.repository.check_user_credentials(data):
            return encode_access_token(data.login)
        raise HTTPException(status_code=403, detail='Invalid credentials')

    async def register(self, data: RegisterDTO):
        return await self.repository.create(data)

    async def get_user(self, user_id: int) -> UserDTO:
        return await self.repository.get(user_id)

    async def get_users(self) -> tuple[UserDTO]:
        return await self.repository.get_all()

    async def delete_user(self, user_id: int) -> None:
        return await self.repository.delete(user_id)
