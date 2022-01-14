from django.contrib import admin
from .models import Students, Instructors, Courses, Classes
# Register your models here.
admin.site.register(Students)
admin.site.register(Instructors)
admin.site.register(Courses)
admin.site.register(Classes)