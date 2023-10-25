from django.db import models
from uuid import uuid4
from accounts.models import Account
from courses.models import Course


class StudentCourseStatusEnum(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"


class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    status = models.CharField(
        max_length=20,
        choices=StudentCourseStatusEnum.choices,
        default=StudentCourseStatusEnum.PENDING
        )
    student = models.ForeignKey(
        Account, null=False,
        on_delete=models.CASCADE,
        related_name="students_courses"
        )
    course = models.ForeignKey(
        Course, null=False,
        on_delete=models.CASCADE,
        related_name="students_courses"
        )
