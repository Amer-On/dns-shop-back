from tortoise.contrib.pydantic import pydantic_model_creator

from internal.repositories.db.models.feedback import Feedback


FeedbackDTO = pydantic_model_creator(
    Feedback,
    name='Feedback DTO',
)


CreateFeedbackDTO = pydantic_model_creator(Feedback, name='Create Feedback DTO', exclude=('id',))
