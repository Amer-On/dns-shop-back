from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from internal.core.auth import verify_token
from internal.repositories.db.user import UserRepository
from internal.services.user import UserService


def create_auth_service(repo: UserRepository = Depends(UserRepository)):
    return UserService(repo)


UserServiceDependency = Annotated[UserService, Depends(create_auth_service)]


Oauth2SchemeDependency = Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl='token', auto_error=False))]


def create_verify_token(token: Oauth2SchemeDependency):
    return verify_token(token)


AuthorizationDependency = Annotated[str, Depends(create_verify_token)]
