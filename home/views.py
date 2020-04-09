from django.shortcuts import render,redirect,HttpResponse
from home.models import Video
import PIL
from  django.db.models import Q

# Create your views here.
def home(request):
    video = Video.objects.all()
    param ={
        "videos": video,
    }

    return render(request, "home.html")    

def search(request):
    if request.method=='POST':
        search1 = request.POST["search"]
        if search1:
            match = Video.objects.filter(Q(title__icontains=search1) | Q(description__icontains=search1))
            if match:
                return render(request,'search.html',{'videos':match})
            else:
                return HttpResponse('data no found')    
        else:
            return redirect("/")
    else:
        return redirect('/')         
    # return render(request,'search.html')
