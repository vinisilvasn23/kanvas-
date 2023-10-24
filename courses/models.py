from django.db import models
from accounts.models import Account


class CourseStatusEnum(models.TextChoices):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"


class Courses(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    status = models.CharField(
        max_length=20,
        choices=CourseStatusEnum.choices,
        default=CourseStatusEnum.NOT_STARTED
        )
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    instructor = models.ForeignKey(
        Account, on_delete=models.CASCADE,
        related_name="courses"
        )
