from django.db import models
from courses.models import Courses


class Content(models.Model):
    name = models.CharField(max_length=150, null=False)
    content = models.TextField(null=False)
    video_url = models.CharField(max_length=200)
    course = models.ForeignKey(
        Courses, null=False,
        on_delete=models.CASCADE,
        related_name="contents"
        )
