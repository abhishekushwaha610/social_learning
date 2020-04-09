from django.shortcuts import render,redirect
from .forms import Video_upload_form
from .models import Video

from django.contrib import messages

def videos(request,slug):
    video = Video.objects.filter(slug=slug)[0]    

    return render(request,"video.html",{"video":video})


def upload_video(request):
    if request.method == "POST":
        form = Video_upload_form(request.POST,request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect("video",video.slug)
        else:
            messages.error(request,"Please upload correct fields")
            return render(request,"upload_video.html",{"form":form})
    form = Video_upload_form()
    return render(request,"upload_video.html",{"form":form})

def edit_video(request,slug):
    video = Video.objects.filter(slug=slug)[0]
    if request.method == "POST":
        form = Video_upload_form(request.POST,request.FILES,instance=video)
        if form.is_valid():
            video = form.save(commit=True)
            return redirect("video",video.slug)
        else:
            messages.error(request,"Please upload correct fields")
            return render(request,"upload_video.html",{"form":form})
    print(video)
    form = Video_upload_form(instance=video)
    return render(request,"upload_video.html",{"form":form})

def delete_video(request,slug):
    video = Video.objects.filter(slug=slug)[0]
    video.delete()
    return redirect("upload")