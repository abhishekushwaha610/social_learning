from django.urls import path
from . import views
# from .views import add_to_playlist

# app_name = 'videos'

urlpatterns = [
    path("allvideos/",views.all_videos,name="all_video"),
    path("videos/",views.AllList.as_view(),name="all_video"),
    path("upload/",views.upload_video,name="upload"),
    path("E_<slug>/",views.edit_video,name="edit_video"),
    path("D_<slug>/",views.delete_video,name="delete_video"),
    path("comment-save/<int:video_id>/<int:comment_id>",views.comment_save,name="comment_save"),
    path("delete-comment/<int:comment_id>",views.comment_delete,name="comment_delete"),
    # path("add-to-playlist/<slug>/",add_to_playlist,name="add-to-playlist"),
    # path("playlist/",views.show_playlist,name="show_playlist"),
    path("<slug>/",views.videos,name="video"),
]