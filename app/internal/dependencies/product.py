from typing import Annotated

from fastapi import Depends

from internal.repositories.db.product import ProductRepository


ProductRepositoryDependency = Annotated[ProductRepository, Depends(ProductRepository)]
