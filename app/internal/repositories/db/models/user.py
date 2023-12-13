from tortoise import fields
from tortoise.models import Model


class User(Model):
    # id: int = fields.IntField(pk=True)
    login: str = fields.CharField(unique=True, max_length=20, description='Email Пользователя')
    password_hash: str = fields.TextField(description='Хэш пароля с солями')
    name: str = fields.CharField(max_length=20, description='Имя пользователя')
    surname: str = fields.CharField(max_length=20, description='Фамилия пользователя')
    patronymic: str = fields.CharField(max_length=20, description='Отчество пользователя')

    class Meta:
        table = 'users'
