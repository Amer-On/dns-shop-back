from fastapi import APIRouter

from internal.dependencies.user import UserServiceDependency
from internal.dto.user import UserDTO


USER_ROUTER = APIRouter()


@USER_ROUTER.get('/users/{user_id}')
async def get_user_handler(user_id: int, service: UserServiceDependency) -> UserDTO:
    return await service.get_user(user_id)


@USER_ROUTER.get('/users/')
async def get_users_handler(service: UserServiceDependency) -> list[UserDTO]:
    return await service.get_users()


@USER_ROUTER.delete('/users/{user_id}')
async def delete_user_handler(user_id: int, service: UserServiceDependency):
    return await service.delete_user(user_id)
