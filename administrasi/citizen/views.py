from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#index
def citizenindex(request):
    return HttpResponse("Hello Index")
# create record
def citizencreate(request):
    return HttpResponse("Hello Create Citizen")
#view datas
def citizenview(request):
    return HttpResponse("Hello View Detail Citizen")
#delete
def citizendelete(request):
    return HttpResponse("Hello Delete Data Citizen")