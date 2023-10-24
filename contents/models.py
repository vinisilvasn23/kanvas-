from django.db import models
from uuid import uuid4
from courses.models import Courses


class Content(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=150, null=False)
    content = models.TextField(null=False)
    video_url = models.CharField(max_length=200)
    course = models.ForeignKey(
        Courses, null=False,
        on_delete=models.CASCADE,
        related_name="contents"
        )
