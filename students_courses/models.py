from django.db import models
from accounts.models import Account
from courses.models import Courses


class StudentCourseStatusEnum(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"


class StudentCourse(models.Model):
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
        Courses, null=False,
        on_delete=models.CASCADE,
        related_name="students_courses"
        )
