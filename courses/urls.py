from django.urls import path
from . import views

urlpatterns = [
    path(
        "courses/",
        views.ListCreateCoursesView.as_view(),
    ),
    path(
        "courses/<uuid:course_id>/",
        views.RetrieveUpdateDestroyCoursesView.as_view()
        ),
]
