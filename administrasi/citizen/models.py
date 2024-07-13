from django.db import models
import os

#family
class KartuKeluarga(models.Model):
    seri_terbit = models.CharField(max_length=20, unique=True)
    no_kk = models.CharField(max_length=20, unique=True)
    nama_kepala = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    rt = models.CharField(max_length=4)
    rw = models.CharField(max_length=4)
    kelurahan = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=50)
    kabupaten = models.CharField(max_length=50)
    kode_pos = models.CharField(max_length=10)
    provinsi = models.CharField(max_length=50)
    tanggal_dikeluarkan = models.DateField()
    ka_dinas = models.CharField(max_length=50, default="PERSONS 1")
    jumlah_anggota_keluarga = models.IntegerField(null=True, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.no_kk)
    
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)


#citizen
class KartuTandaPenduduk(models.Model):
    no_kk = models.ForeignKey(KartuKeluarga, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=100)
    nik = models.CharField(max_length=50, unique=True, null=False)
    jenis_kelamin = models.CharField(max_length=10)
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
    agama = models.CharField(max_length=50)
    pendidikan = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=50)
    pernikahan = models.CharField(max_length=50)
    status_keluarga = models.CharField(max_length=100)
    kewarganegaraan = models.CharField(max_length=50)
    passpor = models.CharField(max_length=50, null=True)
    kitas = models.CharField(max_length=50,null= True)
    nama_ayah = models.CharField(max_length=50)
    nama_ibu = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nama_lengkap


    
    
    
