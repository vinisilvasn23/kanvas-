from .models import Courses
from .serializers import CoursesSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperuserOrReadOnly
from rest_framework.generics import ListCreateAPIView


class ListCreateCoursesView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperuserOrReadOnly]

    serializer_class = CoursesSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Courses.objects.all()

        if not user.is_superuser:
            queryset = queryset.filter(instructor_id=user.id)

        return queryset
