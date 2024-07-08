# Generated by Django 5.0.6 on 2024-07-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='goblog',
        ),
        migrations.AlterField(
            model_name='citizen',
            name='gender',
            field=models.CharField(choices=[('Laki-laki', 'Laki-Laki'), ('Perempuan', 'Perempuan')], max_length=10),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='graduate',
            field=models.CharField(choices=[('SD', 'Sekolah Dasar/Sederajat'), ('SMP', 'Sekolah Menengah Pertama/Sederajat'), ('SMA', 'Sekolah Menengah Atas/Sederajat'), ('Diploma', 'Diploma I/II/III/IV'), ('Sarjana', 'Sarjana'), ('Magister', 'Magister'), ('Doctoral', 'Doctoral')], max_length=10),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='status_in_family',
            field=models.CharField(choices=[('Anak', 'Anak'), ('Orang Tua', 'Orang Tua')], max_length=10),
        ),
        migrations.AlterField(
            model_name='familycard',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]