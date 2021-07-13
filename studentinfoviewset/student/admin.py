from django.contrib import admin

# Register your models here.
from student.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','rollno','branch']
admin.site.register(Student,StudentAdmin)
