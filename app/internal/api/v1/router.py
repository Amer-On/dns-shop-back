from fastapi import APIRouter

from .auth import AUTH_ROUTER
from .status import STATUS_ROUTER
from .store import STORE_ROUTER
from .user import USER_ROUTER


V1_ROUTER = APIRouter(prefix='/v1')
V1_ROUTER.include_router(STATUS_ROUTER)
V1_ROUTER.include_router(AUTH_ROUTER)
V1_ROUTER.include_router(USER_ROUTER)
V1_ROUTER.include_router(STORE_ROUTER)
