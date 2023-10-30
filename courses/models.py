from django.db import models
from uuid import uuid4
from accounts.models import Account


class CourseStatusEnum(models.TextChoices):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"


class Course(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100, unique=True, null=False)
    status = models.CharField(
        max_length=11,
        choices=CourseStatusEnum.choices,
        default=CourseStatusEnum.NOT_STARTED,
    )
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    instructor = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,
        blank=True
    )
    students = models.ManyToManyField(
        Account,
        related_name="my_courses"
    )
