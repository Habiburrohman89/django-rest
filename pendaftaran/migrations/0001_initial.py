# Generated by Django 5.0.3 on 2024-03-21 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pendaftaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama', models.CharField(max_length=30)),
                ('NPM', models.CharField(max_length=20)),
                ('Prodi', models.CharField(max_length=30)),
                ('Tanggal_lahir', models.DateField()),
                ('Alamat', models.TextField()),
                ('Kode_pos', models.CharField(max_length=5)),
            ],
        ),
    ]
