from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import FamilyCard, Citizen
from .forms import FamilyCardForm
from django.contrib import messages
import os

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
    templates = 'familycard/create.html'
    if request.method == "POST":
        form = FamilyCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "successfull add record")
            return redirect('indexfamilycard')
    else:
        form = FamilyCardForm()
    return render(request, templates, {'form' : form} )
#edit record
def familycardupdate(request, id):
    data = get_object_or_404(FamilyCard, id=id)
    if request.method == "POST":
        form = FamilyCardForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'data updated succesfully')
            return redirect('indexfamilycard')
    else:
        form = FamilyCardForm(instance=data)
        return render(request, 'familycard/edit.html', {'data' : data})
    
def familycarddetails(request, id):
    template = "familycard/detail.html"
    context = {}
    try:
        data = FamilyCard.objects.get(id=id)
    except:
        raise Http404("Data Not Found")
    return render(request, template, {"data" : data})
#delete
def familycarddelete(request,id):
    data = get_object_or_404(FamilyCard, id=id)
    
    if request.method == "GET":
        data.delete()
        messages.success(request, "Data berhasil di hapus")
        return redirect('indexfamilycard')
    
    