from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import ClassView, SingleClassView, SingleCourseView, SingleInstructorView, StudentView, SingleStudentView, InstructorView, CourseView
from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path

app_name = "api"

urlpatterns = [
    path('students/',StudentView.as_view()),
    path('students/<int:pk>',SingleStudentView.as_view()),
    
    path('instructors/',InstructorView.as_view()),
    path('instructors/<int:pk>',SingleInstructorView.as_view()),
    
    path('courses/',CourseView.as_view()),
    path('courses/<int:pk>',SingleCourseView.as_view()),

    path('classes/',ClassView.as_view()),
    path('classes/<int:pk>',SingleClassView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
