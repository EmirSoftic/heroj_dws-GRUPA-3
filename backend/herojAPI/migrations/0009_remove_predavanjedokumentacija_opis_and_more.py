# Generated by Django 4.2.1 on 2023-05-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herojAPI', '0008_remove_nesrece_simptomi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predavanjedokumentacija',
            name='opis',
        ),
        migrations.AlterField(
            model_name='predavanjedokumentacija',
            name='dokumentacija',
            field=models.FileField(max_length=255, upload_to=None),
        ),
    ]