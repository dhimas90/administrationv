from django.db import models
import os
# Create your models here.

#family
class FamilyCard(models.Model):
    card_number = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    neighbourhood_t = models.CharField(max_length=5)
    neighbourhood_w = models.CharField(max_length=5)
    subdistrict = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    postalcode = models.CharField(unique=True, max_length=10)
    image = models.ImageField(max_length=100, upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
       
    def __str__(self):
        return str(self.card_number)
    
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)


#citizen
class Citizen(models.Model):
    GENDER = {
        "Laki-laki":"Laki-Laki",
        "Perempuan":"Perempuan",
    }
    GRADUATE = {
        "SD" : "Sekolah Dasar/Sederajat",
        "SMP" : "Sekolah Menengah Pertama/Sederajat",
        "SMA" : "Sekolah Menengah Atas/Sederajat",
        "Diploma" : "Diploma I/II/III/IV",
        "Sarjana" : "Sarjana",
        "Magister" : "Magister",
        "Doctoral" : "Doctoral",
    }
    MARRIAGE = {
        "K" : "Kawin",
        "BK" : "Belum Kawin",
        "J" : "Janda",
        "D" : "Duda",
    }
    STATUS = {
        "Anak" : "Anak",
        "Orang Tua" : "Orang Tua",
    }
    card_number = models.ForeignKey(FamilyCard, on_delete=models.CASCADE )
    id_number = models.CharField(unique=True,max_length=100)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER)
    graduate = models.CharField(max_length=10, choices=GRADUATE)
    passport = models.CharField(max_length=50, unique=True)
    permit = models.CharField(max_length=50, unique=True)
    head_family_name = models.CharField(max_length=100)
    marriage = models.CharField(max_length=50, choices=MARRIAGE)
    status_in_family = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name


    
    
    
