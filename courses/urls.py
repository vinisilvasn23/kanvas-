from django.urls import path
from . import views

urlpatterns = [
    path(
        "courses/",
        views.ListCreateCoursesView.as_view(),
    ),
]
