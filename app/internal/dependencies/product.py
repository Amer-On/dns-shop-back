from typing import Annotated

from fastapi import Depends

from internal.repositories.db.feedback import FeedbackRepository
from internal.repositories.db.product import ProductRepository


ProductRepositoryDependency = Annotated[ProductRepository, Depends(ProductRepository)]

FeedbackRepositoryDependency = Annotated[FeedbackRepository, Depends(FeedbackRepository)]
