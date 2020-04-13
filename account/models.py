from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_image_name(instance, filename): 
    return 'profile_img/user_{0}.png'.format(instance.student.id) 

def get_image_name1(instance, filename): 
    return 'profile_img/user_{0}.png'.format(instance.teacher.id) 

class Student(models.Model):
    student = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    institute = models.CharField(max_length=50)
    image = models.FileField(upload_to=get_image_name,default='profile_img/user.png',null=True)
    interests = models.CharField(max_length=50)
    def __str__(self):
        return str(self.student)

class Teacher(models.Model):
    teacher = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.FileField(upload_to = get_image_name1,default='profile_img/user.png',null=True)
    institute = models.CharField(max_length=50)
    qualifications  = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    work_experience = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.teacher)
    