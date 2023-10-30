from .models import Course
from .serializers import CoursesSerializer, CourseListSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsSuperuserOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import NotFound
from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=["Criação e listagem de cursos"],
)
class ListCreateCoursesView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]

    serializer_class = CoursesSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CourseListSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            queryset = Course.objects.all()
        else:
            queryset = Course.objects.filter(students=user)

        return queryset


@extend_schema(
    tags=["Listagem, atualização e deleção de cursos por id"],
)
class RetrieveUpdateDestroyCoursesView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]
    serializer_class = CoursesSerializer
    queryset = Course.objects.all()
    lookup_url_kwarg = "course_id"

    def get_object(self):
        course = Course.objects.filter(pk=self.kwargs["course_id"]).first()

        if not course:
            raise NotFound({"detail": "content not found."})

        return course
