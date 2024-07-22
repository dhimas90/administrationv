from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import KartuKeluarga, KartuTandaPenduduk
#route
    # path('kk/', views.indexkk, name='indexkk'),
    # path('kk/<int:id>/detail', views.detailkk, name='detailkk'),
    # path('kk/<int:id>/update', views.updatekk, name='updatekk'),
    # path('kk/<int:id>/delete', views.deletekk, name='deletekk'),
    
    # #ktp
    # path('ktp/', views.indexktp, name='indexktp'),
    # path('ktp/<int:id>/detail', views.detailktp, name='detailktp'),
    # path('ktp/<int:id>/update', views.updatektp, name='updatektp'),
    # path('ktp/<int:id>/delete', views.deletektp, name='deletektp'),

#kk
def indexkk(request):
    data = KartuKeluarga.objects.all()
    template = "kk/index.html"
    context = {'data' : data}
    return render(request, template, context)

def createkk(request):
    return HttpResponse("buat kk")

def detailkk(request, id):
    #template = null
    #context = {}
    return HttpResponse(id)

def updatekk(request, id):
    return HttpResponse(id)

def deletekk(request, id):
    return HttpResponse(id)


#ktp
def indexktp(request):
    return HttpResponse("ok ktp")

def createktp(request):
    return HttpResponse("buat ktp")

def detailktp(request, id):
    return HttpResponse(id)

def updatektp(request, id):
    return HttpResponse(id)

def deletektp(request, id):
    return HttpResponse(id)
