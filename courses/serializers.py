from rest_framework import serializers
from .models import Courses
from contents.serializers import ContentSerializer
from students_courses.serializers import StudentCourseSerializer


class CoursesSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)
    students_courses = StudentCourseSerializer(many=True, read_only=True)
    instructor_id = serializers.UUIDField(required=False)

    class Meta:
        model = Courses
        fields = (
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor_id",
            "contents",
            "students_courses",
        )

    def create(self, validated_data):
        instructor = validated_data.get("instructor_id")
        if instructor is None:
            instructor = self.context["request"].user
            validated_data["instructor_id"] = instructor
        return Courses.objects.create(**validated_data)
