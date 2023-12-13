from tortoise import fields
from tortoise.models import Model

from internal.core.types import LessonEnum, SubgroupEnum


class Schedule(Model):
    id = fields.UUIDField(pk=True)
    date = fields.DateField(index=True)
    time = fields.CharField(max_length=30)
    lesson = fields.CharField(max_length=150)
    professor = fields.CharField(max_length=30, null=True)
    type = fields.CharEnumField(LessonEnum)
    subgroup = fields.CharEnumField(SubgroupEnum, null=True)
    auditory = fields.CharField(max_length=30, null=True)
    group = fields.CharField(max_length=30, index=True)

    class Meta:
        unique_together = ('date', 'time', 'lesson', 'group')
