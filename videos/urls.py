from django.urls import path
from . import views
urlpatterns = [
    path("upload/",views.upload_video,name="upload"),
    path("E_<slug>/",views.edit_video,name="edit_video"),
    path("D_<slug>/",views.delete_video,name="delete_video"),
    path("<slug>/",views.videos,name="video"),
]