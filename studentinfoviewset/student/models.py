from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=10)
    rollno=models.IntegerField()
    branch=models.CharField(max_length=10)
