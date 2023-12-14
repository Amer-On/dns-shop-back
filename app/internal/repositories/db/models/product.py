from typing import Optional

from tortoise import fields
from tortoise.models import Model

from internal.core.types.category import ProductCategoryEnum


class Product(Model):
    name: str = fields.TextField(description='Наименование товара')
    summary: str = fields.TextField(description='Сводка о товаре')
    description: str = fields.TextField(description='Описание товара')
    price: int = fields.IntField(description='Стоимость товара')
    images: list[str] = fields.JSONField(description='Изображения товаров')
    category: Optional[ProductCategoryEnum] = fields.CharEnumField(ProductCategoryEnum, description='Категория товара', null=True)

    class Meta:
        table = 'products'
