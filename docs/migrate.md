# Миграции tortoise (aerich)
## Конфигурация базы данных берется из `local.yaml`
```
POSTGRES_DB: "db"
POSTGRES_USER: "user"
POSTGRES_PASSWORD: "password"
POSTGRES_HOST: "localhost"
POSTGRES_PORT: "5432"
```
## Если первая миграция, прописать в директории с `pyproject.toml`
```
> poetry run aerich init-db
```
## Сделать миграцию, если база данных уже инициализированна через aerich
```
> poetry run aerich migrate
> poetry run aerich upgrade
```