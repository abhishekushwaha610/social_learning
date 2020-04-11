from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("signup/<str:type>",views.signup,name="signup"),
    path("edit-profile",views.edit_profile,name="edit_profile"),
    # path("edit-profile",views.delete_profile,name="delete_profile"),
    # foggot password
    path('reset_password/',auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("<str:username>/",views.profile,name="profile"),
    
]