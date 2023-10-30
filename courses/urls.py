from django.urls import path
from . import views
from contents.views import CreateContentView, ListUpdateDestroyContentView
from students_courses.views import AddStudentToCourseView

urlpatterns = [
    path(
        "courses/",
        views.ListCreateCoursesView.as_view(),
    ),
    path(
        "courses/<uuid:course_id>/",
        views.RetrieveUpdateDestroyCoursesView.as_view()
        ),
    path(
        "courses/<uuid:course_id>/contents/",
        CreateContentView.as_view()
        ),
    path(
        "courses/<uuid:course_id>/contents/<uuid:content_id>/",
        ListUpdateDestroyContentView.as_view()
        ),
    path(
        "courses/<uuid:course_id>/students/",
        AddStudentToCourseView.as_view()
        ),
]
