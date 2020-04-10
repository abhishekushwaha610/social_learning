from django.urls import path
from . import views
urlpatterns = [
     path("allvideos/",views.all_videos,name="all_video"),
    path("upload/",views.upload_video,name="upload"),
    path("E_<slug>/",views.edit_video,name="edit_video"),
    path("D_<slug>/",views.delete_video,name="delete_video"),
    path("comment-save/<int:video_id>/<int:comment_id>",views.comment_save,name="comment_save"),
    path("delete-comment/<int:comment_id>",views.comment_delete,name="comment_delete"),
    path("<slug>/",views.videos,name="video"),
    
]