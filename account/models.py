from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    student = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    image = models.FileField()
    about = models.TextField()
    # interests = models.ManyToManyField(Subject, related_name='interested_students')


    

# class Teacher(models.Model):
    