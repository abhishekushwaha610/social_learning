from django.urls import path
from . import views
# from .views import SurveyFormView
urlpatterns = [
    path("",views.home,name="home"),
    path("search/",views.search,name="search"),
    # path('survey/', SurveyFormView.as_view() , name='survey'),
]