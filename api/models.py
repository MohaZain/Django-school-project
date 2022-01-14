from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    def __str__(self):
        return self.first_name
    
class Instructors(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    def __str__(self):
        return self.first_name
    
class Courses(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class Classes(models.Model):
    student_id = models.ForeignKey('Students', on_delete=models.DO_NOTHING)
    instructor_id = models.ForeignKey('Instructors', on_delete=models.DO_NOTHING)
    course_id = models.ForeignKey('Courses', on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return str(self.id)