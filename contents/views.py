from .models import Content
from courses.models import Course
from .serializers import ContentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import (
    AccessContentPermission,
    IsSuperuserPermission,
    check_content_permission
    )
from rest_framework.exceptions import NotFound


class CreateContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserPermission]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        course_id = self.kwargs.get("course_id")
        course = Course.objects.get(pk=course_id)
        serializer.save(course=course)


class ListUpdateDestroyContentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AccessContentPermission]
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    def get_queryset(self):
        course_id = self.kwargs["course_id"]
        content_id = self.kwargs["content_id"]

        try:
            course = Course.objects.get(pk=course_id)
            content = Content.objects.filter(id=content_id, course=course)

            if not content:
                raise NotFound({"detail": "content not found."})

            if self.request.method == 'GET':
                if check_content_permission(course, self.request.user):
                    return content
                else:
                    return Content.objects.none()

            else:
                return content

        except Course.DoesNotExist:
            raise NotFound({"detail": "course not found."})
