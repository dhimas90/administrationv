
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.citizenindex, name='indexcitizen'),
    path("createcitizen/", views.citizencreate, name='createcitizen'),
    path("detailcitizen/", views.citizenview, name='viewcitizen'),
    path("deletecitizen/", views.citizendelete, name='deletecitizen'),
  
    path("familycard/", views.familycardindex, name='indexfamilycard'),
    path("familycard/create", views.familycardcreate, name='createfamilycard'),
    path("familycard/<int:id>/update/", views.familycardupdate, name='updatefamilycard'),
    path("familycard/<int:id>/details/", views.familycarddetails, name='detailsfamilycard'),
    path("familycard/<int:id>/delete/", views.familycarddelete, name='deletefamilycard'),
] 
