from django.shortcuts import render,redirect ,get_object_or_404
from .forms import Video_upload_form,Comment_form
from .models import Video,Comment , Playlist
from django.views.generic import ListView
from django.contrib import messages

def videos(request,slug):
    video = Video.objects.filter(slug=slug)[0]  
    comment_form = Comment_form()
    return render(request,"video.html",{"video":video,"comment_form":comment_form})


def upload_video(request):
    if request.method == "POST":
        form = Video_upload_form(request.POST,request.FILES)
        if form.is_valid():
            url = form.cleaned_data["video_url"].replace("watch?v=","embed/")
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            video.video_url = url
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
            url = form.cleaned_data["video_url"].replace("watch?v=","embed/")
            print(url)
            video = form.save(commit=True)
            video.video_url = url
            video.save()
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

def comment_save(request,video_id,comment_id):
    if request.method == "POST":
        video = Video.objects.get(id=video_id)
        form = Comment_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.video = video
            comment.save()
            if comment_id:
                comment.parent = Comment.objects.get(id = comment_id)
                comment.save()    
            return redirect("video",video.slug)

def comment_delete(request,comment_id):
    comment = Comment.objects.get(id = comment_id)
    comment.delete()
    url = request.GET.get("redirect",None)
    if url:
        return redirect(url)
    return redirect("/")

class AllList(ListView):
    template_name = "All_videos.html"
    context_object_name = 'videos'
    paginate_by = 10
    def get_queryset(self):
        # self.language = get_object_or_404(ProjectDetail, language=self.kwargs['catagory'])
        catagory = self.request.GET.get("catagory",None)
        
        if catagory:
            return Video.objects.filter(catagory=catagory)
        # elif query=="search":
        #     word = self.request.GET["fields"]
        #     # print(word)
        #     return ProjectDetail.objects.filter(Q(headline__contains=word) | Q(language__contains = word))

        return Video.objects.all().order_by("-creation_time")

def all_videos(request):
    videos = Video.objects.all()
    return render(request,"All_videos.html",{"videos":videos})

def add_to_playlist(request,slug):
    newvideo = get_object_or_404(Video , slug=slug)
    # newvideo = Video.objects.create(slug = myslug)
    if not request.user.playlist_set.all():
        
        newplaylist = Playlist.objects.create( user = request.user )
        newplaylist.video.add(newvideo)
        # newplaylist.save()

    return redirect("video" ,slug)
    