from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from courses.models import Course
from .models import StudentCourse
from accounts.models import Account
from courses.serializers import StudentCourseSerializer
from .permissions import IsSuperuserPermission
from rest_framework.exceptions import NotFound
from .exceptions import NoActiveAccountsError


class AddStudentToCourseView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserPermission]
    serializer_class = StudentCourseSerializer
    lookup_url_kwarg = "course_id"

    def get_object(self):
        course = Course.objects.filter(pk=self.kwargs["course_id"]).first()
        if not course:
            raise NotFound({"detail": "course not found."})

        student_emails = self.request.data.get("students_courses")
        error_emails = []

        for email_data in student_emails:
            email = email_data.get("student_email")
            if email:
                account = Account.objects.filter(email=email).first()
                if account:
                    student_course = StudentCourse.objects.create(
                        student=account, course=course
                        )
                    course.students_courses.add(student_course)
                else:
                    error_emails.append(email)

        if error_emails:
            error_message = f"No active accounts was found: {', '.join(error_emails)}."
            raise NoActiveAccountsError({"detail": error_message})

        return course
