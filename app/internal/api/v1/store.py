from typing import Annotated

from fastapi import APIRouter, Depends

from internal.dependencies.product import ProductRepositoryDependency
from internal.dto.product import CreateProductDTO, GetProductsInputDTO, ProductDTO


STORE_ROUTER = APIRouter(tags=['Online shop'])


@STORE_ROUTER.get('/products/{product_id}/')
async def get_product_handler(product_id: int, repository: ProductRepositoryDependency) -> ProductDTO:
    return await repository.get(product_id)


@STORE_ROUTER.get('/products/')
async def get_products_handler(repository: ProductRepositoryDependency, data: Annotated[GetProductsInputDTO, Depends()]) -> list[ProductDTO]:
    return await repository.get_many(**data.model_dump(exclude_none=True))


@STORE_ROUTER.post('/products/')
async def create_product_handler(data: CreateProductDTO, repository: ProductRepositoryDependency) -> ProductDTO:
    return await repository.add(data)


@STORE_ROUTER.delete('/products/{product_id}/')
async def delete_product_handler(product_id: int, repository: ProductRepositoryDependency):
    return await repository.delete(product_id)
