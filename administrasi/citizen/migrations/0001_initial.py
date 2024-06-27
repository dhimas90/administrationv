# Generated by Django 5.0.6 on 2024-06-25 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('neighbourhood_t', models.CharField(max_length=5)),
                ('neighbourhood_w', models.CharField(max_length=5)),
                ('subdistrict', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('postalcode', models.CharField(max_length=10, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='goblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('joss', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=100, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], max_length=10)),
                ('graduate', models.CharField(choices=[('SD', 'Sekolah Dasar/Sederajat'), ('SMP', 'Sekolah Menengah Pertama/Sederajat'), ('SMA', 'Sekolah Menengah Atas/Sederajat'), ('D', 'Diploma I/II/III/IV'), ('S', 'Sarjana'), ('M', 'Magister'), ('Dr', 'Doctoral')], max_length=10)),
                ('passport', models.CharField(max_length=50, unique=True)),
                ('permit', models.CharField(max_length=50, unique=True)),
                ('head_family_name', models.CharField(max_length=100)),
                ('marriage', models.CharField(choices=[('K', 'Kawin'), ('BK', 'Belum Kawin'), ('J', 'Janda'), ('D', 'Duda')], max_length=50)),
                ('status_in_family', models.CharField(choices=[('A', 'Anak'), ('OT', 'Orang Tua')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('card_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citizen.familycard')),
            ],
        ),
    ]
