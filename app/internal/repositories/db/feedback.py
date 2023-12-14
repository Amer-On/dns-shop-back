from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist, IntegrityError

from internal.dto.feedback import FeedbackDTO
from internal.repositories.db.models.feedback import Feedback


class FeedbackRepository:
    model = Feedback

    async def get_many(self) -> tuple[FeedbackDTO]:
        products = await self.model.all()
        return tuple(FeedbackDTO.from_orm(product) for product in products)

    async def get(self, feedback_id: int) -> FeedbackDTO:
        try:
            product = await self.model.get(id=feedback_id)
            return FeedbackDTO.from_orm(product)
        except DoesNotExist as e:
            raise HTTPException(status_code=404, detail='Feedback does not exist') from e

    async def add(self, email: str, comment: str) -> FeedbackDTO:
        try:
            product = await self.model.create(email=email, comment=comment)
        except IntegrityError as e:
            raise HTTPException(status_code=409, detail='Feedback already exists') from e

        return FeedbackDTO.from_orm(product)

    async def delete(self, feedback_id: int):
        try:
            await self.model.filter(id=feedback_id).delete()
        except DoesNotExist as e:
            raise HTTPException(status_code=404, detail='Feedback does not exist') from e
