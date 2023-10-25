from .models import Course
from .serializers import CoursesSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperuserOrReadOnly, IsSuperUserOrUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import NotFound


class ListCreateCoursesView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperuserOrReadOnly]

    serializer_class = CoursesSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Course.objects.all()

        if not user.is_superuser:
            queryset = queryset.filter(instructor_id=user.id)

        return queryset


class RetrieveUpdateDestroyCoursesView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrUser]
    serializer_class = CoursesSerializer
    queryset = Course.objects.all()
    lookup_url_kwarg = "course_id"

    def get_object(self):
        course = Course.objects.filter(pk=self.kwargs["course_id"]).first()

        if not course:
            raise NotFound({"detail": "course not found."})

        return course
