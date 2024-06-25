from django.db import models

# Create your models here.
class Citizen(models.Model):
    GENDER = {
        "L":"Laki-Laki",
        "P":"Perempuan",
    }
    GRADUATE = {
        "SD" : "Sekolah Dasar/Sederajat",
        "SMP" : "Sekolah Menengah Pertama/Sederajat",
        "SMA" : "Sekolah Menengah Atas/Sederajat",
        "D" : "Diploma I/II/III/IV",
        "S" : "Sarjana",
        "M" : "Magister",
        "Dr" : "Doctoral",
    }
    MARRIAGE = {
        "K" : "Kawin",
        "BK" : "Belum Kawin",
        "J" : "Janda",
        "D" : "Duda",
    }
    STATUS = {
        "A" : "Anak",
        "OT" : "Orang Tua",
    }
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


class FamilyCard(models.Model):
       card_number = models.CharField(max_length=100, unique=True)
       address = models.CharField(max_length=100)
       neighbourhood_t = models.CharField(max_length=5)
       neighbourhood_w = models.CharField(max_length=5)
       subdistrict = models.CharField(max_length=50)
       district = models.CharField(max_length=50)
       province = models.CharField(max_length=50)
       postalcode = models.CharField(unique=True, max_length=10)
       image = models.ImageField(max_length=100, required=False)
       