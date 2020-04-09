from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.
class Video(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    slug = models.SlugField(null = False)
    description = models.TextField(max_length=300)
    creation_time = models.DateTimeField(default=datetime.now() , blank=False, null=False) 
    video_url = models.URLField()
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    video = models.ForeignKey(Video,on_delete=models.CASCADE)
    # reply = models.ForeignKey(super(),on_delete=models.CASCADE,null=True)
    description = models.TextField(max_length=300)
    creation_time = models.DateTimeField(default=datetime.now() , blank=False, null=False) 
    
    def __str__(self):
        return str(self.user)