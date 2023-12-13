from fastapi import APIRouter

from internal.dependencies.user import UserServiceDependency
from internal.dto.auth import CredentialsDTO, RegisterDTO


AUTH_ROUTER = APIRouter()


@AUTH_ROUTER.post('/login')
async def login_handler(request_data: CredentialsDTO, service: UserServiceDependency):
    return await service.login(request_data)


@AUTH_ROUTER.post('/register')
async def register_handler(request_data: RegisterDTO, service: UserServiceDependency):
    return await service.register(request_data)
