from tortoise import fields
from tortoise.models import Model


class Feedback(Model):
    email: str = fields.CharField(max_length=30, description='Email клиента')
    comment: str = fields.TextField(description='Комментарий клиента')

    class Meta:
        table = 'feedbacks'
