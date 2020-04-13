from django.shortcuts import render,redirect ,reverse
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.
VIDEO_CATEGORIES = (
    ('cse','Computer Science'),
    ('phs','Philosphy'),
    ('phy','Physics'),
    ('mda', 'Media'),
    ('mth', 'Methametics'),
    ('art', 'Arts'),
    ('chy', 'Chemistry'),
    ('bio', 'Biology'),
)
def file_upload_path(instance,filename):
    return "notes/%s-%s" %(instance.slug,filename)

class Video(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=300)
    creation_time = models.DateTimeField(default=str(datetime.now())) 
    video_url = models.URLField()
    catagory = models.CharField(choices=VIDEO_CATEGORIES,max_length=3)
    notes = models.FileField(upload_to=file_upload_path,null=True,blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_add_to_playlist_url(self):
        return reverse("add-to-playlist" , kwargs={
            'slug':self.slug
            })

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    video = models.ForeignKey(Video,on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies',on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    creation_time = models.DateTimeField(default=str(datetime.now()))
    
    def __str__(self):
        return str(self.user)

class Playlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    video = models.ManyToManyField(Video)
