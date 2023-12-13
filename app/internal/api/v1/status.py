from fastapi import APIRouter

from internal.dependencies.user import AuthorizationDependency


STATUS_ROUTER = APIRouter()


@STATUS_ROUTER.get('/status')
async def v1_status_router(username: AuthorizationDependency):
    return {'message': f'hey there, {username}'}
