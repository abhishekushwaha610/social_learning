from django import forms
from .models import Video
class Video_upload_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title","description","video_url"]
        widgets = {
            "title" : forms.TextInput(attrs={"class":"form-control border-primary","placeholder":"Name of Video"}),
            "description" : forms.Textarea(attrs={"class":"form-control border-primary","rows":4,"placeholder":"About the Video"}),
            'video_url' : forms.TextInput(attrs={'class':"form-control border-primary","placeholder":"Youtube url of The video"})
        }