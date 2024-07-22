
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #kk 
    path('kk/', views.indexkk, name='indexkk'),
    path('kk/create', views.createkk, name='createkk'),
    path('kk/<int:id>/detail', views.detailkk, name='detailkk'),
    path('kk/<int:id>/update', views.updatekk, name='updatekk'),
    path('kk/<int:id>/delete', views.deletekk, name='deletekk'),
    
    #ktp
    path('ktp/', views.indexktp, name='indexktp'),
    path('ktp/create', views.createktp, name='createktp'),
    path('ktp/<int:id>/detail', views.detailktp, name='detailktp'),
    path('ktp/<int:id>/update', views.updatektp, name='updatektp'),
    path('ktp/<int:id>/delete', views.deletektp, name='deletektp'),
    
] 
