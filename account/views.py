from django.shortcuts import render,HttpResponse
from django.contrib import auth 
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib import messages
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
        user = auth.authenticate(request,email_or_username,password)
        if user is None:
            messages.error(request,"User has already Exist !")
            return HttpResponse("already Exist!")
        else:
            messages.success(request,"Welcome!")
            return HttpResponse(user)
    