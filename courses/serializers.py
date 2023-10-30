from rest_framework import serializers
from .models import Course
from contents.serializers import ContentSerializer
from students_courses.serializers import StudentSerializer
from accounts.models import Account


class CoursesSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)
    students_courses = StudentSerializer(many=True, read_only=True)
    instructor = serializers.UUIDField(source="instructor_id", required=False)

    class Meta:
        model = Course
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
        instructor_id = validated_data.get("instructor_id")
        if instructor_id:
            instructor = Account.objects.get(id=instructor_id)
            validated_data["instructor"] = instructor
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
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


class StudentCourseSerializer(serializers.ModelSerializer):
    students_courses = StudentSerializer(many=True, read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "students_courses",
        )
