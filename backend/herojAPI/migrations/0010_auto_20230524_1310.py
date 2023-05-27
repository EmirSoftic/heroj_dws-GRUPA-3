# Generated by Django 3.1.14 on 2023-05-24 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('herojAPI', '0009_korisnik1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historijanesreca',
            name='korisnikid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herojAPI.korisnik1'),
        ),
        migrations.AlterField(
            model_name='rezultatitestiranja',
            name='korisnikid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herojAPI.korisnik1'),
        ),
        migrations.DeleteModel(
            name='Korisnik',
        ),
    ]