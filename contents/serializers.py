from rest_framework import serializers
from .models import Content


class ContentSerializer(serializers.ModelSerializer):
    course = serializers.UUIDField(
        source="course_id",
        required=False,
        write_only=True
        )

    class Meta:
        model = Content
        fields = '__all__'
