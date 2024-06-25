from django.urls import path

from . import views

urlpatterns = [
    path("", views.citizenindex, name='indexcitizen'),
    path("createcitizen/", views.citizencreate, name='createcitizen'),
    path("detailcitizen/", views.citizenview, name='viewcitizen'),
    path("deletecitizen/", views.citizendelete, name='deletecitizen'),
]
