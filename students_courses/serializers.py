from rest_framework import serializers
from .models import StudentCourse


class StudentSerializer(serializers.ModelSerializer):
    student_id = serializers.UUIDField(source="student.id", required=False)
    student_username = serializers.CharField(source="student.username", required=False)
    student_email = serializers.EmailField(source="student.email", read_only=True)

    class Meta:
        model = StudentCourse
        fields = (
            "id",
            "student_id",
            "student_username",
            "student_email",
            "status",
        )
