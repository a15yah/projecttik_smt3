# Generated by Django 4.1.1 on 2022-10-06 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fkip', '0003_rename_tanggal_lahir_dosen_jabatan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosen',
            name='alamat',
        ),
    ]
