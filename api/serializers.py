from django.db import models
from api.models import Classes, Courses, Instructors, Students
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('first_name','last_name','email','phone')

    
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructors
        fields = ('first_name','last_name','email','phone')
    
    
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('name','description')
    
class ClassesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classes
        fields = ('student_id','instructor_id','course_id','start_date','end_date')