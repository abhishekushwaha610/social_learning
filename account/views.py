from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth 
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db.models import Q
from .forms import Student_form,Teacher_form
from django.core.mail import send_mail

class EmailorUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None,**kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


def login(request):
    if request.method == "POST":
        email_or_username = request.POST["email_or_username"]
        password = request.POST["password"]
        user = auth.authenticate(username = email_or_username,password=password)
        if user is None:
            messages.error(request,"User has already Exist !")
            return HttpResponse("already Exist!")
        else:
            auth.login(request,user)
            messages.success(request,"Welcome!")
            return redirect("/")
    return render(request,"login.html")

def signup(request,type):
    
    if request.method == "POST":
        if type == "teach":
            form = Teacher_form(request.POST,request.FILES)
        else:
            form = Student_form(request.POST,request.FILES)
        
        if form.is_valid():
            fname = request.POST["fname"]
            lname = request.POST["lname"]
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            cpassword = request.POST["cpassword"]
            
            if password != cpassword:
                messages.error(request,"Password does not match!")
                return render(request,"signup.html",{"form": Student_form()})
            else:
                try:
                    user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=email))
                except User.DoesNotExist:
                    user = None
                if user is None:
                    user = User.objects.create_user(username=username,email=email, first_name = fname, last_name = lname,password=password)
                    user.save()
                    student = form.save(commit=False)
                    student.student = user
                    student.save()
                    messages.success(request,"Signup succes !")
                    return redirect("login")
                messages.error(request,"User With profile has already Exist!")
    if type == "teach":
        return render(request,"signup.html",{"form": Teacher_form(),"teach":True})
    return render(request,"signup.html",{"form": Student_form()})


def logout(request):
    auth.logout(request)
    return redirect("login")

def profile(request):
    return render(request,"student_profile.html")