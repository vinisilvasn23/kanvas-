from rest_framework import serializers
from .models import Courses
from contents.serializers import ContentSerializer
from students_courses.serializers import StudentCourseSerializer
from accounts.models import Account


class CoursesSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)
    students_courses = StudentCourseSerializer(many=True, read_only=True)
    instructor = serializers.UUIDField(source="instructor_id", required=False)

    class Meta:
        model = Courses
        fields = (
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        )

    def create(self, validated_data):
        instructor_id = validated_data.get("instructor")
        if instructor_id is None:
            instructor = self.context["request"].user
        else:
            instructor = Account.objects.get(id=instructor_id)
        validated_data["instructor"] = instructor
        return Courses.objects.create(**validated_data)
