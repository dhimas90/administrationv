from django.shortcuts import render
from django.http import HttpResponse, Http404
from citizen.models import FamilyCard, Citizen
# Create your views here.
#index
def citizenindex(request):
    try:
        data = Citizen.objects.all()
    except:
        raise Http404("Data not found")
    return render(request, 'citizen/header.html', {"data" : data} )
# create record
def citizencreate(request):
    return HttpResponse("Hello Create Citizen")
#view datas
def citizenview(request):
    return HttpResponse("Hello View Detail Citizen")
#delete
def citizendelete(request):
    return HttpResponse("Hello Delete Data Citizen")

def familycardindex(request):
    try:
        data = FamilyCard.objects.all()
    except:
        raise Http404("Data doesn't exist")
    return render(request, "familycard/header.html", {"data" : data})
# create record
def familycardcreate(request):
    return HttpResponse("Hello Create familycard")
#view datas
def familycardview(request):
    return HttpResponse("Hello View Detail familycard")
#delete
def familycarddelete(request):
    return HttpResponse("Hello Delete Data familycard")