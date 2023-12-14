from typing import Annotated

from fastapi import APIRouter, Depends

from internal.dependencies.product import FeedbackRepositoryDependency, ProductRepositoryDependency
from internal.dto.feedback import CreateFeedbackDTO, FeedbackDTO
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


@STORE_ROUTER.get('/feedbacks/{feedback_id}')
async def get_feedback_handler(feedback_id: int, repository: FeedbackRepositoryDependency) -> FeedbackDTO:
    return await repository.get(feedback_id)


@STORE_ROUTER.get('/feedbacks/')
async def get_feedbacks_handler(repository: FeedbackRepositoryDependency) -> list[FeedbackDTO]:
    return await repository.get_many()


@STORE_ROUTER.post('/feedbacks')
async def create_feedback_handler(data: CreateFeedbackDTO, repository: FeedbackRepositoryDependency) -> FeedbackDTO:
    return await repository.add(**data.model_dump())
