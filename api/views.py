# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Classes, Courses, Students, Instructors
from .serializers import StudentSerializer, InstructorSerializer, CoursesSerializer, ClassesSerializer

'''
Student
'''
class StudentView(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
class SingleStudentView(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer    

'''
Instructor
'''
class InstructorView(ListCreateAPIView):
    queryset = Instructors.objects.all()
    serializer_class = InstructorSerializer
    
class SingleInstructorView(RetrieveUpdateDestroyAPIView):
    queryset = Instructors.objects.all()
    serializer_class = InstructorSerializer  
        
'''
Course
'''       
class CourseView(ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    
class SingleCourseView(RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
'''
Classroom
'''        
class ClassView(ListCreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    
class SingleClassView(RetrieveUpdateDestroyAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer