from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist, IntegrityError
from tortoise.expressions import Q

from internal.core.types import Empty, ProductCategoryEnum
from internal.dto.product import CreateProductDTO, ProductDTO
from internal.repositories.db.models import Product


class ProductRepository:
    model = Product

    async def get_many(self, category: ProductCategoryEnum = Empty, min_price: int = Empty, max_price: int = Empty, search: str = Empty) -> tuple[ProductDTO]:
        filters = []
        if category is not Empty:
            filters.append(Q(category=category))
        if min_price is not Empty:
            filters.append(Q(price__gte=min_price))
        if max_price is not Empty:
            filters.append(Q(price__lte=max_price))
        if search is not Empty:
            filters.append(Q(name__icontains=search, summary__icontains=search, description__icontains=search, join_type='OR'))

        products = await self.model.filter(*filters).all()
        return tuple(ProductDTO.from_orm(product) for product in products)

    async def get(self, product_id: int) -> ProductDTO:
        try:
            product = await self.model.get(id=product_id)
            return ProductDTO.from_orm(product)
        except DoesNotExist as e:
            raise HTTPException(status_code=404, detail='Product does not exist') from e

    async def add(self, data: CreateProductDTO) -> ProductDTO:
        try:
            product = await self.model.create(**data.model_dump())
        except IntegrityError as e:
            raise HTTPException(status_code=409, detail='User already exists') from e

        return ProductDTO.from_orm(product)

    async def delete(self, product_id: int):
        try:
            await self.model.filter(id=product_id).delete()
        except DoesNotExist as e:
            raise HTTPException(status_code=404, detail='Product does not exist') from e
