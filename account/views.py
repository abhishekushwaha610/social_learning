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

def is_teacher(user):
    try:
        teacher = user.teacher
    except:
        teacher = None
    return teacher
    
def login(request):
    if request.method == "POST":
        email_or_username = request.POST["email_or_username"]
        password = request.POST["password"]
        user = auth.authenticate(username = email_or_username,password=password)
        if user is None:
            messages.error(request,"Invalid username or Password")
            return redirect("login")
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
                return render(request,"signup.html",{"form": form})
            else:
                try:
                    user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=email))
                except User.DoesNotExist:
                    user = None
                if user is None:
                    user = User.objects.create_user(username=username,email=email, first_name = fname, last_name = lname,password=password)
                    user.save()
                    profile = form.save(commit=False)
                    if type == "teach":
                        print("teacher form")
                        profile.teacher = user
                    else:
                        profile.student = user
                        
                    profile.save()
                    messages.success(request,"Signup succes !")
                    return redirect("login")
                messages.error(request,"User With profile has already Exist!")
        else:
            print("Not valid")
            if type == "teach":
                return render(request,"signup.html",{"form": form,"teach":True})
            return render(request,"signup.html",{"form": form,})
            
    if type == "teach":
        return render(request,"signup.html",{"form": Teacher_form(),"teach":True})
    return render(request,"signup.html",{"form": Student_form()})


def logout(request):
    auth.logout(request)
    return redirect("login")

def profile(request,username):
    user = User.objects.get(username=username)
    teacher = is_teacher(user)
    if teacher:
        print('teacher')
        return render(request,"teacher_profile.html",{'user':user})
    return render(request,"student_profile.html",{'user':user})


def edit_profile(request):
    teacher = is_teacher(request.user)
    if request.method == "POST":
        if teacher:
            form = Teacher_form(request.POST,request.FILES,instance=teacher)
        else:
            form = Student_form(request.POST,request.FILES,instance=request.user.student)    
        if form.is_valid():
            fname = request.POST["fname"]
            lname = request.POST["lname"]
            username = request.POST["username"]
            email = request.POST["email"]
        
            form.save(commit=True)
            request.user.first_name = fname
            request.user.last_name = lname
            request.user.username = username
            request.user.email = email
            request.user.save()
            return redirect("profile", request.user.username)
        else:
            messages.error(request,"Something went wrong please try again !")
            return redirect("edit_profile")
    if teacher:
        return render(request,"signup.html",{"form": Teacher_form(),"teach":True,"edit":True})
    return render(request,"signup.html",{"form": Student_form(),"edit":True})
    