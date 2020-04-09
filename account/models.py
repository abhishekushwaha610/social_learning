from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_image_name(instance, filename): 
    return 'profile_img/user_{0}.png'.format(instance.student.id) 

class Student(models.Model):
    student = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    institute = models.CharField(max_length=20)
    image = models.FileField(upload_to=get_image_name,default='profile_img/user.png')
    interests = models.CharField(max_length=20)
    def __str__(self):
        return str(self.student)

class Teacher(models.Model):
    teacher = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.FileField(upload_to = get_image_name)
    institute = models.CharField(max_length=20)
    qualifications  = models.CharField(max_length=10)
    status = models.CharField(max_length=10)

    def __str__(self):
        return str(self.teacher)
    