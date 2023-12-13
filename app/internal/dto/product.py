from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from internal.core.types import ProductCategoryEnum
from internal.repositories.db.models.product import Product


_CreateProductDTOBase = pydantic_model_creator(Product, name='Create product DTO', exclude=('id', 'images'))


class CreateProductDTO(_CreateProductDTOBase):
    images: list[str]


ProductDTO = pydantic_model_creator(Product, name='Product DTO')


class GetProductsInputDTO(BaseModel):
    category: Optional[ProductCategoryEnum] = None
    min_price: Optional[int] = None
    max_price: Optional[int] = None
    search: Optional[str] = None
