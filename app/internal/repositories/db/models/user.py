from tortoise import fields
from tortoise.models import Model


class User(Model):
    login: str = fields.CharField(unique=True, max_length=20, description='Email Пользователя')
    password_hash: str = fields.TextField(description='Хэш пароля с солями')

    class Meta:
        table = 'users'
