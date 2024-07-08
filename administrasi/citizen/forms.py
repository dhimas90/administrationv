from django import forms
from django.forms import ModelForm
from .models import FamilyCard

class FamilyCardForm(forms.ModelForm):
    class Meta:
        model = FamilyCard
        fields = ['card_number', 
                  'neighbourhood_t',
                  'neighbourhood_w',
                  'subdistrict',
                  'district',
                  'province',
                  'postalcode',
                  'image',
                  ]