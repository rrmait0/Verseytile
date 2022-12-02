from django.urls import path
from . import views

urlpatterns = [

    path("", views.homepage, name="homepage"),
    path("<a_forum>",views.a_forum,name="a_forum"),
    path("<a_forum>/<discuss>",views.discuss,name="discuss"),

]